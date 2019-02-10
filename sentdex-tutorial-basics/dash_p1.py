#https://www.youtube.com/watch?v=J_Cy_QjG6NE

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1('Dash-tutorials'),
    dcc.Graph(id='example',
              figure= {
                  'data': [
                      {'x':[1,2,3],'y':[7,8,2],'type':'line','name':'boats'},
                      {'x':[1,5,3],'y':[7,2,9],'type':'bar','name':'cars'}],
                  'layout': {
                      'title': 'basic dash example'
                      }
                  })
              ])

if __name__ == '__main__':
    app.run_server(debug=True)


