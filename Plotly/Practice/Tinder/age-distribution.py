import pandas as pd
import plotly
import plotly.express as px

df = pd.read_csv("profiles.csv")

fig = px.histogram(df, x="age")
fig.show()