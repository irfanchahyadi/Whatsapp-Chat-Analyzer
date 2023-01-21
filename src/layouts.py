from dash import dcc
from dash import html
import dash_daq as daq
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
from src import settings

base = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    dcc.Loading(type='graph', fullscreen=True, children=[
        html.Div(id='container-data-store', style={'display': 'none'}, children=[
            dcc.Store(id='data-store')])])
])


def add_help(inside, tooltip_id=None, hide=True):
    """Wrapper html tag to display help tooltips."""
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
        dbc.Tooltip(settings.TOOLTIPS[tooltip_id], id='tt-' + tooltip_id, target='help-' + tooltip_id, style={'visibility': visibility, 'z-index': 9999})
    ])
    return result

footer = html.Div([
    dbc.Col(html.A(settings.COPYRIGHT, href=settings.COPYRIGHT_URL, target='_blank', style={'color': '#fff', 'font-weight': '400'}), style={'text-align': 'left'}),
    dbc.Col([
        html.A('Disclaimer', href=settings.DISCLAIMER_URL, target='_blank'),
        ' | ',
        html.A('Source Code', href=settings.SOURCE_CODE_URL, target='_blank')], style={'text-align': 'center'}),
    dbc.Col([
        html.A(html.I(className='fas fa-at'), href=settings.CONTACT_EMAIL, target='_blank'),
        html.A(html.I(className='fab fa-github'), href=settings.CONTACT_GITHUB, target='_blank'),
        html.A(html.I(className='fab fa-linkedin-in'), href=settings.CONTACT_LINKEDIN, target='_blank')
    ], style={'text-align': 'right'})
], className='home-footer')

home = html.Div([
    html.Div([
        html.A(html.Img(src=settings.LOGO, height="60px"), href='/'),
        html.H1(settings.APP_NAME)], className='home-header'),
    html.Div([
        dcc.Link('SHOW DEMO', href='/groupchat/DEMO', className='btn btn-wa', style={'margin-left': '10px'}),
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
                        html.Button(id='url-submit', children='Submit', className='btn btn-wa')])]),
            style={'display': 'none'}), # hidden, no need to show when save chat is disable
        dbc.Card(
            dbc.CardBody([
                dbc.Col([
                    html.H5('Upload and Analyze your chat'),
                    html.Div([
                        add_help(html.Div('Save '), 'save', hide=False),
                        html.Div(':', style={'margin-left': '5px', 'margin-right': '10px'}),
                        daq.BooleanSwitch(id='save-switch', on=False, color='#29b6f6', disabled=True)], style={'display': 'flex', 'margin-left': 'auto', 'margin-right': '0px', 'align-items': 'center'})
                ], style={'display': 'flex', 'margin-bottom': '5px'}),
                dbc.Col([
                    dcc.Upload(id='upload-data', children=html.Div(['Drag and Drop or ', html.A('Select Files')]), multiple=False, className='upload-file'),
                    html.Div(id='alert-container')
                ]),
                dbc.Col([
                    html.Table(
                        html.Tr([
                            html.Td(html.P('Notes:')),
                            html.Td([
                                html.P("We won't save your data unless you specify to Save (which is not currently available)"),
                                html.P('Due to heroku free plan performance, upload time may take a few minutes depend on file size. For comparison, 100kb file uploaded around 20 second and 1mb around 2 minutes.')])]))
                ], className='small-note'),
                dbc.Col([
                    html.H5('How to export chat history'),
                    html.Table([
                        html.Tr([html.Td('1. '), html.Td(['Select group chat on WhatsApp'])]),
                        html.Tr([html.Td('2. '), html.Td(['Click ', html.I(className='fas fa-ellipsis-v'), ' button > ', html.Strong('More')])]),
                        html.Tr([html.Td('3. '), html.Td(['Select ', html.Strong('Export chat'), ' > ', html.Strong('Without media')])]),
                        html.Tr([html.Td('4. '), html.Td(['Choose send chat via ', html.Strong('Gmail'), ' or ', html.Strong('Google Drive')])]),
                        html.Tr([html.Td('5. '), html.Td(['Download chat file (something like ', html.Strong("Chat WhatsApp with <chatname>.txt"), '), then upload it here'])])]),
                ], style={'margin-top': '20px'})
            ]), style={'margin-top': '20px'})], className='home'),
    html.Div(footer, style={'position': 'absolute', 'bottom': 0, 'width': '100%'})
])


