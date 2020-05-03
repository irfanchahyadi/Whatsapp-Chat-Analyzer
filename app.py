import base64, json
from datetime import datetime, date
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from src import charts, chat_parser, layouts, settings

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, settings.FONT_AWESOME])
server = app.server
app.config.suppress_callback_exceptions = True

app.title = 'Whatsapp Chat Analyzer'
app.layout = layouts.base

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

@app.callback([Output('date-picker', 'min_date_allowed'), Output('date-picker', 'max_date_allowed')], [Input('date-picker', 'id')], [State('data-store', 'data')])
def update_date_picker(id_date_picker, datasets):
    datasets = json.loads(datasets)
    return datasets['chat_min_date'], datasets['chat_max_date']

@app.callback(
    [Output('help-' + key, 'style') for key in settings.TOOLTIPS] +
    [Output('tt-' + key, 'style') for key in settings.TOOLTIPS] +
    [Output('tt-' + key, 'hide_arrow') for key in settings.TOOLTIPS],
    [Input('help-switch', 'on')])
def update_help_switch(show):
    visibility = 'visible' if show else 'hidden'
    output = [{'visibility': visibility}] * len(settings.TOOLTIPS) * 2 + [not show] * len(settings.TOOLTIPS)
    return output


@app.callback(
    [Output('counter', 'children'), Output('count-message', 'children'), Output('count-word', 'children'), Output('count-emoji', 'children'), Output('count-mention', 'children'),
     Output('count-media', 'children'), Output('count-location', 'children'), Output('count-link', 'children'), Output('count-contact', 'children'),
     Output('chart-1', 'figure'), Output('chart-2', 'figure'), Output('chart-3', 'figure'),
     Output('avg-user', 'children'), Output('avg-message', 'children'), Output('avg-day', 'children'), Output('avg-month', 'children'),
     Output('most-busy', 'children'), Output('most-active', 'children'), Output('most-silent', 'children'), Output('most-typer', 'children'),
     Output('most-emoji', 'children'), Output('most-media', 'children'), Output('most-location', 'children'), Output('most-link', 'children'),
     Output('most-contact', 'children'), Output('most-mention', 'children'), Output('most-add', 'children'), Output('most-deleted', 'children'),
     Output('chart-4', 'figure'), Output('chart-5', 'figure'), Output('chart-6', 'figure')],
    [Input('dropdown-users', 'value'), Input('date-picker', 'start_date'), Input('date-picker', 'end_date'), Input('time-interval1', 'value'), Input('time-interval2', 'value')],
    [State('data-store', 'data')])
def update_filter(dropdown_users, start_date_str, end_date_str, interval1, interval2, datasets):
    datasets = json.loads(datasets)
    df = pd.read_json(datasets['data'], orient='split')
    start_date = date.min if start_date_str is None else datetime.strptime(start_date_str, '%Y-%m-%d').date()
    end_date = date.max if end_date_str is None else datetime.strptime(end_date_str, '%Y-%m-%d').date()
    filtered_df = df[
        ((df.contact.isin(dropdown_users)) | (len(dropdown_users) == 0)) &
        (df.datetime.dt.date >= start_date) & (df.datetime.dt.date <= end_date)
    ]
    output = [dash.no_update] * 31
    ctx = dash.callback_context
    if ctx.triggered[0]['prop_id'] == 'time-interval1.value':
        output[9] = charts.chart1(filtered_df, interval1)
    elif ctx.triggered[0]['prop_id'] == 'time-interval2.value':
        output[28] = charts.chart4(filtered_df, interval2, 5)
    else:
        by_category = filtered_df[['contact', 'category']].pivot_table(index='contact', columns='category', aggfunc=len, fill_value=0).reindex(columns=settings.CATEGORIES, fill_value=0)
        by_column = filtered_df.groupby('contact').sum(numeric_only=True)
        output = [
            ctx.triggered[0]['prop_id'],
            '{:,} sent, {:,} deleted'.format(by_category.sum().sum() - by_category['Event'].sum(), by_category['Deleted'].sum()),
            '{:,} sent'.format(by_column['count_words'].sum()),
            '{:,} sent'.format(by_column['count_emoji'].sum()),
            '{:,} sent'.format(by_column['count_mention'].sum()),
            '{:,} shared'.format(by_category['Media'].sum()),
            '{:,} shared'.format(by_category['Location'].sum()),
            '{:,} shared'.format(by_column['count_link'].sum()),
            '{:,} shared'.format(by_category['Contact'].sum()),
            charts.chart1(filtered_df, interval1),
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
            charts.chart4(filtered_df, interval2, 5),
            charts.chart5(filtered_df, 5),
            charts.chart6(filtered_df, 10)
        ]
    return output

if __name__ == "__main__":
    app.run_server(debug=True)
