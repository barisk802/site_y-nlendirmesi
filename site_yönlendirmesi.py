import streamlit as st
import webbrowser
import streamlit as st

st.title("🌐 Site Yönlendirme")

st.markdown("[📸 Instagram'a Git](https://www.instagram.com/bariskaya_1912/)")
st.markdown("[🐦 Twitter'a Git](https://x.com/Bariskaya_1907)")
st.markdown("[▶️ YouTube'a Git](https://www.youtube.com/@bariskaya1907)")
st.title("🌐 Site Yönlendirme")

if st.button("Instagram'a Git"):
    webbrowser.open("https://www.instagram.com/bariskaya_1912/")

if st.button("Twitter'a Git"):
    webbrowser.open("https://x.com/Bariskaya_1907")

if st.button("YouTube'a Git"):
    webbrowser.open("https://www.youtube.com/@bariskaya1907")



