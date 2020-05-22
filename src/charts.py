from collections import Counter
import base64
from io import BytesIO
from wordcloud import WordCloud
from src.chat_parser import encode_emoji
from src.settings import CHART_HEIGHT, DAYS, HOURS, CATEGORIES, CONTENT, LANGUAGE
from src.stopwords import get_stopwords

def chart1(df, interval):
    """Generate time series figure chart."""
    pivoted = df[[interval, 'category']].pivot_table(index=interval, columns='category', aggfunc=len, fill_value=0).reset_index()
    return {
        'data': [{'x': pivoted[interval], 'y': pivoted[category], 'type': 'bar', 'name': category} for category in sorted(pivoted.columns)[::-1] if category != interval],
        'layout': {
            'barmode': 'stack',
            'height': CHART_HEIGHT,
            'showlegend': True,
            'legend': {'x': 1, 'y': 1, 'xanchor': 'right', 'orientation': 'h'},
            'margin': {'l': 30, 'r': 30, 't': 10, 'b': 30}}}

def chart2(df):
    """Generate daily chat activity figure chart."""
    pivoted = df.groupby('day').size()
    return {
        'data':[{
            'type': 'scatterpolar',
            'r': [pivoted.get(day, default=0) for day in DAYS],
            'theta': DAYS,
            'fill': 'toself'}],
        'layout': {
            'height': CHART_HEIGHT,
            'margin': {'l': 50, 'r': 60, 't': 20, 'b': 20},
            'polar': {
                'radialaxis': {'range': [0, max(pivoted)*1.1], 'nticks': 7, 'angle': 90, 'tickangle': 90},
                'angularaxis': {'rotation': 90, 'direction': 'clockwise', 'automargin': True}}}}

def chart3(df):
    """Generate chat activity by hour figure chart."""
    pivoted1 = df.groupby('hour').size()
    pivoted2 = df[['day', 'hour']].pivot_table(index='day', columns='hour', aggfunc=len, fill_value=0)
    return {
        'data': [{
            'type': 'scatter',
            'x': HOURS,
            'y': [pivoted1.get(i, default=0) for i in HOURS],
            'line': {'width': 3}},
            {'type': 'heatmap',
            'z': [[pivoted2.loc[i, j] if j in pivoted2.columns else 0 for j in HOURS] if i in pivoted2.index else [0]*24 for i in DAYS[::-1]],
            'x': HOURS,
            'y': [i[:3] for i in DAYS[::-1]],
            'xaxis': 'x',
            'yaxis': 'y2',
            'showscale': False}],
        'layout': {
            'grid': {'rows': 2, 'columns': 1},
            'height': CHART_HEIGHT,
            'margin': {'l': 0, 'r': 0, 't': 10, 'b': 50},
            'yaxis': {'nticks': 7, 'side': 'right', 'domain': [0.63, 1], 'automargin': True},
            'yaxis2': {'nticks': 7, 'side': 'right', 'domain': [0, 0.6], 'automargin': True}}}

def chart4(df, interval, n):
    """Generate Top n user dominance figure chart."""
    pivoted = df[[interval, 'contact']].pivot_table(index=interval, columns='contact', aggfunc=len, fill_value=0).reset_index()
    users = pivoted.sum(numeric_only=True).sort_values(ascending=False).head(n)
    return {
        'data': [{'x': pivoted[interval], 'y': pivoted[user], 'type': 'scatter', 'name': user} for user in users.index],
        'layout': {
            'height': CHART_HEIGHT,
            'showlegend': True,
            'legend': {'x': 1, 'y': 1, 'xanchor': 'right', 'orientation': 'h'},
            'margin': {'l': 30, 'r': 30, 't': 10, 'b': 30}}}

def chart5(df, n):
    """Generate Top n breakdown by content figure chart."""
    pivoted = df[['contact', 'category']].pivot_table(index='contact', columns='category', aggfunc=len, fill_value=0).reindex(columns=CATEGORIES, fill_value=0)
    users = pivoted.sum(axis=1).sort_values(ascending=False).head(n).sort_values()
    return {
        'data': [{'x': [pivoted[category][user] for user in users.index], 'y': users.index, 'type': 'bar', 'orientation': 'h', 'name': category} for category in reversed(CONTENT)],
        'layout': {
            'barmode': 'stack',
            'height': CHART_HEIGHT,
            'showlegend': True,
            'legend': {'x': 1, 'y': 1.1, 'xanchor': 'right', 'orientation': 'h'},
            'margin': {'r': 30, 't': 10, 'b': 30, 'pad': 5},
            'yaxis': {'automargin': True}}}

def chart6(df, n):
    """Generate Top n emoji used figure chart."""
    list_emoji = df[df.count_emoji > 0]['list_emoji'].sum()
    if isinstance(list_emoji, list):
        counter = Counter(list_emoji)
        n_most = counter.most_common(n)
        other = 0
        for emoji, i in counter.most_common():
            if (emoji, i) not in n_most:
                other += i
        if other:
            n_most.append(('other', other))
        values = [n for emoji, n in n_most]
        labels = [encode_emoji(emoji) for emoji, n in n_most]
    else:
        values = []
        labels = []
    return {
        'data': [{
            'values': values,
            'labels': labels,
            'type': 'pie',
            'hole': 0.4,
            'sort': False,
            'textinfo': 'label+percent',
            'textposition': 'inside',
            'insidetextfont': {'size': 30},
            'insidetextorientation': 'horizontal',
            'hoverinfo': 'label',
            'hoverlabel': {'font': {'size': 70}},
            'automargin': True}],
        'layout': {
            'height': CHART_HEIGHT,
            'showlegend': False,
            'margin': {'r': 0, 'l': 0, 't': 0, 'b': 20, 'pad': 0}}}

def chart7(df):
    """Generate WordCloud."""
    list_words = df.list_words.sum()
    stopwords = get_stopwords(list_words)
    counter = dict(Counter(list_words))
    counter = {key: counter[key] for key in counter if key not in stopwords and key.isalpha()}
    wc = WordCloud(stopwords=stopwords, prefer_horizontal=0.9, colormap='tab10', background_color='white', min_font_size=10, width=1000, height=250, scale=2)
    wc_img = wc.generate_from_frequencies(frequencies=counter).to_image()
    with BytesIO() as buffer:
        wc_img.save(buffer, 'png')
        img = "data:image/png;base64," + base64.b64encode(buffer.getvalue()).decode()
    return img

def chart8(df, lang):
    """Generate Recruitment genealogy elements chart."""
    and_conj = LANGUAGE[lang]['and']
    list_invited = df[(df.category == 'Event') & (df.event_type == 'added')][['contact', 'event_target']].values
    list_invited = [(source, tgt.strip()) for source, target in list_invited for tgt in target.replace(f' {and_conj} ', ',').split(',')]
    list_user = set([item for sublist in list_invited for item in sublist])
    return [{'data': {'id': user, 'label': user}} for user in list_user] + [{'data': {'source': source, 'target': target}} for source, target in list_invited]