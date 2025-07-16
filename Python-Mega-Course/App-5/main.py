import requests
import streamlit as st

api_key = "YscPc40NqgFqcvqbp1oi9CGWjdbmbtVgQ33exVUf"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response=requests.get(url)
apod = response.json()

title = apod["title"]
image = apod["url"]
explain = apod["explanation"]

image_filepath = "img.png"
response_img = requests.get(image)
print(response_img)
with open(image_filepath,'wb') as file:
    file.write(response_img.content)

st.title(title)
st.image(image)
st.write(explain)