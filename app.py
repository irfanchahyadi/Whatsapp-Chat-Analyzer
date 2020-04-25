import base64, json
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from src import charts, chat_parser, layouts, settings

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
server = app.server
app.config.suppress_callback_exceptions = True


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    dcc.Loading(type='graph', fullscreen=True, children=[
        html.Div(id='container-data-store', style={'display': 'none'}, children=[
            dcc.Store(id='data-store')])])
])

@app.callback([Output('page-content', 'children'), Output('container-data-store', 'children')], [Input('url', 'pathname')])
def display_page(pathname):
    container_data_store = dash.no_update
    if pathname == '/':
        page_content = layouts.home
    elif pathname.startswith('/groupchat/') or pathname.startswith('/personalchat/'):
        chat_type, url_key = pathname[1:].split('/')
        page_content = layouts.groupchat if chat_type == 'groupchat' else None
        if not pathname.endswith(settings.FROM_LANDING_PAGE):
            url, datasets = chat_parser.load_parsed_data(url_key, 'url')
            container_data_store = dcc.Store(id='data-store', data=datasets)
            if url == 'not_found':
                page_content = layouts.not_found
    elif pathname.endswith('not_found'):
        page_content = layouts.not_found
    else:
        page_content = layouts.page_404
    return page_content, container_data_store

@app.callback(
    [Output('url', 'pathname'), Output('data-store', 'data'), Output('alert-container', 'children')],
    [Input('upload-data', 'contents'), Input('url-submit', 'n_clicks')],
    [State('save-switch', 'on'), State('url-input', 'value')])
def upload_data(contents, n_click, save, url_input):
    ctx = dash.callback_context
    url, datasets, alert = dash.no_update, dash.no_update, dash.no_update
    if ctx.triggered[0]['prop_id'] == 'upload-data.contents':
        content_type, content = contents.split(',')
        if content_type == 'data:text/plain;base64':
            content_decoded = base64.b64decode(content)
            url, datasets = chat_parser.load_parsed_data(content_decoded, 'upload', save)
            if url == 'not_supported':
                supported_language = ', '.join([settings.PATTERN[i]['language'] for i in list(settings.PATTERN.keys())[1:]])
                alert = dbc.Alert('Language not supported. Currently support: {} language.'.format(supported_language), dismissable=True, color='danger')
                url = dash.no_update
            else:
                url = url + settings.FROM_LANDING_PAGE
        else:
            alert = dbc.Alert('Wrong file type, please upload txt file from exported Whatsapp chat.', dismissable=True, color='danger')
    elif ctx.triggered[0]['prop_id'] == 'url-submit.n_clicks':
        url, datasets = chat_parser.load_parsed_data(url_input, 'url')
        if url != 'not_found':
            url = url + settings.FROM_LANDING_PAGE
    return url, datasets, alert

@app.callback(
    [Output('dropdown-users', 'options'), Output('navbar-brand', 'children'), Output('created-by', 'children'), Output('count-user', 'children')],
    [Input('dropdown-users', 'value')], [State('data-store', 'data')])
def fill_dropdown_users(dropdown_users, datasets):
    datasets = json.loads(datasets)
    df = pd.read_json(datasets['data'], orient='split')
    output = [
        [{'label': i, 'value': i} for i in datasets['users']],
        datasets['chat_name'],
        '{} at {}'.format(datasets['chat_created_by'], datasets['chat_created_at']),
        '{:,} active, {:,} left group'.format(len(datasets['users']), df[(df.category == 'Event') & (df.event_type == 'left')].shape[0])
    ]
    return output

@app.callback(Output('selectall-users-container', 'children'), [Input('dropdown-users', 'value')], [State('selectall-users', 'value')])
def update_selectall_users(dropdown_users, select_all):
    if len(dropdown_users) > 0 and select_all == [1]:
        select_all_container = dcc.Checklist(id='selectall-users', options=[{'label': 'Select All', 'value': 1}], value=[])
    elif len(dropdown_users) == 0 and select_all == []:
        select_all_container = dcc.Checklist(id='selectall-users', options=[{'label': 'Select All', 'value': 1}], value=[1])
    else:
        select_all_container = dash.no_update
    return select_all_container

@app.callback(Output('dropdown-users-container', 'children'), [Input('selectall-users', 'value')], [State('dropdown-users', 'value')])
def update_dropdown_users(select_all, dropdown_users):
    if select_all == [1] and len(dropdown_users) > 0:
        return dcc.Dropdown(id='dropdown-users', options=[], multi=True, value=[])
    else:
        return dash.no_update

