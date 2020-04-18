import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq

home = html.Div([
    html.H1('Landing Page'),
    dcc.Link('visualize', href='/groupchat/asdf?abcd'),
    html.Div(className='input-group',
        children=[
            dcc.Input(id='url-input',
                placeholder='Enter your last url key',
                type='text',
                maxLength=10,
                value='',
                className='form-control'),
            html.Button(id='url-submit', children='Submit', className='btn btn-primary')]),
    html.Div(
        children=[
            'Save: ',
            daq.BooleanSwitch(id='save-switch', on=True,
                style={
                    'display': 'inline-block'})],
        style={
            'display': 'inline-block',
            'float': 'right'
        }),
    html.Div(
        dcc.Upload(id='upload-data', children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center'},
            multiple=False)),
])

groupchat = html.Div([
    html.H1('Page Visualize'),
    dcc.Link('home', href='/'),
    html.Div(
        children=[
            html.Div(id='selectall_users_container', children=[
                dcc.Checklist(id='selectall_users', options=[{'label': 'Select All', 'value': 1}], value=[1])]),
            html.Div(id='dropdown_users_container', children=[
                dcc.Dropdown(id='dropdown_users', options=[], multi=True, value=[])])],
        style={}),
    dcc.RadioItems(id='time-interval',
        options=[
            {'label': 'Yearly', 'value': 'year'},
            {'label': 'Monthly', 'value': 'month'},
            {'label': 'Weekly', 'value': 'week'},
            {'label': 'Daily', 'value': 'date'}],
        value='date'),
    dcc.Graph(id='chart-1', figure={}),
    dcc.Graph(id='chart-2', figure={}),
    dcc.Graph(id='chart-3', figure={}),
    dcc.Graph(id='chart-4', figure={}),
    html.Div(id='counter')
])

not_found = 'sory not found'

page_404 = html.Div([
    'Are you lost ?',
    html.Br(),
    html.A('Here', href='/'),
    ' a link to guide you home'
])