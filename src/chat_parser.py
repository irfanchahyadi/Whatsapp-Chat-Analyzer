import re
import json
from datetime import datetime
import pandas as pd
import numpy as np
from src import db_handler as db
from src.settings import LANGUAGE, PATTERN, LINK_LOCATION
from src.emoji import EMOJI, DEMOJI, CLEANER

emoji_pattern = re.compile('|'.join(sorted([re.escape(emo) for emo in EMOJI], key=len, reverse=True)))
demoji_pattern = re.compile('|'.join(DEMOJI))
cleaner_pattern = re.compile('|'.join([re.escape(c) for c in CLEANER]))

def get_pattern(key, lang='en'):
    """Provide regex pattern for emoji, link, mention, media, location, contact, deleted and events."""
    re_patterns = PATTERN[key]
    if isinstance(re_patterns, list):
        re_patterns = [re_pattern.format(**LANGUAGE[lang]) for re_pattern in re_patterns]
    elif key != 'mention':
        re_patterns = re_patterns.format(**LANGUAGE[lang])
    return re_patterns

def translate_event_type(event_type, lang):
    """Translate non english event type to standard english event type."""
    event_index = {v: k for k, v in LANGUAGE[lang].items()}[event_type]
    return LANGUAGE['en'][event_index]

def decode_emoji(text):
    """Convert unicode character of emoji into string representation."""
    replaced = emoji_pattern.sub(lambda x: '<Emoji_' + str(EMOJI.get(x.group(0))) + '>', text)
    cleaned = cleaner_pattern.sub('', replaced)
    if cleaned[-1:] == '\n':
        cleaned = cleaned[:-1]
    return cleaned

def encode_emoji(text):
    """Convert emoji string representation to unicode character."""
    return demoji_pattern.sub(lambda x: DEMOJI.get(x.group(0)), text)

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
    """Detect android system language when exporting chat history, affect date format, event type, and non text object declaration."""
    for lang in LANGUAGE:
        if re.search(get_pattern('events', lang)[0], chat):
            return lang, 'groupchat'
        elif re.search(get_pattern('events', lang)[1], chat):
            return lang, 'personalchat'
    return 'not_supported', ''

def clean_message(x):
    """Remove newline, emoji, link, mention, and other non text object from message."""
    category, message = x
    if category == 'Text':
        message = message.replace('\n', ' ')
        message = re.sub(get_pattern('emoji'), '', message)
        message = re.sub(get_pattern('link'), '', message)
        message = re.sub(get_pattern('mention'), '', message)
    else:
        message = ''
    return message

def find_link(x):
    """Find links from message."""
    category, message = x
    list_link = []
    if category == 'Text':
        for link in re.findall(get_pattern('link'), message):
            temp = link[:-1] if link[-1] in ['.', ','] else link
            temp = temp[2:] if temp[:2] in ['m.'] else temp
            if temp not in LINK_LOCATION:
                list_link.append(temp)
    return list_link

def find_word(text):
    """Find words from message."""
    words = re.findall('\w+', text)
    return [word.lower() for word in words]

def get_category(x, lang):
    """Define category (Event, Media, Location, Contact, Deleted, and Text) for each message."""
    contact, message = x
    if pd.isna(contact):
        return 'Event'
    elif re.match(get_pattern('media', lang), message):
        return 'Media'
    elif re.match(get_pattern('location', lang), message):
        return 'Location'
    elif re.match(get_pattern('contact', lang), message):
        return 'Contact'
    elif re.match(get_pattern('deleted', lang), message):
        return 'Deleted'
    else:
        return 'Text'

def extract_event(text, lang):
    """Define subject, type, and target for every event."""
    for event in get_pattern('events', lang):
        match = re.match(event, text)
        if match:
            matchs = match.groups()
            if len(matchs) == 3:
                contact, event_type, target = matchs
                if target == LANGUAGE[lang]['you'].lower():
                    target = LANGUAGE[lang]['you']
            elif len(matchs) == 2:
                contact, event_type, target = matchs[0], matchs[1], np.nan
            else:
                contact, event_type, target = np.nan, matchs[0], np.nan
            if lang != 'en':
                event_type = translate_event_type(event_type, lang)
            if isinstance(contact, str):
                contact = contact.replace('\\u200e', '')
            return contact, event_type, target
    return np.nan, text, np.nan

def enrich(df, lang):
    """Adding some column for analysis purpose."""
    df['category'] = pd.Categorical(df[['contact', 'message']].apply(lambda x: get_category(x, lang), axis=1))
    df['clean_message'] = df[['category', 'message']].apply(clean_message, axis=1)
    df['date'] = df.datetime.dt.date
    df['year'] = df.date + pd.offsets.YearEnd(0)
    df['month'] = df.date + pd.offsets.MonthEnd(0)
    df['week'] = df.date + pd.offsets.Week(weekday=6)
    df['day'] = pd.Categorical(df.datetime.dt.strftime('%A'))
    df['hour'] = pd.Categorical(df.datetime.apply(lambda x: x.strftime('%H:00')))
    df['list_emoji'] = df.message.apply(lambda x: re.findall(get_pattern('emoji'), x))
    df['list_link'] = df[['category', 'message']].apply(find_link, axis=1)
    df['list_mention'] = df.message.apply(lambda x: re.findall(get_pattern('mention'), x))
    df['list_words'] = df.clean_message.apply(find_word)
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
    chat = chat.decode('utf-8')
    lang, chat_type = detect_language(chat)

    if lang == 'not_supported':
        df = pd.DataFrame()
    else:
        pattern = LANGUAGE[lang]['date'] + ' - '
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
            msg = decode_emoji(msg)
            data.append({
                'datetime': date,
                'contact': contact,
                'message': msg.encode('unicode_escape').decode()})
        df = pd.DataFrame(data)
    return df, chat_type, lang

def load_parsed_data(input_string, input_type, save=True):
    """Grab chat data, parse, enrich, and store information to client side."""
    if input_type == 'upload':
        df, chat_type, lang = parse(input_string)
        url = db.generate_url(10, unique=save)
        if save and not df.empty:
            url = db.add_chat(df, lang, chat_type, url)
    elif input_type == 'url':
        url = input_string
        df, chat_type, lang = db.get_chat(url)

    if lang in ['not_supported', 'not_found']:
        return lang, {'data': ''}

    df = enrich(df, lang)
    users = sorted(filter(lambda x: pd.notna(x), df.contact.unique().tolist()))
    if chat_type == 'groupchat':
        chat_name = encode_emoji(df[(df.category == 'Event') & (df.event_type.isin(['created group', 'changed the subject from']))].tail(1)['event_target'].values[0])
        chat_created = df[(df.category == 'Event') & (df.event_type == 'created group')]
        df = df.drop(chat_created.index[0])
    elif chat_type == 'personalchat':
        chat_name = ' & '.join(users)
        chat_created = df[df.category != 'Event'].sort_values('datetime').head(1)
    df = df.drop(['message', 'clean_message'], axis=1)
    datasets = {
        'data': df.to_json(date_format='iso', orient='split'),
        'lang': lang,
        'users': users,
        'chat_name': chat_name,
        'chat_created_by': chat_created['contact'].values[0],
        'chat_created_at': chat_created['datetime'].dt.strftime('%d %b %Y').values[0],
        'chat_min_date': df.datetime.min().strftime('%Y-%m-%d'),
        'chat_max_date': df.datetime.max().strftime('%Y-%m-%d')
    }
    # TODO: create method to check Series.values is empty, to avoid IndexError: index 0 is out of bounds for axis 0 with size 0
    return f'/{chat_type}/' + url, json.dumps(datasets)