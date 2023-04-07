import streamlit as st
import pandas
from send_mail import send_mail

st.header("CONTACT US ")

df = pandas.read_csv("topics.csv")

with st.form(key="email form"):
    user_email = st.text_input("enter your Email here: ")
    select_topic = st.selectbox("select the topic from below options:",
                                df["topic"])
    message = st.text_area("enter the message: ")
    message = f""""\
Subject: new email from {user_email}

From: {user_email}
topic: {select_topic}
{message}
"""
    button = st.form_submit_button("SUBMIT")
    if button:
        send_mail(message)
        st.info("Email has been sent successfully:")
