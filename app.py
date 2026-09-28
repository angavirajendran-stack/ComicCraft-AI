import streamlit as st
import requests
import zipfile
import io
from io import BytesIO
import urllib.parse

st.set_page_config(page_title="ComicCraft-AI", page_icon="💬", layout="wide")
st.title("ComicCraft-AI 💬 - AI Comic Generator")
st.write("Convert your story into a 4-panel comic strip using AI.")

story = st.text_area("Enter your story here:")

if st.button("Generate Comic"):
    if story:
        st.success("Comic Generated Successfully!")
        
        image_urls = []
        cols = st.columns(2)
        
        for i in range(4):
            prompt = urllib.parse.quote(f"{story}, comic book panel {i+1}, detailed comic art, vibrant colors")
            img_url = f"https://image.pollinations.ai/prompt/{prompt}?width=512&height=512&seed={i}"
            image_urls.append(img_url)
            
            with cols[i % 2]:
                st.subheader(f"Panel {i+1}")
                st.image(img_url, caption=f"Panel {i+1}", use_container_width=True)

        # Download Section
        st.divider()
        st.subheader("Download Options")
        
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zip_file:
            for idx, url in enumerate(image_urls):
                try:
                    r = requests.get(url, timeout=10)
                    zip_file.writestr(f"Panel_{idx+1}.jpg", r.content)
                except Exception as e:
                    st.error(f"Failed to download Panel {idx+1}")
        
        zip_buffer.seek(0)

        st.download_button(
            label="Download All Panels as ZIP",
            data=zip_buffer,
            file_name="ComicCraft_Output.zip",
            mime="application/zip",
            type="primary"
        )
    else:
        st.warning("Please enter a story to generate the comic.")
