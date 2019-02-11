#https://www.youtube.com/watch?v=wv2MXJIdKRY

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
from dash.dependencies import Input, Output
import datetime

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1('Dash-tutorials, part 3'),
    html.Div(children='''
        symbol to graph:
    '''),
    dcc.Input(id='input', value = '', type= 'text'),
    html.Div(id='output_graph')
    ])
@app.callback(
        Output(component_id='output_graph', component_property='children'),
        [Input(component_id='input', component_property='value')]
        )

def update_graph(input_data):

    start = datetime.datetime(2015,1,1)
    end = datetime.datetime.now()
    #stock = 'LOCAL.PA'

    df = web.DataReader(input_data,'yahoo', start, end)
    
    return dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x':df.index, 'y':df.Close, 'type': 'line', 'name': input_data},
                ],
                'layout': {
                    'title': input_data
                }
            }
        )


if __name__ == '__main__':
    app.run_server(debug=True)

