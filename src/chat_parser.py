import re
import json
from datetime import datetime
import pandas as pd
import numpy as np
from src import db_handler as db
from src.settings import PATTERN

def replace_emoji(text, emoji):
    """Convert unicode character of emoji into string representation."""
    new_text = text
    for idx, emo in filter(lambda x: x[1] in text, emoji):
        new_text = new_text.replace(emo, f'<Emoji_{idx}>')
    for i in re.findall('(\\\\ufe0.|\\\\u206[89])', new_text):
        new_text = new_text.replace(i, '')
    return new_text

def detect_pattern():
    """Return python date-format pattern from first line of chat."""
    return '%m/%d/%y, %H:%M - '

def convert_to_re_pattern(pattern):
    """Convert python date-format pattern into regular expression pattern."""
    symb_conv = lambda x: '\d{1,' + str(len(datetime.today().strftime(x))) + '}'
    re_pattern = ''
    i = 0
    while i < len(pattern):
        if pattern[i] == '%':
            re_pattern += symb_conv(pattern[i:i+2])
            i += 1
        elif pattern[i] in '/()[].$^*?':
            re_pattern += '\\' + pattern[i]
        else:
            re_pattern += pattern[i]
        i += 1
    return re_pattern

def detect_language(chat):
    for lang in list(PATTERN.keys())[1:]:
        if re.match(PATTERN[lang]['events'][0], chat):
            return lang
    return 'not_supported'

def clean_message(x):
    """Remove newline, emoji, and media from message."""
    category, message = x
    if category == 'Text':
        message = message.replace('\n', ' ')
        message = re.sub(PATTERN['universal']['emoji'], '', message)
        message = re.sub(PATTERN['universal']['link'], '', message)
        message = re.sub(PATTERN['universal']['mention'], '', message)
    else:
        message = ''
    return message

def find_link(x):
    """Find links from message."""
    category, message = x
    list_link = []
    if category == 'Text':
        for link in re.findall(PATTERN['universal']['link'], message):
            if link[-1] in ['.', ',']:
                temp = link[:-1]
            else:
                temp = link
            list_link.append(temp)
    return list_link

def get_category(x, lang):
    contact, message = x
    if pd.isna(contact):
        return 'Event'
    elif re.match(PATTERN[lang]['media'], message):
        return 'Media'
    elif re.match(PATTERN[lang]['location'].format(PATTERN['universal']['link']), message):
        return 'Location'
    elif re.match(PATTERN[lang]['contact'], message):
        return 'Contact'
    elif re.match(PATTERN[lang]['deleted'], message):
        return 'Deleted'
    else:
        return 'Text'

def extract_event(text, lang):
    for event in PATTERN[lang]['events']:
        match = re.match(event, text)
        if match:
            matchs = match.groups()
            if len(matchs) == 3:
                contact, message, target = matchs
            elif len(matchs) == 2:
                contact, message, target = matchs[0], matchs[1], np.nan
            else:
                contact, message, target = np.nan, matchs[0], np.nan
            return contact, message, target
    return np.nan, text, np.nan

def enrich(df, lang):
    """Adding some column for analysis."""
    df['category'] = pd.Categorical(df[['contact', 'message']].apply(lambda x: get_category(x, lang), axis=1))
    df['clean_message'] = df[['category', 'message']].apply(clean_message, axis=1)
    df['date'] = df.datetime.dt.date
    df['year'] = df.date + pd.offsets.YearEnd(0)
    df['month'] = df.date + pd.offsets.MonthEnd(0)
    df['week'] = df.date + pd.offsets.Week(weekday=6)
    df['day'] = pd.Categorical(df.datetime.dt.strftime('%A'))
    df['hour'] = pd.Categorical(df.datetime.apply(lambda x: x.strftime('%H:00')))
    df['list_emoji'] = df.message.apply(lambda x: re.findall(PATTERN['universal']['emoji'], x))
    df['list_link'] = df[['category', 'message']].apply(find_link, axis=1)
    df['list_mention'] = df.message.apply(lambda x: re.findall(PATTERN['universal']['mention'], x))
    df['list_words'] = df.clean_message.apply(lambda x: re.findall('\w+', x))
    df['count_emoji'] = df.list_emoji.apply(len)
    df['count_link'] = df.list_link.apply(len)
    df['count_mention'] = df.list_mention.apply(len)
    df['count_words'] = df.list_words.apply(len)
    df['count_character'] = df.clean_message.apply(len)
    df['count_newline'] = df.message.str.count('\n')
    df['event_type'] = np.nan
    df['event_target'] = np.nan
    df.loc[df.category == 'Event', 'contact'], df.loc[df.category == 'Event', 'event_type'], df.loc[df.category == 'Event', 'event_target'], = zip(*df[df.category == 'Event'].message.apply(lambda x: extract_event(x, lang)))
    return df

def parse(chat):
    """Parse exported chat and define date, contact, message for each message."""
    emoji = db.get_emoji()[['index', 'unicode']].values.tolist()

    chat = chat.decode().encode('unicode_escape').decode('utf-8')
    lang = detect_language(chat)

    if lang == 'not_supported':
        df = pd.DataFrame()
    else:
        pattern = PATTERN[lang]['date'] + ' - '
        re_pattern = convert_to_re_pattern(pattern)

        dates = re.findall(re_pattern, chat)
        msgs = re.split(re_pattern, chat)
        msgs.pop(0)

        data = []
        for date, msg in zip(dates, msgs):
            date = datetime.strptime(date, pattern)
            msg_splitted = msg.split(': ', 1)
            if len(msg_splitted) > 1:
                contact, msg = msg_splitted
            else:
                contact, msg = np.nan, msg_splitted[0]
            if '\\U000' in msg or '\\u' in msg:
                msg = replace_emoji(msg, emoji)
            if msg[-2:] == '\\n':
                msg = msg[:-2]
            data.append({
                'datetime': date,
                'contact': contact,
                'message': msg.encode().decode('unicode_escape')})
        df = pd.DataFrame(data)
    return df, lang

def load_parsed_data(input_string, input_type, save=True):
    if input_type == 'upload':
        df, lang = parse(input_string)
        url = db.generate_url(10)
        if save and not df.empty:
            db.reset_chat() # TODO: delete this for production
            url = db.add_chat(df, lang, url)
    elif input_type == 'url':
        url = input_string
        df, lang = db.get_chat(url)

    if lang in ['not_supported', 'not_found']:
        return lang, {'data': ''}

    df = enrich(df, lang)
    # TODO: support for both private & group chat
    group_created = df[(df.category == 'Event') & (df.event_type == 'created group')]
    chat_name = df[(df.category == 'Event') & (df.event_type.isin(['created group', 'changed the subject']))].tail(1)['event_target']
    users = sorted(filter(lambda x: pd.notna(x) and x != 'You', df.contact.unique().tolist()))
    df = df.drop(group_created.index)
    df = df.drop(['message', 'clean_message'], axis=1)
    datasets = {
        'data': df.to_json(date_format='iso', orient='split'),
        'users': users,
        'chat_name': chat_name.values[0],
        'chat_created_by': group_created['contact'].values[0],
        'chat_created_at': group_created['datetime'].dt.strftime('%d %b %Y').values[0]
    }
    # TODO: create method to check Series.values is empty, to avoid IndexError: index 0 is out of bounds for axis 0 with size 0
    return '/groupchat/' + url, json.dumps(datasets)