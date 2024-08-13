import pandas as pd
from dash import Dash, html
import plotly.express as px
from dash import Dash, html, dcc, callback, Output, Input, dash_table,Input, Output
import pandas as pd
import dash_bootstrap_components as dbc
cldf = pd.read_csv('assets/AIT21_cl.df.csv')

app = Dash(__name__)
#app = Dash()


app.layout = html.Div([
    html.H1(children='HiGlass Multiome', style={'textAlign':'center'}),
    
# input-----------------------------------------------------------
    #first row
    html.Div( className = 'row',
        children=[
        
        html.Div(children=[ 

            
            #sunburst plot
            html.Div([ 
            dcc.Graph(id = 'sunburst',style={'width': '1000px','height':'1000px'}),
            ], style={'width': '33%','height':'1000px', 'display': 'inline-block','vertical-align': 'top'}),
            html.Button("clear selection", id="clear"),
            
            dbc.Container([
                dash_table.DataTable(
                    page_size=10,
                    style_table={'height': '400px','width':'33%', 'overflowY': 'auto'},

                    columns=[
                    {'name': 'Class', 'id': 'class_id_label', 'type': 'text'},
                    {'name': 'Subclass', 'id': 'subclass_id_label', 'type': 'text'},
                    {'name': 'Cluster', 'id': 'cluster_id_label', 'type': 'text'},
                    ],

                    data=cldf.to_dict('records'),
                    filter_action='native',
                    style_data={
                    'width': '100px', 'minWidth': '100px', 'maxWidth': '150px',
                    'overflow': 'hidden',
                    'textOverflow': 'ellipsis'},
                    id='tbl')   ,
                dbc.Alert(id='tbl_out')
                ])

            ],style={'display': 'inline-block',"width": "40%", 'vertical-align': 'top',  'margin-top': '3vw'}),
            html.Div(
                html.Iframe(
                    src="assets/higlass_test.html",
                    style={"height": "1500px",'width':'1067px'}
                    
                ),style={"height": "1067px",'display': 'inline-block','vertical-align': 'top'}
            )
            ]
            ),


           
            ]) #end app layout
            
#clear table
@app.callback(
    Output("cldf", "value"),
    Input("clear", "n_clicks"))
def clear(n_clicks):
    cldf = pd.read_csv('assets/AIT21_cl.df.csv')
    return(cldf)

#@callback(Output('tbl_out', 'children'), Input('tbl', 'active_cell'))
#def update_graphs(active_cell):
#    return str(active_cell) if active_cell else "Click the table"

@app.callback(
    Output('sunburst', 'figure'),
    Input("clear","n_clicks"),
)
def update_sunburst(clear):
    print(clear)
    #print(cldf.head())
    df = px.data.tips()
    fig = px.sunburst(cldf, path=['class_id_label', 'subclass_label','supertype_label'])
    return(fig)
    
    
if __name__ == '__main__':
    app.run(debug=True, port=8000)
