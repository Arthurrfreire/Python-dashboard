import pandas as pd
import plotly.express as px
from sklearn.datasets import load_wine
from dash import Dash, html, dcc, callback
from dash.dependencies import Input, Output


# Load Data
def load_data():
    wine = load_wine()
    wine_df = pd.DataFrame(wine.data, columns=wine.feature_names)
    wine_df["WineType"] = [wine.target_names[t] for t in wine.target]
    return wine_df

wine_df = load_data()
ingredients = wine_df.drop(columns=["WineType"]).columns

avg_wine_df = wine_df.groupby("WineType").mean().reset_index()

# Charts
def create_scatter_chart(x_axis="alcohol", y_axis="malic_acid", color_encode=False):
    scatter_fig = px.scatter(wine_df, x=x_axis, y=y_axis, color="WineType" if color_encode else None, title="{} vs{}".format(x_axis.capitalize(), y_axis.capitalize()))
    scatter_fig.update_layout(height=600)
    return scatter_fig

def create_bar_chart(ingredients=["alchool", "malic_acid", "ash"]):
    bar_fig = px.bar(avg_wine_df, x="WineType", y=ingredients, title="Avg. Ingrecients per Wine Type")
    