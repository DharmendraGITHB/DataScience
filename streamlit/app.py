import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title= "Dharmendra", page_icon="kumar", layout= "wide")

def load_lottieurl(url):
    r= requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_qp1q7mct.json")

st.subheader("Hi, I am Dharmendra:")

st.title("Data Science")
st.write("kdkdkdkdkdkdkdk")

st.write("[check github profile >](https://github.com/DharmendraGITHB)")

with st.container():
    left_column, right_column = st.columns(2)

with right_column:
    st_lottie(lottie_coding, height =300, key="coding")
