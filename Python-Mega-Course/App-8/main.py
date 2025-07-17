import glob
import streamlit as st
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon if not already present
import nltk
nltk.download('vader_lexicon')

filepaths = sorted(glob.glob("diary/*.txt"))
analyzer = SentimentIntensityAnalyzer()

negative = []
positive = []

for filepath in filepaths:
    with open(filepath) as file:
        content = file.read()
        scores = analyzer.polarity_scores(content)
        positive.append(scores["pos"])
        negative.append(scores["neg"])

dates = [name.strip(".txt").strip("diary/") for name in filepaths]

st.title("Diary Tone Analysis")

# Positivity chart
st.subheader("Positivity")
pos_figure = px.line(x=dates, y=positive,
                    labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(pos_figure)

# Negativity chart
st.subheader("Negativity")
neg_figure = px.line(x=dates, y=negative,
                   labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(neg_figure)