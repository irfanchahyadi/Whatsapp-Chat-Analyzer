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
    html.Div(id='page-content'),
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
     Output('most-busy', 'children'), Output('most-active', 'children'), Output('most-silent', 'children'), Output('most-typer', 'children')],
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
        by_category = filtered_df.groupby('category').size()
        by_column = filtered_df.sum(numeric_only=True)
        output = [
            filtered_df.groupby('day').size(),
            '{:,} sent, {:,} deleted'.format(by_category.sum() - by_category.get('Event', default=0), by_category.get('Deleted', default=0)),
            '{:,} sent'.format(by_column['count_words']),
            '{:,} sent'.format(by_column['count_emoji']),
            '{:,} sent'.format(by_column['count_mention']),
            '{:,} shared'.format(by_category.get('Media', default=0)),
            '{:,} shared'.format(by_category.get('Location', default=0)),
            '{:,} shared'.format(by_column['count_link']),
            '{:,} shared'.format(by_category.get('Contact', default=0)),
            charts.chart1(filtered_df, interval),
            charts.chart2(filtered_df),
            charts.chart3(filtered_df),
            '{:,.2f} messages'.format((by_category.sum() - by_category.get('Event', default=0))/filtered_df.contact.nunique(dropna=True)),
            '{:,.2f} words, {:.2f} emoji'.format(by_column['count_words']/by_category.get('Text', default=0), by_column['count_emoji']/by_category.get('Text', default=0)),
            '{:,.2f} text, {:.2f} media'.format(by_category.get('Text', default=0)/filtered_df.date.nunique(), by_category.get('Media', default=0)/filtered_df.date.nunique()),
            '{:,.2f} text, {:.2f} media'.format(by_category.get('Text', default=0)/filtered_df.month.nunique(), by_category.get('Media', default=0)/filtered_df.month.nunique()),
            layouts.award_list(filtered_df.groupby('date').size().sort_values(ascending=False)),
            layouts.award_list(filtered_df[filtered_df.category != 'Event'].groupby('contact').size().sort_values(ascending=False)),
            layouts.award_list(filtered_df[filtered_df.category != 'Event'].groupby('contact').size().sort_values(ascending=True)),
            layouts.award_list(filtered_df[filtered_df.category == 'Text'].groupby('contact')['count_character'].sum().sort_values(ascending=False))
        ]
    return output

if __name__ == "__main__":
    app.run_server(debug=True)
