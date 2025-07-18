import streamlit as st
import plotly.express as px
from backend import get_data

images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
          "Rain": "images/rain.png", "Snow": "images/snow.png"}

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
       # Get Data
    filtered_data = get_data(place,days,option)

    if option == "Temperature":
        temperatures = [dicti["main"]["temp"] / 10 for dicti in filtered_data]
        dates = [dicti["dt_txt"] for dicti in filtered_data]
        figure = px.line(x=dates,y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        sky_conditions = [dicti["weather"][0]["main"] for dicti in filtered_data]
        print(sky_conditions)    
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, width=120)
