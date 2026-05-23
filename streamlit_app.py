import streamlit as st
import tensorflow as tf
from huggingface_hub import hf_hub_download

@st.cache_resource
def load_models():
    # تحميل الموديلات من مستودع Hugging Face الخاص بك
    model1_path = hf_hub_download(repo_id="Ahme-cmyk/TRI-SCIENCE-AI", filename="health_model.keras")
    model2_path = hf_hub_download(repo_id="Ahme-cmyk/TRI-SCIENCE-AI", filename="plant_model.keras")
    
    # تحميل الموديلات بعد تنزيلها
    model1 = tf.keras.models.load_model(model1_path, compile=False)
    model2 = tf.keras.models.load_model(model2_path, compile=False)
    return model1, model2

# استدعاء الدالة
model1, model2 = load_models()