groupchat = html.Div([
    html.Div([
        html.Header([
            dbc.Navbar([
                dbc.Row([
                    html.A(
                        dbc.Col(html.Img(src=settings.LOGO, height="45px")), href='/'),
                    dbc.Col(dbc.NavbarBrand(id='navbar-brand', className='ml-2'), style={'margin-left': '10px'})],
                    align='center')], fixed='top', className='wa-navbar')]),

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
                    dcc.DatePickerRange(id='date-picker', display_format='DD/MM/YYYY', clearable=True),
                    dbc.Col(
                        dcc.Dropdown(id='dropdown-users', placeholder='Filter user', options=[], multi=True, value=[]), style={'margin-left': '20px', 'margin-right': '20px'}),
                    html.Div(['Show help :', daq.BooleanSwitch(id='help-switch', on=False, color='#29b6f6', style={'margin-left': '5px'})], style={'margin-left': 'auto', 'margin-right': '0px', 'display': 'inherit'})
                ], align='center')
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
                dcc.Graph(id='chart-1')])),

        dbc.Row([
            dbc.Card(
                dbc.CardBody([
                    dbc.CardHeader(add_help(html.H5('Daily Chat Activity'), 'daily-activity')),
                        dcc.Graph(id='chart-2')]), className='col-md-4'),
            dbc.Card(
                dbc.CardBody([
                    dbc.CardHeader(add_help(html.H5('Chat Activity by Hour'), 'hourly-activity')),
                    dcc.Graph(id='chart-3')]), className='col-md')]),

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
                dbc.Card([dbc.CardHeader(add_help(html.H6('Inconstant'), 'inconstant')), html.Div(id='most-deleted')], className='col-md')], justify='around', style={'margin-top': '-10px'}),
            dbc.Row([
                dbc.Card([dbc.CardHeader(add_help(html.H6('Favorite Domain'), 'favorite-domain')), html.Div(id='most-domain')], className='col-md'),
                dbc.Card([dbc.CardHeader(html.H6('')), html.Div(id='most-')], className='col-md'),
                dbc.Card([dbc.CardHeader(html.H6('')), html.Div(id='most-')], className='col-md'),
                dbc.Card([dbc.CardHeader(html.H6('')), html.Div(id='most-')], className='col-md')], justify='around', style={'margin-top': '-10px'})]),

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
                dcc.Graph(id='chart-4')])),

        dbc.Row([
            dbc.Card(
                dbc.CardBody([
                    dbc.CardHeader(add_help(html.H5('Top 5 Breakdown by Content'), 'breakdown-content')),
                        dcc.Graph(id='chart-5')]), className='col-md-8'),
            dbc.Card(
                dbc.CardBody([
                    dbc.CardHeader(add_help(html.H5('Top 10 Emoji Used'), 'emoji-used')),
                    dcc.Graph(id='chart-6')
                    ]), className='col-md')]),

        dbc.Card(
            dbc.CardBody([
                dbc.CardHeader(add_help(html.H5('Word Cloud'), 'word-cloud')),
                html.Img(id='chart-7', style={'width': '100%'})])),

        dbc.Card(
            dbc.CardBody([
                dbc.CardHeader(add_help(html.H5('Recruitment Genealogy'), 'recruitment-genealogy')),
                cyto.Cytoscape(
                    id='chart-8',
                    layout={'name': 'breadthfirst', 'directed': True, 'spacingFactor': 1.5},
                    style={'width': '100%', 'height': f'{settings.CHART_HEIGHT}px'},
                    minZoom=0.2, maxZoom=3,
                    stylesheet=[
                        {'selector': 'node', 'style': {'label': 'data(id)'}},
                        {'selector': 'edge', 'style': {
                            'curve-style': 'bezier',
                            'target-arrow-color': '#1ebea5',
                            'target-arrow-shape': 'triangle',
                            'line-color': '#1ebea5'}}],
                    elements=[])]), style={'margin-top': '20px'}),

        html.Div(id='counter', style={'visibility': 'hidden'})], className='visualize'),

    html.Div(footer)
])

