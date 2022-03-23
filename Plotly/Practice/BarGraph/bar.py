import pandas as pd
import plotly
import plotly.express as px
import plotly.io as pio

df = pd.read_csv("Caste.csv")
# Focus only on Maharashtra state
df = df[df['state_name']=='Maharashtra']
df = df.groupby(['year', 'gender'], as_index=False)[['detenues','under_trial','convicts','others']].sum()
# print(df[:5])

barchart = px.bar(
    data_frame=df,
    # x="year",
    x='gender',
    y="convicts",
    #to use animation frame.... commented it #color="gender",         # differentiate color of marks
    opacity=0.9,            # set opacity of markers (from 0 to 1)
    orientation="v",        #'v', 'h': orientation of the marks\
    barmode='relative',     # in overlay mode, bars are top of one another.
                            # in group mode, bars are placed beside each other
    # ----------------------------------------------------------------------------------------- #
    # facet_row='caste',      # assign marks to subplots in the vertical direction... 
                            # it is good to use when you want to show multiple types of data
    # facet_col='',
    # facet_col_wrap=2,     # maximum number of subplot columns. Do not set facet_rows

    # color_discrete_sequence=["pink", "yellow"] # set specific marker colors. 
    # color_discrete_map={"Male": "gray", "Female":"red"} # map your chosen colors... Use when you don't know which thing comes first or second or third
    # color_continuous_scale=px.colors.diverging.Picnic, # Set marker colors. When color column is numeric data # color code continuous values
    # use color continuous with range_color # Look at built in continuous color scales in the documentation
    # color_continuous_midpoint=100, 
    # range_color=[1,1000],

    # ---------------------------------------------------------------------------------------- #
    text='convicts',            # values appear in figure text labels
    hover_name='under_trial',   # values appear in bold in the hover tooltip
    hover_data=['detenues'],    # values appear as extra data in the hovel tooltip
    custom_data=['others'],     # invisible values that are extra data to be used in Dash callbacks or widgets
    # ---------------------------------------------------------------------------------------- #
    labels={"convicts":"Convicts in Maharashtra",
    "Gender":"Gender"},             #map the labels of the figures
    title='Indian Prison Statistics', #figure title
    width=1400,
    height=720,
    template='plotly_dark',
    # ---------------------------------------------------------------------------------------- #
    animation_frame='year',     # assign marks to animation frames
    #animation_group=,           # use only when df has mutiple rows with same objects
    #range_x=[5,50],             # set range of x-axis
    range_y=[0,9000],
    category_orders={'year':     # force a specific ordering of values per column
    [2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001]},
)

barchart.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1000     # 1 second
barchart.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 500   # 0.5 second

pio.show(barchart)