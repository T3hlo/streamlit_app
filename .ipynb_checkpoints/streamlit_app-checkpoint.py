from collections import namedtuple
import altair as alt
import math
import numpy as np
import pandas as pd
import streamlit as st


"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


'''
# This is the document title

This is some _markdown_.
'''

with st.echo(code_location='below'):
    
        with col1:
            
            total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
            num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

            Point = namedtuple('Point', 'x y')
            data = []

                  # Compute x^2 + y^2 across a 2D grid
            x, y = np.meshgrid(range(-5, 5), range(-5, 5))
            z = x ** 2 + y ** 2

            # Convert this grid to columnar data expected by Altair
            source = pd.DataFrame({'x': x.ravel(),
                                 'y': y.ravel(),
                                 'z': z.ravel()})

            st.altair_chart(alt.Chart(source).mark_rect().encode(
            x='x:O',
            y='y:O',
            color='z:Q'
        ), 

                            alt.Chart(source).mark_rect().encode(
            x='x:O',
            y='y:O',
            color='z:Q'
        )

                )

'''
This is an interatcive plot.
'''

            
col1, col2 = st.beta_columns(2)




with col1:
    
    x = np.arange(100)
    source = pd.DataFrame({
      'x': x,
      'f(x)': np.sin(x / 5)
    })



    st.altair_chart(alt.Chart(source).mark_line().encode(
    x='x',
    y='f(x)'))


    

with col2:

        # Compute x^2 + y^2 across a 2D grid
        x, y = np.meshgrid(range(-5, 5), range(-5, 5))
        z = x ** 2 + y ** 2

        # Convert this grid to columnar data expected by Altair
        source = pd.DataFrame({'x': x.ravel(),
                             'y': y.ravel(),
                             'z': z.ravel()})

        st.altair_chart(alt.Chart(source).mark_rect().encode(
        x='x:O',
        y='y:O',
        color='z:Q'
    )              

      )
        


'''
This is asupbplot
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
alt.hconcat(
    points,
    mag,
    data=source
).transform_bin(
    "mbin",
    field="m",
    bin=alt.Bin(maxbins=20)
)


'''
This is another subplot example
'''


col1, col2, = st.beta_columns()

with col1:
    st.header("A cat")
    
    st.altair_chart(mag)              

      
        
    
with col1:
    st.header("A cat")
    st.altair_chart(points)
