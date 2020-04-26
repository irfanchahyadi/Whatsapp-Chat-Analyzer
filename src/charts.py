from src.settings import CHART_HEIGHT, DAYS, HOURS, CATEGORIES, CONTENT

def chart1(df, interval):
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
            'yaxis': {'nticks': 7, 'side': 'right', 'domain': [0.55, 1], 'automargin': True},
            'yaxis2': {'side': 'right', 'domain': [0, 0.53], 'automargin': True}}}

def chart4(df, interval, n):
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
    pivoted = df[['contact', 'category']].pivot_table(index='contact', columns='category', aggfunc=len, fill_value=0).reindex(columns=CATEGORIES, fill_value=0)
    users = pivoted.sum(axis=1).sort_values(ascending=False).head(n)
    return {
        'data': [{'x': [pivoted[category][user] for user in reversed(users.index)], 'y': users.index, 'type': 'bar', 'orientation': 'h', 'name': category} for category in reversed(CONTENT)],
        'layout': {
            'barmode': 'stack',
            'height': CHART_HEIGHT,
            'showlegend': True,
            'legend': {'x': 1, 'y': 1.1, 'xanchor': 'right', 'orientation': 'h'},
            'margin': {'r': 30, 't': 10, 'b': 30, 'pad': 5},
            'yaxis': {'automargin': True}}}