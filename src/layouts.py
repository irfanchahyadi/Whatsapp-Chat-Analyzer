import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import dash_bootstrap_components as dbc
from src import settings

base = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    dcc.Loading(type='graph', fullscreen=True, children=[
        html.Div(id='container-data-store', style={'display': 'none'}, children=[
            dcc.Store(id='data-store')])])
])


def add_help(inside, tooltip_id=None, hide=True):
    style = {'display': 'inline-block', 'margin-right': '5px'}
    visibility = 'hidden' if hide else 'visible'
    try:
        inside.style
    except AttributeError:
        inside.style = {}
    inside.style.update(style)
    result = html.Span([
        inside,
        html.I(className='fas fa-question-circle fa-sm text-muted', id='help-' + tooltip_id, style={'visibility': visibility}),
        dbc.Tooltip(settings.TOOLTIPS[tooltip_id], id='tt-' + tooltip_id, target='help-' + tooltip_id, hide_arrow=hide, style={'visibility': visibility, 'z-index': 9999})
    ])
    return result

home = html.Div([
    html.H1(settings.APP_NAME),
    dcc.Link('DEMO', href='/groupchat/DEMO'),
    html.I(className='fas fa-question-circle fa-lg'),
    dbc.Card(
        dbc.CardBody([
            html.H5('Show your saved chat'),
            html.Div(className='input-group',
                children=[
                    dcc.Input(id='url-input',
                        placeholder='Enter your last url key',
                        type='text',
                        maxLength=10,
                        autoFocus=True,
                        debounce=True,
                        className='form-control'),
                    html.Button(id='url-submit', children='Submit', className='btn btn-primary')])])),
    dbc.Card(
        dbc.CardBody([
            html.H5('Upload and Analyze your chat'),
            dbc.Col([
                dbc.Row([
                    html.Div([
                        add_help(html.Div('Save '), 'save', hide=False),
                        html.Div(':', style={'margin-right': '10px'}),
                        daq.BooleanSwitch(id='save-switch', on=False, color='#29b6f6', disabled=True)], style={'display': 'flex', 'margin-left': 'auto', 'margin-right': '0px', 'align-items': 'center'})], style={'margin-bottom': '5px'}),
                html.Div(
                    dcc.Upload(id='upload-data', children=html.Div(['Drag and Drop or ', html.A('Select Files')]), multiple=False, className='upload-file')),
                html.Div(id='alert-container')
            ])]))
])


