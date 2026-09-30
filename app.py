import streamlit as st
import requests
import zipfile
import io
import urllib.parse
import time

st.set_page_config(page_title="ComicCraft-AI", page_icon="💬", layout="wide")
st.title("ComicCraft-AI - AI Comic Generator")
st.write("Convert your story into a 4-panel comic strip using AI.")

story = st.text_area("Enter your story here:", placeholder="Type your story here... e.g., A boy finds a magical key")

if st.button("Generate Comic", type="primary"):
    if story:
        st.success("Comic Generated Successfully! Please wait for images to load.")
        
        image_urls = []
        cols = st.columns(2)
        
        for i in range(4):
            prompt = urllib.parse.quote(f"{story}, comic book panel {i+1}, detailed comic art, vibrant colors, high quality")
            # Better URL with random seed to avoid cache error
            seed = int(time.time()) + i
            img_url = f"https://image.pollinations.ai/prompt/{prompt}?width=512&height=512&seed={seed}&nologo=true"
            image_urls.append(img_url)
            
            with cols[i % 2]:
                st.subheader(f"Panel {i+1}")
                st.image(img_url, caption=f"Panel {i+1}", use_container_width=True)

        # Download Section - Fixed
        st.divider()
        st.subheader("Download Options")
        
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zip_file:
            for idx, url in enumerate(image_urls):
                try:
                    # Increased timeout and retry
                    r = requests.get(url, timeout=30)
                    if r.status_code == 200:
                        zip_file.writestr(f"Panel_{idx+1}.jpg", r.content)
                except Exception as e:
                    st.warning(f"Panel {idx+1} is still loading, please try downloading again in 10 seconds.")
        
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
