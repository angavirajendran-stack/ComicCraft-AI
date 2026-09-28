import streamlit as st
import requests
import zipfile
import io
from io import BytesIO
import urllib.parse

st.set_page_config(page_title="ComicCraft-AI", page_icon="💬")
st.title("ComicCraft-AI 💬")
st.write("Your story to 4 panel comic!")

story = st.text_area("Story ah inga type pannu da:")

if st.button("Generate Comic"):
    if story:
        st.success("Story received! Your Comic is Ready!")
        
        image_urls = []
        cols = st.columns(2)
        
        for i in range(4):
            prompt = urllib.parse.quote(f"{story}, comic panel {i+1}, comic book style, vibrant")
            img_url = f"https://image.pollinations.ai/prompt/{prompt}"
            image_urls.append(img_url)
            
            with cols[i % 2]:
                st.subheader(f"Panel {i+1}")
                st.image(img_url, caption=f"Panel {i+1}")

        # DOWNLOAD PART - ITHA THAAN ADD PANNOM
        st.write("---")
        st.subheader("📥 Download Pannu da!")
        
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zip_file:
            for idx, url in enumerate(image_urls):
                try:
                    r = requests.get(url)
                    zip_file.writestr(f"Panel_{idx+1}.jpg", r.content)
                except:
                    pass
        zip_buffer.seek(0)

        st.download_button(
            label="🔥 Download All 4 Panels as ZIP",
            data=zip_buffer,
            file_name="ComicCraft_Comic.zip",
            mime="application/zip"
        )
    else:
        st.warning("Macha story type pannu da!")
