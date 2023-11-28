import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast For the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days ", min_value=1, max_value=5,
                 help="select number of days to forecast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))


# to draw the graph import plotly.express, then use plotly_chart()
# you will also need a corresponding list of dates and temperatures and they should
# be of the same length


if place != "":

    try:
        st.subheader(f"{option} for the next {days} days in {place.capitalize()}")
        filtered_data = get_data(place=place, forecast_days=days)
        if option == "Temperature":
            temperatures = [(dict_1["main"]["temp"])/10 for dict_1 in filtered_data]
            print(temperatures)
            dates = [dict_1["dt_txt"] for dict_1 in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png",
                      "images/snow": "images/snow.png"}
            sky_condition = [dict_2["weather"][0]["main"] for dict_2 in filtered_data]
            image_paths = [images[condition] for condition in sky_condition]
            st.image(image_paths, width=105)
    except KeyError:
        st.info(f"No information found for {place}")


