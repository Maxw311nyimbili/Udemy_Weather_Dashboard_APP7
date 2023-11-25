import streamlit as st
import plotly.express as px

st.title("Weather Forecast For the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days ", min_value=1, max_value=5,
                 help="select number of days to forecast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place.capitalize()}")

# to draw the graph import plotly.express, then use plotly_chart()
# you will also need a corresponding list of dates and temperatures and they should
# be of the same length

dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
temperature = [10, 11, 15]

figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y" : "Temperature"})
st.plotly_chart(figure)