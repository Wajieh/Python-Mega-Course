import streamlit as st
import pandas as pd
from email import send_email
st.header("Contact Us")
df = pd.read_csv("topics.csv")

with st.form(key="form"):
    user_email = st.text_input("Enter your email address")
    option = st.selectbox("What do you want to discuss about?",df["topic"])
    comments = st.text_area("Comments")
    message = f"""\
    Subject: New email from {user_email}
    From: {user_email}
    Topic: {option}
    Message: {comments}"""

    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info("Email sent successfully")