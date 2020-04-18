import dash
from dash.dependencies import Output, Input, State
import dash_core_components as dcc
import dash_html_components as html
from src.app import app
from src import layouts
from src import chat_parser
from src import callbacks

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content',
        style={
            'padding': '20px'
        }),
    html.Div(id='container-data-store', style={'display': 'none'}, children=[
        html.Div(id='data-store', style={'display': 'none'})])
])

@app.callback([Output('page-content', 'children'), Output('container-data-store', 'children')], [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return layouts.home, dash.no_update
    elif pathname.startswith('/groupchat/') or pathname.startswith('/personalchat/'):
        chat_type, url_key = pathname[1:].split('/')
        page_content = layouts.groupchat if chat_type == 'groupchat' else None
        container_data_store = dash.no_update
        if pathname.endswith(callbacks.FROM_LANDING_PAGE):
            container_data_store = dash.no_update
        else:
            url, datasets = chat_parser.load_parsed_data(url_key, 'url')
            container_data_store = html.Div(id='data-store', style={'display': 'none'}, children=datasets)
            if url == 'not_found':
                page_content = layouts.not_found
                container_data_store = dash.no_update
        return page_content, container_data_store
    else:
        return layouts.page_404, dash.no_update

if __name__ == "__main__":
    app.run_server(debug=True)