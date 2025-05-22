import streamlit as st

st.title("🎈 My new Streamlit app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.text_input("Enter your name")
studymethod = st.selectbox ("StudyMethod", "Crammer", "Pre-Planner")
st.button("Diva")

if button:
    with st.spinner("Loading your divs stastud"):
        if studymethod