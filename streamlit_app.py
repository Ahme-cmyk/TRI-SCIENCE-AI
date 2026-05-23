import streamlit as st
import tensorflow as tf
import requests
import os

# دالة التحميل المباشر
def download_file(file_id, filename):
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    if not os.path.exists(filename):
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)

@st.cache_resource
def load_models():
    # معرفات الملفات (اللي بعد /d/ وقبل /view)
    id1 = "1FhkJtdD8XHpKy9vFQGCrJpvsHsCs3O73"
    id2 = "1MY9O2VcEDeQm7M_jv1_88st17rAxECtR"
    
    download_file(id1, "health_model.keras")
    download_file(id2, "plant_model.keras")
    
    model1 = tf.keras.models.load_model("health_model.keras", compile=False)
    model2 = tf.keras.models.load_model("plant_model.keras", compile=False)
    return model1, model2

model1, model2 = load_models()
# كمل باقي الكود بتاعك من هنا...