@app.callback(
    [Output('counter', 'children'), Output('count-message', 'children'), Output('count-word', 'children'), Output('count-emoji', 'children'), Output('count-mention', 'children'),
     Output('count-media', 'children'), Output('count-location', 'children'), Output('count-link', 'children'), Output('count-contact', 'children'),
     Output('chart-1', 'figure'), Output('chart-2', 'figure'), Output('chart-3', 'figure'),
     Output('avg-user', 'children'), Output('avg-message', 'children'), Output('avg-day', 'children'), Output('avg-month', 'children'),
     Output('most-busy', 'children'), Output('most-active', 'children'), Output('most-silent', 'children'), Output('most-typer', 'children'),
     Output('most-emoji', 'children'), Output('most-media', 'children'), Output('most-location', 'children'), Output('most-link', 'children'),
     Output('most-contact', 'children'), Output('most-mention', 'children'), Output('most-add', 'children'), Output('most-deleted', 'children')],
    [Input('dropdown-users', 'value'), Input('time-interval1', 'value')],
    [State('data-store', 'data')])
def update_filter(dropdown_users, interval, datasets):
    datasets = json.loads(datasets)
    df = pd.read_json(datasets['data'], orient='split')
    filtered_df = df[((df.contact.isin(dropdown_users)) | (len(dropdown_users) == 0))]
    output = [dash.no_update] * 20
    ctx = dash.callback_context
    if ctx.triggered[0]['prop_id'] == 'time-interval.value':
        output[9] = charts.chart1(filtered_df, interval)
    else:
        by_category = filtered_df[['contact', 'category']].pivot_table(index='contact', columns='category', aggfunc=len, fill_value=0).reindex(columns=['Contact', 'Deleted', 'Event', 'Location', 'Media', 'Text'], fill_value=0)
        by_column = filtered_df.groupby('contact').sum(numeric_only=True)
        output = [
            filtered_df.groupby('day').size(),
            '{:,} sent, {:,} deleted'.format(by_category.sum().sum() - by_category['Event'].sum(), by_category['Deleted'].sum()),
            '{:,} sent'.format(by_column['count_words'].sum()),
            '{:,} sent'.format(by_column['count_emoji'].sum()),
            '{:,} sent'.format(by_column['count_mention'].sum()),
            '{:,} shared'.format(by_category['Media'].sum()),
            '{:,} shared'.format(by_category['Location'].sum()),
            '{:,} shared'.format(by_column['count_link'].sum()),
            '{:,} shared'.format(by_category['Contact'].sum()),
            charts.chart1(filtered_df, interval),
            charts.chart2(filtered_df),
            charts.chart3(filtered_df),
            '{:,.2f} messages'.format((by_category.sum().sum() - by_category['Event'].sum())/filtered_df.contact.nunique(dropna=True)),
            '{:,.2f} words, {:.2f} emoji'.format(by_column['count_words'].sum()/by_category['Text'].sum(), by_column['count_emoji'].sum()/by_category['Text'].sum()),
            '{:,.2f} text, {:.2f} media'.format(by_category['Text'].sum()/filtered_df.date.nunique(), by_category['Media'].sum()/filtered_df.date.nunique()),
            '{:,.2f} text, {:.2f} media'.format(by_category['Text'].sum()/filtered_df.month.nunique(), by_category['Media'].sum()/filtered_df.month.nunique()),
            layouts.award_list(filtered_df.groupby('date').size().sort_values(ascending=False)),
            layouts.award_list((by_category.sum(axis=1) - by_category['Event']).sort_values(ascending=False)),
            layouts.award_list((by_category.sum(axis=1) - by_category['Event'])[lambda x: x > 0].sort_values(ascending=True)),
            layouts.award_list(by_column['count_character'].sort_values(ascending=False)),
            layouts.award_list(by_column['count_emoji'].sort_values(ascending=False)),
            layouts.award_list(by_category['Media'].sort_values(ascending=False)),
            layouts.award_list(by_category['Location'].sort_values(ascending=False)),
            layouts.award_list(by_column['count_link'].sort_values(ascending=False)),
            layouts.award_list(by_category['Contact'].sort_values(ascending=False)),
            layouts.award_list(by_column['count_mention'].sort_values(ascending=False)),
            layouts.award_list(filtered_df[(filtered_df.category == 'Event') & (filtered_df.event_type == 'added')].groupby('contact').size().sort_values(ascending=False)),
            layouts.award_list(by_category['Deleted'].sort_values(ascending=False)),
        ]
    return output

if __name__ == "__main__":
    app.run_server(debug=True)
