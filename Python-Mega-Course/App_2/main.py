import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("Big Company")
st.write("Very Big Company")
st.subheader("Our Big Team")


c1, c2, c3 = st.columns(3)
df = pandas.read_csv("data.csv")

with c1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with c2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with c3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])




