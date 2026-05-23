import streamlit as st
import tensorflow as tf
import requests
import os

# دالة لتحميل الملف إذا لم يكن موجوداً
def download_model(url, filename):
    if not os.path.exists(filename):
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)

@st.cache_resource
def load_models():
    # روابط التحميل المباشرة من الـ Space الخاص بك
    # تأكد من الروابط بالضغط على زر التحميل في Hugging Face ونسخ الرابط
    url1 = "https://huggingface.co/spaces/ahmedhosny2052005/TRI-SCIENCE-AI/resolve/main/health_model.keras"
    url2 = "https://huggingface.co/spaces/ahmedhosny2052005/TRI-SCIENCE-AI/resolve/main/plant_model.keras"
    
    download_model(url1, "health_model.keras")
    download_model(url2, "plant_model.keras")
    
    model1 = tf.keras.models.load_model("health_model.keras", compile=False)
    model2 = tf.keras.models.load_model("plant_model.keras", compile=False)
    return model1, model2

model1, model2 = load_models()
