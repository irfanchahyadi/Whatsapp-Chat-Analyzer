import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import dash_bootstrap_components as dbc

LOGO = '/assets/logo.png'

home = html.Div([
    html.H1('Landing Page'),
    dcc.Link('DEMO', href='/groupchat/DEMO'),
    dbc.Card(
        dbc.CardBody([
            html.H5('Show your saved chat'),
            html.Div(className='input-group',
                children=[
                    dcc.Input(id='url-input',
                        placeholder='Enter your last url key',
                        type='text',
                        maxLength=10,
                        value='',
                        className='form-control'),
                    html.Button(id='url-submit', children='Submit', className='btn btn-primary')])])),
    dbc.Card(
        dbc.CardBody([
            html.H5('Upload and Analyze your chat'),
            dbc.Col([
                dbc.Row([
                    html.Div([
                        'Save: ',
                        daq.BooleanSwitch(id='save-switch', on=True, color='#29b6f6', style={'display': 'inline-block', 'margin-right': '10px'})])],
                    style={'display': 'block', 'text-align': 'end'}),
                html.Div(
                    dcc.Upload(id='upload-data', children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
                        style={
                            'width': '100%',
                            'height': '200px',
                            'lineHeight': '200px',
                            'borderWidth': '3px',
                            'borderStyle': 'dashed',
                            'borderRadius': '10px',
                            'textAlign': 'center'},
                        multiple=False))])])),
    dbc.Alert('hello world', duration=1000, fade=True, style={'position': 'fixed', 'width': '100%', 'top': '0px', 'left': '0px'}),
])

groupchat = html.Div([
    html.Header([
        dbc.Navbar([
            dbc.Row([
                html.A(
                    dbc.Col(html.Img(src=LOGO, height="30px")), href='/'),
                dbc.Col(dbc.NavbarBrand(id='navbar-brand', className='ml-2'), style={'margin-left': '10px'})],
                align='center',
                no_gutters=True),
            dbc.NavbarToggler(id="navbar-toggler")],
        color='dark',
        fixed='top',
        style={'height': '50px'})]),


    dbc.Card(
        dbc.CardBody([
            html.H3('General Information', className='card-title'),
            dbc.Col([
                dbc.Row([
                    dbc.Card([dbc.CardHeader(html.H6('Created by'))]),
                    dbc.Card([dbc.CardHeader(html.H6('Users'))]),
                    dbc.Card([dbc.CardHeader(html.H6('Messages'))]),
                    dbc.Card([dbc.CardHeader(html.H6('Words'))]),
                    dbc.Card([dbc.CardHeader(html.H6('Media'))]),
                    dbc.Card([dbc.CardHeader(html.H6('Emoji'))]),
                ], justify='around'),
                dbc.Row([
                    dbc.Card([dbc.CardHeader(html.H6('Contact'))]),
                    dbc.Card([dbc.CardHeader(html.H6('Location'))]),
                    dbc.Card([dbc.CardHeader(html.H6('Link'))]),
                    dbc.Card([dbc.CardHeader(html.H6('Event'))]),
                    dbc.Card([dbc.CardHeader(html.H6('Deleted'))]),
                    dbc.Card([dbc.CardHeader(html.H6('Left'))]),
                ], justify='around')
            ])
            ])),
    dbc.Row([
        dbc.Col(
            html.Div(id='selectall_users_container', children=[
                dcc.Checklist(id='selectall_users', options=[{'label': 'Select All', 'value': 1}], value=[1])]), className='col-md-1'),
        dbc.Col(
            html.Div(id='dropdown_users_container', children=[
                dcc.Dropdown(id='dropdown_users', options=[], multi=True, value=[])]), className='col-md-11')], align='center'),

    dbc.Card(
        dbc.CardBody([
            dbc.CardHeader(html.H4('Time Series Chat')),
            dcc.RadioItems(id='time-interval',
                options=[
                    {'label': 'Yearly  ', 'value': 'year'},
                    {'label': 'Monthly  ', 'value': 'month'},
                    {'label': 'Weekly  ', 'value': 'week'},
                    {'label': 'Daily  ', 'value': 'date'}],
                value='date',
                inputStyle={'margin-left': '7px'}),
            dcc.Graph(id='chart-1', figure={})])),
    dbc.Card(
        dbc.CardBody([
            dbc.CardHeader(html.H4('Chat Activity by Day & Hour')),
            dbc.Row([
                dcc.Graph(id='chart-2', figure={}, className='col-md-4'),
                dbc.Col([
                    dcc.Graph(id='chart-3', figure={}),
                    dcc.Graph(id='chart-4', figure={})], md=8)])])),
    html.Div(id='counter')
])

not_found = 'sory not found'

page_404 = html.Div([
    'Are you lost ?',
    html.Br(),
    html.A('Here', href='/'),
    ' a link to guide you home'
])