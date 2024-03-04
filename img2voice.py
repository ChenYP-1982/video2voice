from dotenv import find_dotenv, load_dotenv
import streamlit as st
import requests
import os



from transformers import pipeline
import warnings

warnings.filterwarnings("ignore")

# Load .envfile
load_dotenv(find_dotenv())
Huggingface_api_token=os.getenv("api_token")

# gerando texto para imagem 

def img2text(path):
    img_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")

    text= img_to_text(path)[0]["generated_text"]
    
    print(text)

    return text


# converting text to speech
def text2speedch(text, speed=1):
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {Huggingface_api_token}"}
    payloads={
        "inputs": text
    }

    response=requests.post(API_URL,headers=headers,json=payloads)
    with open("audio.wav", "wb")as f:
        f.write(response.content)

def main():
    st.set_page_config(layout="wide",
                       page_title="Image to audio",
                       page_icon="🤖")
    st.header("Turn image to speech")
    upload_file= st.file_uploader("Please Choose your image file", type=["jpg","png"])


