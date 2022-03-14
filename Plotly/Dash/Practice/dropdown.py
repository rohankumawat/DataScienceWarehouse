import pandas as pd
import plotly
import plotly.express as px
import dash
from dash import html, dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

#Read the csv file
df = pd.read_csv("data/Urban_Park_Ranger_Animal_Condition.csv")

#Starting the Layout
#Focus mainly on Dropdown in this file

app.layout = html.Div([
    html.Div([
        dcc.Graph(id='our_graph')
    ], className='nine columns'),

    html.Div([
        html.Br(),
        html.Div(id='output_data'),
        html.Br(),

        html.Label(['Choose Column: '], style={'font-weight': 'bold', "text-align": "center"}),

        dcc.Dropdown(id='my_dropdown',
            options=[
                {'label': 'Species', 'value': 'Animal Class'},
                {'label': 'Final Ranger Action', 'value': 'Final Ranger Action'},
                {'label': 'Age', 'value': 'Age', 'disabled':True},
                {'label': 'Animal Condition', 'value': 'Animal Condition'},
                {'label': 'Borough', 'value': 'Borough'},
                {'label': 'Species Status', 'value': 'Species Status'}
            ],
            optionHeight = 20,         #Height/Space between the options
            value = 'Borough',         #Dropdown value automatically selected when the page is refreshed
            disabled = False,          #disable the whole dropdown value selection || We definitely want False
            multi = False,             #Allow multiple dropdown selection (Multiple Choice Types)
            searchable = True,         #allows to actually type in and search the keyword
            search_value = '',         #remembers the value searched in the dropdown || Put an empty string here
            placeholder = 'Please select ', #gray, gray, default text shown when no option is selected
            clearable=True,                     #allow user to removes the selected value
            style={'width':"100%"},             #use dictionary to define CSS styles of your dropdown
            # className='select_box',           #activate separate CSS document in assets folder
            # persistence=True,                 #remembers dropdown value. It has to be Used with persistence_type
            # persistence_type='memory'         #remembers dropdown value selected until:
                                                    #'memory': browser tab is refreshed
                                                    #'session': browser tab is closed
                                                    #'local': browser cookies are deleted
        )
    ], className='three columns'),
])

#Connecting the Dropdown values to the graph
@app.callback(
    Output(component_id='our_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)

def build_graph(column_chosen):
    dff = df
    fig = px.pie(dff, names = column_chosen)
    fig.update_traces(textinfo='percent+label')
    fig.update_layout(title={'text':'NYC Calls for Animal Rescue',
                        'font':{'size':28}, 'x':0.5, 'xanchor':'center'})
    return fig

#To run the file on a server
if __name__ == '__main__':
    app.run_server(debug=True)