import streamlit as st
import plotly.express as px

st.title("Weather Forecast For the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days ", min_value=1, max_value=5,
                 help="select number of days to forecast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place.capitalize()}")

