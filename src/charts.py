DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
HOURS = [f'0{i}:00'[-5:] for i in range(24)]

def chart1(df, interval):
    pivoted = df[[interval, 'category']].pivot_table(index=interval, columns='category', aggfunc=len, fill_value=0).reset_index()
    return {
        'data': [{'x': pivoted[interval], 'y': pivoted[category], 'type': 'bar', 'name': category} for category in sorted(pivoted.columns)[::-1] if category != interval],
        'layout': {
            'title': 'Dash Data Visualization',
            'barmode': 'stack',
            'showlegend': True,
            'legend': {'x': '1', 'y': '1', 'xanchor': 'right', 'orientation': 'h'}}}

def chart2(df):
    pivoted = df.groupby('day').size()
    return {
        'data':[{
            'type': 'scatterpolar',
            'r': [pivoted.get(i, default=0) for i in DAYS],
            'theta': DAYS,
            'fill': 'toself'}],
        'layout': {
            'polar': {
                'radialaxis': {'range': [0, max(pivoted)*1.1], 'nticks': 7, 'angle': 90, 'tickangle': 90},
                'angularaxis': {'rotation': 90, 'direction': 'clockwise'}}}}

def chart3(df):
    pivoted = df.groupby('hour').size()
    return {
        'data': [{
            'type': 'scatter',
            'x': HOURS,
            'y': [pivoted.get(i, default=0) for i in HOURS],
            'line': {'width': 5}}]}

def chart4(df):
    pivoted = df[['day', 'hour']].pivot_table(index='day', columns='hour', aggfunc=len, fill_value=0)
    return {
        'data': [{
            'type': 'heatmap',
            'z': [[pivoted.loc[i, j] if j in pivoted.columns else 0 for j in HOURS] if i in pivoted.index else [0]*24 for i in DAYS[::-1]],
            'x': HOURS,
            'y': DAYS[::-1]
        }]
    }