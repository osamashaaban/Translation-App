import streamlit as st
import re
import requests
import json
import time

# Define regext patterns
english_pattern = re.compile(r'\b[A-Za-z]+\b')
arabic_pattern = re.compile(r'[أبجدهـوزحطيكلمنسعفصقرشتثخذضظؤاإءئةى]')


st.title("Blog Translator")
st.subheader("This app is made for translating blogs from Arabic to English and vice versa")

blog = st.text_input("Enter your blog")
matches_en = re.findall(english_pattern, blog)
matches_ar = re.findall(arabic_pattern, blog)
detect = st.button("Detect Language")

# If the blog not detected make the langusge session state = None
if "language" not in st.session_state:
    st.session_state["language"] = None
    
if detect:
    # Make sure that the inputted sentence is valid - Just English or Arabic
    if (((len(matches_en) > 0) and (len(matches_ar) == 0)) or ((len(matches_en) == 0) and (len(matches_ar) > 0))):
        data = json.dumps({"text":blog})
        # Make matches empty for the next blog
        matches_en = []
        matches_ar = []
        start_time = time.time()
        # Send prediction request to detection model
        response = requests.post(url="http://127.0.0.1:8050/text",data=data)
        end_time = time.time()
        # Calculate time of prediction
        inference_time = end_time - start_time
        st.session_state["language"] = response.json()
        st.caption("Response Time: " + str(round(inference_time,6)))
        st.success(f"your blog language is: {response.json()}")
        st.header("Translation")
    else:
        matches_en = []
        matches_ar = []
        st.error(f"your blog language is NOT SUPPORTED")
        st.header("Translation")

tr = st.button("Translate your blog")

if tr:
    if st.session_state["language"]:
        st.subheader("Your Blog Language Is:  " + st.session_state["language"])
        inputs = {
            "language":st.session_state["language"],
            "text": blog
        }
        inputs = json.dumps(inputs)
        response1 = requests.post(url="http://127.0.0.1:9000/text",data=inputs)
        output = response1.json()
        st.success("Your Blog is :  \n" + output['blog'])
        if st.session_state["language"] == "English":
            st.success("Translation in Arabic :  \n" + output["Arabic"])
        elif st.session_state["language"] == "Arabic":
            st.success("Translation in English :  \n" + output["English"])
        st.session_state["language"] = None
    else:
        st.error("Detect language first")
        st.session_state["language"] = None
