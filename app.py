import streamlit as st
import urllib.parse

st.set_page_config(page_title="ComicCraft-AI", page_icon="💬")
st.title("💬 ComicCraft-AI")
st.write("Welcome to your Comic Creator!")

story = st.text_area("Un comic story ah inga type pannu:", placeholder="Eg: A cat superhero flying in Madurai...")

if st.button("Generate Comic"):
    if story:
        st.success(f"Story received: {story}")
        
        # Story ah 4 panels ah split pannrom
        st.write("### Your Comic is Ready! 🔥")
        
        prompts = [
            f"comic book panel 1, {story}, cartoon style, vibrant",
            f"comic book panel 2, {story}, action scene, cartoon style",
            f"comic book panel 3, {story}, funny expression, cartoon style",
            f"comic book panel 4, {story}, epic finale, cartoon style"
        ]
        
        cols = st.columns(2)
        for i, p in enumerate(prompts):
            encoded_prompt = urllib.parse.quote(p)
            image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=512&height=512&seed={i}"
            cols[i % 2].image(image_url, caption=f"Panel {i+1}")

        st.balloons()
    else:
        st.warning("Macha, story ah type pannu da!")
