import base64, json
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from src import charts, chat_parser, layouts

FROM_LANDING_PAGE = '?from=landing_page'

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
server = app.server
app.config.suppress_callback_exceptions = True


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content',
        style={
            # 'padding': '50px'
        }),
    dcc.Loading(type='graph', fullscreen=True, children=[
        html.Div(id='container-data-store', style={'display': 'none'}, children=[
            dcc.Store(id='data-store')])])
])

@app.callback([Output('page-content', 'children'), Output('container-data-store', 'children')], [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return layouts.home, dash.no_update
    elif pathname.startswith('/groupchat/') or pathname.startswith('/personalchat/'):
        chat_type, url_key = pathname[1:].split('/')
        page_content = layouts.groupchat if chat_type == 'groupchat' else None
        container_data_store = dash.no_update
        if pathname.endswith(FROM_LANDING_PAGE):
            container_data_store = dash.no_update
        else:
            url, datasets = chat_parser.load_parsed_data(url_key, 'url')
            container_data_store = dcc.Store(id='data-store', data=datasets)
            if url == 'not_found':
                page_content = layouts.not_found
                container_data_store = dash.no_update
        return page_content, container_data_store
    else:
        return layouts.page_404, dash.no_update

@app.callback(
    [Output('url', 'pathname'), Output('data-store', 'data')],
    [Input('upload-data', 'contents'), Input('url-submit', 'n_clicks')],
    [State('save-switch', 'on'), State('url-input', 'value')])
def upload_data(contents, n_click, save, url_input):
    ctx = dash.callback_context
    url, datasets = dash.no_update, dash.no_update
    if ctx.triggered[0]['prop_id'] == 'upload-data.contents':
        content_type, content = contents.split(',')
        if content_type == 'data:text/plain;base64':
            content_decoded = base64.b64decode(content)
            url, datasets = chat_parser.load_parsed_data(content_decoded, 'upload', save)
            url = url + FROM_LANDING_PAGE
            # TODO: add alert message, wrong file type, please upload txt file
    elif ctx.triggered[0]['prop_id'] == 'url-submit.n_clicks':
        url, datasets = chat_parser.load_parsed_data(url_input, 'url')
        if url != 'not_found':
            url = url + FROM_LANDING_PAGE
    return url, datasets

@app.callback(
    [Output('dropdown_users', 'options'), Output('navbar-brand', 'children'), Output('created-by', 'children'), Output('user-count', 'children')],
    [Input('dropdown_users', 'value')], [State('data-store', 'data')])
def fill_dropdown_users(dropdown_users, datasets):
    datasets = json.loads(datasets)
    output = [
        [{'label': i, 'value': i} for i in datasets['users']],
        datasets['chat_name'],
        datasets['chat_created_by'],
        len(datasets['users'])
    ]
    return output

@app.callback(Output('selectall_users_container', 'children'), [Input('dropdown_users', 'value')], [State('selectall_users', 'value')])
def update_selectall_users(dropdown_users, select_all):
    if len(dropdown_users) > 0 and select_all == [1]:
        select_all_container = dcc.Checklist(id='selectall_users', options=[{'label': 'Select All', 'value': 1}], value=[])
    elif len(dropdown_users) == 0 and select_all == []:
        select_all_container = dcc.Checklist(id='selectall_users', options=[{'label': 'Select All', 'value': 1}], value=[1])
    else:
        select_all_container = dash.no_update
    return select_all_container

@app.callback(Output('dropdown_users_container', 'children'), [Input('selectall_users', 'value')], [State('dropdown_users', 'value')])
def update_dropdown_users(select_all, dropdown_users):
    if select_all == [1] and len(dropdown_users) > 0:
        return dcc.Dropdown(id='dropdown_users', options=[], multi=True, value=[])
    else:
        return dash.no_update

@app.callback(
    [Output('counter', 'children'), Output('message-count', 'children'), Output('word-count', 'children'), Output('media-count', 'children'), Output('emoji-count', 'children'), Output('location-count', 'children'), Output('link-count', 'children'), Output('deleted-count', 'children'), Output('left-count', 'children'),
     Output('chart-1', 'figure'), Output('chart-2', 'figure'), Output('chart-3', 'figure'), Output('chart-4', 'figure')],
    [Input('dropdown_users', 'value'), Input('time-interval', 'value')],
    [State('data-store', 'data')])
def update_filter(dropdown_users, interval, datasets):
    df = pd.read_json(json.loads(datasets)['data'], orient='split')
    filtered_df = df[((df.contact.isin(dropdown_users)) | (len(dropdown_users) == 0))]
    output = [
        filtered_df.groupby('day').size(),
        filtered_df[filtered_df.category != 'Event'].shape[0],
        filtered_df['count_words'].sum(),
        filtered_df[filtered_df.category == 'Media'].shape[0],
        filtered_df['count_emoji'].sum(),
        filtered_df[filtered_df.category == 'Location'].shape[0],
        filtered_df['count_link'].sum(),
        filtered_df[filtered_df.category == 'Deleted'].shape[0],
        filtered_df[(filtered_df.category == 'Event') & (filtered_df.event_type == 'left')].shape[0],
        charts.chart1(filtered_df, interval),
        charts.chart2(filtered_df),
        charts.chart3(filtered_df),
        charts.chart4(filtered_df)]
    return output

if __name__ == "__main__":
    app.run_server(debug=True)
