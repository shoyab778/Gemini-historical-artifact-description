import streamlit as st
import google.generativeai as genai
from PIL import Image

# 🔴 your API key
genai.configure(api_key="AIzaSyB0yqBc0W9V7CtQ6p7LCDNY-pfCgSO8xds")

model = genai.GenerativeModel("gemini-2.5-flash")


def get_gemini_response(text, image_part):

    prompt = f"""
You are a historian.

Follow this format EXACTLY. Do not change spacing or structure.

## 📜 Description of the Artifact:

Write a short 2–3 sentence paragraph.

• **Name:** value

• **Origin:** value

• **Time Period:** value

• **Historical Significance:** value

• **Interesting Facts:**
   ○ fact 1
   ○ fact 2
   ○ fact 3

User input: {text}
"""

    response = model.generate_content([prompt, image_part])
    return response.text


# ---------------- UI ----------------
st.set_page_config(page_title="Artifact Analyzer", page_icon="🏺")

st.title("🏺 Gemini Historical Artifact Description App")

text = st.text_input("Enter prompt (optional)")
file = st.file_uploader("Upload artifact image", type=["jpg", "jpeg", "png"])

if file:
    st.image(Image.open(file), use_container_width=True)


if st.button("🚀 Generate Artifact Description") and file:

    image_part = {
        "mime_type": file.type,
        "data": file.getvalue()
    }

    with st.spinner("Analyzing artifact..."):
        result = get_gemini_response(text, image_part)

    st.markdown(result, unsafe_allow_html=True)
