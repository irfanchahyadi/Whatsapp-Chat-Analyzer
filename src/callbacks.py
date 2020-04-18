import json
import base64
import pandas as pd
import dash
import dash_core_components as dcc
from dash.dependencies import Output, Input, State
from src.app import app
from src import chat_parser
from src import charts

FROM_LANDING_PAGE = '?from=landing_page'

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

@app.callback(Output('dropdown_users', 'options'), [Input('dropdown_users', 'value')], [State('data-store', 'data')])
def fill_dropdown_users(dropdown_users, datasets):
    users = json.loads(datasets)['users']
    dropdown_users_options = [{'label': i, 'value': i} for i in users]
    return dropdown_users_options

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
    [Output('counter', 'children'), Output('chart-1', 'figure'), Output('chart-2', 'figure'), Output('chart-3', 'figure'), Output('chart-4', 'figure')],
    [Input('dropdown_users', 'value'), Input('time-interval', 'value')], 
    [State('data-store', 'data')])
def update_filter(dropdown_users, interval, datasets):
    df = pd.read_json(json.loads(datasets)['data'], orient='split')
    filtered_df = df[((df.contact.isin(dropdown_users)) | (len(dropdown_users) == 0))]
    return filtered_df.groupby('day').size(), charts.chart1(filtered_df, interval), charts.chart2(filtered_df), charts.chart3(filtered_df), charts.chart4(filtered_df)