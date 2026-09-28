import streamlit as st

st.set_page_config(page_title="ComicCraft-AI", page_icon="💬", layout="wide")

st.title("💬 ComicCraft-AI")
st.write("Welcome to your Comic Creator!")

prompt = st.text_area("Un comic story ah inga type pannu:", placeholder="Eg: A cat superhero flying in Madurai...")

if st.button("Generate Comic"):
    if prompt:
        st.success(f"Story received: {prompt}")
        st.info("AI Generation logic will be added here. For now deploy is working!")
        st.image("https://via.placeholder.com/600x400?text=Your+Comic+Will+Appear+Here")
    else:
        st.warning("Please enter a story first da!")