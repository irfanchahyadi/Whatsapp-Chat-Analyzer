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
                        'Save: ',
                        daq.BooleanSwitch(id='save-switch', on=True, color='#29b6f6', style={'display': 'inline-block', 'margin-right': '10px'})])],
                    style={'display': 'block', 'text-align': 'end'}),
                html.Div(
                    dcc.Upload(id='upload-data', children=html.Div(['Drag and Drop or ', html.A('Select Files')]), multiple=False, className='upload-file')),
                html.Div(id='alert-container')
            ])])),
])

groupchat = html.Div([
    html.Header([
        dbc.Navbar([
            dbc.Row([
                html.A(
                    dbc.Col(html.Img(src=LOGO, height="45px")), href='/'),
                dbc.Col(dbc.NavbarBrand(id='navbar-brand', className='ml-2'), style={'margin-left': '10px'})],
                align='center', no_gutters=True)], fixed='top', className='wa-navbar')]),

    dbc.Col([
        dbc.Row([
            dbc.Card([dbc.CardHeader([html.H6('Created by')]), html.Div(id='created-by')], className='col-md-3'),
            dbc.Card([dbc.CardHeader([html.H6('Messages')]), html.Div(id='count-message')], className='col-md'),
            dbc.Card([dbc.CardHeader(html.H6('Words')), html.Div(id='count-word')], className='col-md'),
            dbc.Card([dbc.CardHeader(html.H6('Emoji')), html.Div(id='count-emoji')], className='col-md'),
            dbc.Card([dbc.CardHeader(html.H6('Mentions')), html.Div(id='count-mention')], className='col-md')], justify='around'),
        dbc.Row([
            dbc.Card([dbc.CardHeader(html.H6('Media')), html.Div(id='count-media')], className='col-md'),
            dbc.Card([dbc.CardHeader([html.H6('Location')]), html.Div(id='count-location')], className='col-md'),
            dbc.Card([dbc.CardHeader(html.H6('Link')), html.Div(id='count-link')], className='col-md'),
            dbc.Card([dbc.CardHeader([html.H6('Contact')]), html.Div(id='count-contact')], className='col-md'),
            dbc.Card([dbc.CardHeader(html.H6('Users')), html.Div(id='count-user')], className='col-md-3')], justify='around', style={'margin-top': '-10px'})]),

    dbc.Card(
        dbc.Row([
            html.Div(id='selectall-users-container', children=[
                dcc.Checklist(id='selectall-users', options=[{'label': 'Select All', 'value': 1}], value=[1])], style={'margin-right': '10px', 'align-self': 'flex-end'}),
            dbc.Col(
                html.Div(id='dropdown-users-container', children=[
                    dcc.Dropdown(id='dropdown-users', options=[], multi=True, value=[])]))], align='center'), className='card-filter'),

    dbc.Card(
        dbc.CardBody([
            dbc.CardHeader(html.H5('Time Series Chat')),
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
                dbc.CardHeader(html.H5('Daily Chat Activity')),
                    dcc.Graph(id='chart-2', figure={})]), className='col-md-4'),
        dbc.Card(
            dbc.CardBody([
                dbc.CardHeader(html.H5('Chat Activity by Hour')),
                dcc.Graph(id='chart-3', figure={})]), className='col-md')]),

    dbc.Card(dbc.CardHeader(html.H5('Averages'), className='single-header')),
        dbc.Row([
            dbc.Card([dbc.CardHeader([html.H6('Per User')]), html.Div(id='avg-user')], className='col-md'),
            dbc.Card([dbc.CardHeader([html.H6('Per Text Message')]), html.Div(id='avg-message')], className='col-md'),
            dbc.Card([dbc.CardHeader(html.H6('Per Day')), html.Div(id='avg-day')], className='col-md'),
            dbc.Card([dbc.CardHeader(html.H6('Per Month')), html.Div(id='avg-month')], className='col-md')], justify='around', style={'margin-top': '-10px'}),

    dbc.Card(dbc.CardHeader(html.H5('Awards'), className='single-header')),
    dbc.Col([
        dbc.Row([
            dbc.Card([dbc.CardHeader([html.H6('Busy Days')]), html.Div(id='most-busy')], className='col-md'),
            dbc.Card([dbc.CardHeader([html.H6('Talk Active')]), html.Div(id='most-active')], className='col-md'),
            dbc.Card([dbc.CardHeader(html.H6('Silent Reader')), html.Div(id='most-silent')], className='col-md'),
            dbc.Card([dbc.CardHeader(html.H6('Long Typer')), html.Div(id='most-typer')], className='col-md')], justify='around', style={'margin-top': '-10px'}),
        dbc.Row([
            dbc.Card([dbc.CardHeader([html.H6('Emoji Fan')]), html.Div(id='most-emoji')], className='col-md'),
            dbc.Card([dbc.CardHeader([html.H6('Media Lover')]), html.Div(id='most-media')], className='col-md'),
            dbc.Card([dbc.CardHeader(html.H6('Location Reporter')), html.Div(id='most-location')], className='col-md'),
            dbc.Card([dbc.CardHeader(html.H6('Link Sharer')), html.Div(id='most-link')], className='col-md')], justify='around', style={'margin-top': '-10px'}),
        dbc.Row([
            dbc.Card([dbc.CardHeader([html.H6('Contact Sharer')]), html.Div(id='most-contact')], className='col-md'),
            dbc.Card([dbc.CardHeader([html.H6('Mentioner')]), html.Div(id='most-mention')], className='col-md'),
            dbc.Card([dbc.CardHeader(html.H6('Recruiter')), html.Div(id='most-add')], className='col-md'),
            dbc.Card([dbc.CardHeader(html.H6('Inconstant')), html.Div(id='most-deleted')], className='col-md')], justify='around', style={'margin-top': '-10px'})]),

    dbc.Card(
        dbc.CardBody([
            dbc.CardHeader(html.H5('Top 5 Dominance')),
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
                dbc.CardHeader(html.H5('Top 5 Breakdown by Content')),
                    dcc.Graph(id='chart-5', figure={})]), className='col-md-8'),
        dbc.Card(
            dbc.CardBody([
                dbc.CardHeader(html.H5('Donut Chart')),
                # dcc.Graph(id='chart-6', figure={})
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