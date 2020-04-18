import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import dash_bootstrap_components as dbc

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
                        daq.BooleanSwitch(id='save-switch', on=True, style={'display': 'inline-block', 'margin-right': '10px'})])],
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
    html.H1('Page Visualize'),
    html.A('home', href='/'),
    html.Div(
        children=[
            html.Div(id='selectall_users_container', children=[
                dcc.Checklist(id='selectall_users', options=[{'label': 'Select All', 'value': 1}], value=[1])]),
            html.Div(id='dropdown_users_container', children=[
                dcc.Dropdown(id='dropdown_users', options=[], multi=True, value=[])])],
        style={}),
    
    html.Div(
        dbc.Card(
            dbc.CardBody([
                html.H3('Time Series Chat', className='card-title'),
                dcc.RadioItems(id='time-interval',
                    options=[
                        {'label': 'Yearly  ', 'value': 'year'},
                        {'label': 'Monthly  ', 'value': 'month'},
                        {'label': 'Weekly  ', 'value': 'week'},
                        {'label': 'Daily  ', 'value': 'date'}],
                    value='date',
                    inputStyle={'margin-left': '7px'}),
                dcc.Graph(id='chart-1', figure={})]))),
    html.Div(
        dbc.Card(
            dbc.CardBody([
                html.H3('Chat Activity by Day & Hour', className='card-title'),
                dbc.Row([
                    dcc.Graph(id='chart-2', figure={}, className='col-md-4'),
                    dbc.Col([
                        dcc.Graph(id='chart-3', figure={}),
                        dcc.Graph(id='chart-4', figure={})], md=8)])]))),
    html.Div(id='counter')
])

not_found = 'sory not found'

page_404 = html.Div([
    'Are you lost ?',
    html.Br(),
    html.A('Here', href='/'),
    ' a link to guide you home'
])