personalchat = html.Div([
    html.Div([
        html.Header([
            dbc.Navbar([
                dbc.Row([
                    html.A(
                        dbc.Col(html.Img(src=settings.LOGO, height="45px")), href='/'),
                    dbc.Col(dbc.NavbarBrand(id='navbar-brand2', className='ml-2'), style={'margin-left': '10px'})],
                    align='center')], fixed='top', className='wa-navbar')]),

        dbc.Col([
            dbc.Row([
                dbc.Card([dbc.CardHeader(add_help(html.H6('Created by'), 'created')), html.Div(id='created-by2')], className='col-md-3'),
                dbc.Card([dbc.CardHeader(add_help(html.H6('Messages'), 'messages')), html.Div(id='count-message2')], className='col-md'),
                dbc.Card([dbc.CardHeader(add_help(html.H6('Words'), 'words')), html.Div(id='count-word2')], className='col-md'),
                dbc.Card([dbc.CardHeader(add_help(html.H6('Emoji'), 'emoji')), html.Div(id='count-emoji2')], className='col-md'),
                dbc.Card([dbc.CardHeader(add_help(html.H6('Mentions'), 'mention')), html.Div(id='count-mention2')], className='col-md')], justify='around'),
            dbc.Row([
                dbc.Card([dbc.CardHeader(add_help(html.H6('Media'), 'media')), html.Div(id='count-media2')], className='col-md'),
                dbc.Card([dbc.CardHeader(add_help(html.H6('Location'), 'location')), html.Div(id='count-location2')], className='col-md'),
                dbc.Card([dbc.CardHeader(add_help(html.H6('Link'), 'link')), html.Div(id='count-link2')], className='col-md'),
                dbc.Card([dbc.CardHeader(add_help(html.H6('Contact'), 'contact')), html.Div(id='count-contact2')], className='col-md'),
                dbc.Card([dbc.CardHeader(add_help(html.H6('Users'), 'users')), html.Div(id='count-user2')], className='col-md-3')], justify='around', style={'margin-top': '-10px'})]),

        dbc.Card(
            dbc.Col([
                dbc.Row([
                    dcc.DatePickerRange(id='date-picker2', display_format='DD/MM/YYYY', clearable=True),
                    dbc.Col(
                        dcc.Dropdown(id='dropdown-users2', placeholder='Filter user', options=[], multi=True, value=[]), style={'margin-left': '20px', 'margin-right': '20px'}),
                    html.Div(['Show help :', daq.BooleanSwitch(id='help-switch', on=False, color='#29b6f6', style={'margin-left': '5px'})], style={'margin-left': 'auto', 'margin-right': '0px', 'display': 'inherit'})
                ], align='center')
            ]), className='card-filter'),

        dbc.Card(
            dbc.CardBody([
                dbc.CardHeader(add_help(html.H5('Time Series Chat'), 'time-series')),
                dcc.RadioItems(id='time-interval1p',
                    options=[
                        {'label': 'Yearly', 'value': 'year'},
                        {'label': 'Monthly', 'value': 'month'},
                        {'label': 'Weekly', 'value': 'week'},
                        {'label': 'Daily', 'value': 'date'}],
                    value='date', inputStyle={'margin-left': '7px', 'margin-right': '2px'}),
                dcc.Graph(id='chart-1p')])),

        dbc.Row([
            dbc.Card(
                dbc.CardBody([
                    dbc.CardHeader(add_help(html.H5('Daily Chat Activity'), 'daily-activity')),
                        dcc.Graph(id='chart-2p')]), className='col-md-4'),
            dbc.Card(
                dbc.CardBody([
                    dbc.CardHeader(add_help(html.H5('Chat Activity by Hour'), 'hourly-activity')),
                    dcc.Graph(id='chart-3p')]), className='col-md')]),

        dbc.Card(dbc.CardHeader(html.H5('Averages'), className='single-header')),
            dbc.Row([
                dbc.Card([dbc.CardHeader(add_help(html.H6('Per User'), 'per-user')), html.Div(id='avg-user2')], className='col-md'),
                dbc.Card([dbc.CardHeader(add_help(html.H6('Per Text Message'), 'per-text')), html.Div(id='avg-message2')], className='col-md'),
                dbc.Card([dbc.CardHeader(add_help(html.H6('Per Day'), 'per-day')), html.Div(id='avg-day2')], className='col-md'),
                dbc.Card([dbc.CardHeader(add_help(html.H6('Per Month'), 'per-month')), html.Div(id='avg-month2')], className='col-md')], justify='around', style={'margin-top': '-10px'}),

        dbc.Card(dbc.CardHeader(html.H5('Awards'), className='single-header')),
        dbc.Col([
            dbc.Row([
                dbc.Card([dbc.CardHeader(add_help(html.H6('Busy Days'), 'busy-day')), html.Div(id='most-busy2')], className='col-md'),
                dbc.Card([dbc.CardHeader(add_help(html.H6('Talk Active'), 'talk-active')), html.Div(id='most-active2')], className='col-md'),
                dbc.Card([dbc.CardHeader(add_help(html.H6('Silent Reader'), 'silent-reader')), html.Div(id='most-silent2')], className='col-md'),
                dbc.Card([dbc.CardHeader(add_help(html.H6('Long Typer'), 'long-typer')), html.Div(id='most-typer2')], className='col-md')], justify='around', style={'margin-top': '-10px'}),
            dbc.Row([
                dbc.Card([dbc.CardHeader(add_help(html.H6('Emoji Fan'), 'emoji-fan')), html.Div(id='most-emoji2')], className='col-md'),
                dbc.Card([dbc.CardHeader(add_help(html.H6('Media Lover'), 'media-lover')), html.Div(id='most-media2')], className='col-md'),
                dbc.Card([dbc.CardHeader(add_help(html.H6('Location Reporter'), 'location-reporter')), html.Div(id='most-location2')], className='col-md'),
                dbc.Card([dbc.CardHeader(add_help(html.H6('Link Sharer'), 'link-sharer')), html.Div(id='most-link2')], className='col-md')], justify='around', style={'margin-top': '-10px'}),
            dbc.Row([
                dbc.Card([dbc.CardHeader(add_help(html.H6('Contact Sharer'), 'contact-sharer')), html.Div(id='most-contact2')], className='col-md'),
                dbc.Card([dbc.CardHeader(add_help(html.H6('Mentioner'), 'mentioner')), html.Div(id='most-mention2')], className='col-md'),
                dbc.Card([dbc.CardHeader(add_help(html.H6('Recruiter'), 'recruiter')), html.Div(id='most-add2')], className='col-md'),
                dbc.Card([dbc.CardHeader(add_help(html.H6('Inconstant'), 'inconstant')), html.Div(id='most-deleted2')], className='col-md')], justify='around', style={'margin-top': '-10px'}),
            dbc.Row([
                dbc.Card([dbc.CardHeader(add_help(html.H6('Favorite Domain'), 'favorite-domain')), html.Div(id='most-domain2')], className='col-md'),
                dbc.Card([dbc.CardHeader(html.H6('')), html.Div(id='most-')], className='col-md'),
                dbc.Card([dbc.CardHeader(html.H6('')), html.Div(id='most-')], className='col-md'),
                dbc.Card([dbc.CardHeader(html.H6('')), html.Div(id='most-')], className='col-md')], justify='around', style={'margin-top': '-10px'})]),

        dbc.Card(
            dbc.CardBody([
                dbc.CardHeader(add_help(html.H5('Top 5 Dominance'), 'dominance')),
                dcc.RadioItems(id='time-interval2p',
                    options=[
                        {'label': 'Yearly', 'value': 'year'},
                        {'label': 'Monthly', 'value': 'month'},
                        {'label': 'Weekly', 'value': 'week'},
                        {'label': 'Daily', 'value': 'date'}],
                    value='date', inputStyle={'margin-left': '7px', 'margin-right': '2px'}),
                dcc.Graph(id='chart-4p')])),

        dbc.Row([
            dbc.Card(
                dbc.CardBody([
                    dbc.CardHeader(add_help(html.H5('Top 5 Breakdown by Content'), 'breakdown-content')),
                        dcc.Graph(id='chart-5p')]), className='col-md-8'),
            dbc.Card(
                dbc.CardBody([
                    dbc.CardHeader(add_help(html.H5('Top 10 Emoji Used'), 'emoji-used')),
                    dcc.Graph(id='chart-6p')
                    ]), className='col-md')]),

        dbc.Card(
            dbc.CardBody([
                dbc.CardHeader(add_help(html.H5('Word Cloud'), 'word-cloud')),
                html.Img(id='chart-7p', style={'width': '100%'})])),

        dbc.Card(
            dbc.CardBody([
                dbc.CardHeader(add_help(html.H5('Recruitment Genealogy'), 'recruitment-genealogy')),
                cyto.Cytoscape(
                    id='chart-8p',
                    layout={'name': 'breadthfirst', 'directed': True, 'spacingFactor': 1.5},
                    style={'width': '100%', 'height': f'{settings.CHART_HEIGHT}px'},
                    minZoom=0.2, maxZoom=3,
                    stylesheet=[
                        {'selector': 'node', 'style': {'label': 'data(id)'}},
                        {'selector': 'edge', 'style': {
                            'curve-style': 'bezier',
                            'target-arrow-color': '#1ebea5',
                            'target-arrow-shape': 'triangle',
                            'line-color': '#1ebea5'}}],
                    elements=[])]), style={'margin-top': '20px'}),

        html.Div(id='counter', style={'visibility': 'hidden'})], className='visualize'),

    html.Div(footer)
])

not_found = 'sory not found'

page_404 = html.Div([
    'Are you lost ?',
    html.Br(),
    html.A('Here', href='/'),
    ' a link to guide you home'
])


def award_list(series, n=3):
    """Generate html table tag for award list."""
    trophy_emoji = '\U0001F3C6'
    list_row = []
    try:
        iterable = series.head(n).iteritems()
    except AttributeError:
        iterable = series.most_common(n)
    for i, (j, k) in enumerate(iterable):
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