import plotly.express as px
import streamlit as st
import pandas as pd
import numpy as np

df = px.data.gapminder().query('year == 2007')
ig = px.treemap(df, path=[px.Constant("World"), 'continent', 'country'], values='pop', color='lifeExp')
fig.show()