groupchat = html.Div([
    html.Header([
        dbc.Navbar([
            dbc.Row([
                html.A(
                    dbc.Col(html.Img(src=settings.LOGO, height="45px")), href='/'),
                dbc.Col(dbc.NavbarBrand(id='navbar-brand', className='ml-2'), style={'margin-left': '10px'})],
                align='center', no_gutters=True)], fixed='top', className='wa-navbar')]),

    dbc.Col([
        dbc.Row([
            dbc.Card([dbc.CardHeader(add_help(html.H6('Created by'), 'created')), html.Div(id='created-by')], className='col-md-3'),
            dbc.Card([dbc.CardHeader(add_help(html.H6('Messages'), 'messages')), html.Div(id='count-message')], className='col-md'),
            dbc.Card([dbc.CardHeader(add_help(html.H6('Words'), 'words')), html.Div(id='count-word')], className='col-md'),
            dbc.Card([dbc.CardHeader(add_help(html.H6('Emoji'), 'emoji')), html.Div(id='count-emoji')], className='col-md'),
            dbc.Card([dbc.CardHeader(add_help(html.H6('Mentions'), 'mention')), html.Div(id='count-mention')], className='col-md')], justify='around'),
        dbc.Row([
            dbc.Card([dbc.CardHeader(add_help(html.H6('Media'), 'media')), html.Div(id='count-media')], className='col-md'),
            dbc.Card([dbc.CardHeader(add_help(html.H6('Location'), 'location')), html.Div(id='count-location')], className='col-md'),
            dbc.Card([dbc.CardHeader(add_help(html.H6('Link'), 'link')), html.Div(id='count-link')], className='col-md'),
            dbc.Card([dbc.CardHeader(add_help(html.H6('Contact'), 'contact')), html.Div(id='count-contact')], className='col-md'),
            dbc.Card([dbc.CardHeader(add_help(html.H6('Users'), 'users')), html.Div(id='count-user')], className='col-md-3')], justify='around', style={'margin-top': '-10px'})]),

    dbc.Card(
        dbc.Col([
            dbc.Row([
                html.Div('Filter User :', style={'padding-left': '0px', 'margin-right': '10px'}),
                dbc.Col(
                    dcc.Dropdown(id='dropdown-users', options=[], multi=True, value=[]))], align='center'),
            dbc.Row([
                html.Div('Filter Date :', style={'padding-left': '0px', 'margin-right': '10px'}),
                dcc.DatePickerRange(id='date-picker', display_format='DD/MM/YYYY', clearable=True),
                html.Div(['Show help :', daq.BooleanSwitch(id='help-switch', on=False, color='#29b6f6', style={'margin-left': '10px'})], style={'margin-left': 'auto', 'margin-right': '0px', 'display': 'inherit'})
                ], align='center', style={'margin-top': '5px'})
            ]), className='card-filter'),

    dbc.Card(
        dbc.CardBody([
            dbc.CardHeader(add_help(html.H5('Time Series Chat'), 'time-series')),
            dcc.RadioItems(id='time-interval1',
                options=[
                    {'label': 'Yearly', 'value': 'year'},
                    {'label': 'Monthly', 'value': 'month'},
                    {'label': 'Weekly', 'value': 'week'},
                    {'label': 'Daily', 'value': 'date'}],
                value='date', inputStyle={'margin-left': '7px', 'margin-right': '2px'}),
            dcc.Graph(id='chart-1', figure={})])),

    dbc.Row([
        dbc.Card(
            dbc.CardBody([
                dbc.CardHeader(add_help(html.H5('Daily Chat Activity'), 'daily-activity')),
                    dcc.Graph(id='chart-2', figure={})]), className='col-md-4'),
        dbc.Card(
            dbc.CardBody([
                dbc.CardHeader(add_help(html.H5('Chat Activity by Hour'), 'hourly-activity')),
                dcc.Graph(id='chart-3', figure={})]), className='col-md')]),

    dbc.Card(dbc.CardHeader(html.H5('Averages'), className='single-header')),
        dbc.Row([
            dbc.Card([dbc.CardHeader(add_help(html.H6('Per User'), 'per-user')), html.Div(id='avg-user')], className='col-md'),
            dbc.Card([dbc.CardHeader(add_help(html.H6('Per Text Message'), 'per-text')), html.Div(id='avg-message')], className='col-md'),
            dbc.Card([dbc.CardHeader(add_help(html.H6('Per Day'), 'per-day')), html.Div(id='avg-day')], className='col-md'),
            dbc.Card([dbc.CardHeader(add_help(html.H6('Per Month'), 'per-month')), html.Div(id='avg-month')], className='col-md')], justify='around', style={'margin-top': '-10px'}),

    dbc.Card(dbc.CardHeader(html.H5('Awards'), className='single-header')),
    dbc.Col([
        dbc.Row([
            dbc.Card([dbc.CardHeader(add_help(html.H6('Busy Days'), 'busy-day')), html.Div(id='most-busy')], className='col-md'),
            dbc.Card([dbc.CardHeader(add_help(html.H6('Talk Active'), 'talk-active')), html.Div(id='most-active')], className='col-md'),
            dbc.Card([dbc.CardHeader(add_help(html.H6('Silent Reader'), 'silent-reader')), html.Div(id='most-silent')], className='col-md'),
            dbc.Card([dbc.CardHeader(add_help(html.H6('Long Typer'), 'long-typer')), html.Div(id='most-typer')], className='col-md')], justify='around', style={'margin-top': '-10px'}),
        dbc.Row([
            dbc.Card([dbc.CardHeader(add_help(html.H6('Emoji Fan'), 'emoji-fan')), html.Div(id='most-emoji')], className='col-md'),
            dbc.Card([dbc.CardHeader(add_help(html.H6('Media Lover'), 'media-lover')), html.Div(id='most-media')], className='col-md'),
            dbc.Card([dbc.CardHeader(add_help(html.H6('Location Reporter'), 'location-reporter')), html.Div(id='most-location')], className='col-md'),
            dbc.Card([dbc.CardHeader(add_help(html.H6('Link Sharer'), 'link-sharer')), html.Div(id='most-link')], className='col-md')], justify='around', style={'margin-top': '-10px'}),
        dbc.Row([
            dbc.Card([dbc.CardHeader(add_help(html.H6('Contact Sharer'), 'contact-sharer')), html.Div(id='most-contact')], className='col-md'),
            dbc.Card([dbc.CardHeader(add_help(html.H6('Mentioner'), 'mentioner')), html.Div(id='most-mention')], className='col-md'),
            dbc.Card([dbc.CardHeader(add_help(html.H6('Recruiter'), 'recruiter')), html.Div(id='most-add')], className='col-md'),
            dbc.Card([dbc.CardHeader(add_help(html.H6('Inconstant'), 'inconstant')), html.Div(id='most-deleted')], className='col-md')], justify='around', style={'margin-top': '-10px'})]),

    dbc.Card(
        dbc.CardBody([
            dbc.CardHeader(add_help(html.H5('Top 5 Dominance'), 'dominance')),
            dcc.RadioItems(id='time-interval2',
                options=[
                    {'label': 'Yearly', 'value': 'year'},
                    {'label': 'Monthly', 'value': 'month'},
                    {'label': 'Weekly', 'value': 'week'},
                    {'label': 'Daily', 'value': 'date'}],
                value='date', inputStyle={'margin-left': '7px', 'margin-right': '2px'}),
            dcc.Graph(id='chart-4', figure={})])),

    dbc.Row([
        dbc.Card(
            dbc.CardBody([
                dbc.CardHeader(add_help(html.H5('Top 5 Breakdown by Content'), 'breakdown-content')),
                    dcc.Graph(id='chart-5', figure={})]), className='col-md-8'),
        dbc.Card(
            dbc.CardBody([
                dbc.CardHeader(html.H5('Top 10 Emoji Used')),
                dcc.Graph(id='chart-6', figure={})
                ]), className='col-md')]),

    html.Div(id='counter')
])

not_found = 'sory not found'

page_404 = html.Div([
    'Are you lost ?',
    html.Br(),
    html.A('Here', href='/'),
    ' a link to guide you home'
])


def award_list(series, n=3):
    trophy_emoji = '\U0001F3C6'
    list_row = []
    for i, (j, k) in enumerate(series.head(n).iteritems()):
        if k > 0:
            row = html.Tr([
                html.Td(f'{i+1}.'),
                html.Td(j if isinstance(j, str) else j.strftime('%d %B %Y'), className='td-content'),
                html.Td('{:,}'.format(k), className='td-value'),
                html.Td(trophy_emoji if i == 0 else '')])
            list_row.append(row)
    if len(list_row) > 0:
        table = html.Table(list_row)
    else:
        table = 'No data found'
    return table