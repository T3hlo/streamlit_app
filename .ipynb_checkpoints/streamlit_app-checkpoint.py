from collections import namedtuple
import altair as alt
import math
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


'''
First actual data
'''
chart_data = pd.read_csv('AVPU.csv')
chart_data.date = pd.to_datetime(chart_data.date)
chart_data = chart_data.set_index('date')

# temp = chart_data['Voice']
# st.line_chart(temp)


source = alt.sequence(start=0, stop=12.7, step=0.1, as_='x')

st.dataframe(source)

alt.Chart(source).mark_line().transform_calculate(
    sin='sin(datum.x)',
    cos='cos(datum.x)'
).transform_fold(
    ['sin', 'cos']
).encode(
    x='x:Q',
    y='value:Q',
    color='key:N'
)


'''
# This is the document title

This is some _markdown_.
'''

with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))

'''
This is a  suplot.
'''
x = np.arange(100)
source = pd.DataFrame({
      'x': x,
      'f(x)': np.sin(x / 5)
    })



# right panel: histogram
sine = alt.Chart(source).mark_line().encode(
    x='x',
    y='f(x)')



# Compute x^2 + y^2 across a 2D grid
x, y = np.meshgrid(range(-5, 5), range(-5, 5))
z = x ** 2 + y ** 2

        # Convert this grid to columnar data expected by Altair
source = pd.DataFrame({'x': x.ravel(),
                             'y': y.ravel(),
                             'z': z.ravel()})

heat = alt.Chart(source).mark_rect().encode(
        x='x:O',
        y='y:O',
        color='z:Q'
    )              

      

# build the chart:
st.altair_chart(alt.hconcat(
    sine,
heat,
)
)
               










        



'''
This is another subplot example
'''


x = np.random.normal(size=100)
y = np.random.normal(size=100)

m = np.random.normal(15, 1, size=100)

source = pd.DataFrame({"x": x, "y":y, "m":m})



# interval selection in the scatter plot
pts = alt.selection(type="interval", encodings=["x"])

# left panel: scatter plot
points = alt.Chart().mark_point(filled=True, color="black").encode(
    x='x',
    y='y'
).transform_filter(
    pts
).properties(
    width=300,
    height=300
)

# right panel: histogram
mag = alt.Chart().mark_bar().encode(
    x='mbin:N',
    y="count()",
    color=alt.condition(pts, alt.value("black"), alt.value("lightgray"))
).properties(
    width=300,
    height=300
).add_selection(pts)

# build the chart:
st.altair_chart(alt.hconcat(
    points,
    mag,
    data=source
).transform_bin(
    "mbin",
    field="m",
    bin=alt.Bin(maxbins=20)
)
               )




