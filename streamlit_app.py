import streamlit as st
import tensorflow as tf
from huggingface_hub import hf_hub_download

@st.cache_resource
def load_models():
    # هذا الكود سيقوم بتحميل الموديلات من مستودعك على Hugging Face
    # تأكد فقط أن المستودع العام (Public)
    model1_path = hf_hub_download(repo_id="ahmedhosny2052005/TRI-SCIENCE-AI", filename="health_model.keras")
    model2_path = hf_hub_download(repo_id="ahmedhosny2052005/TRI-SCIENCE-AI", filename="plant_model.keras")
    
    # تحميل الموديلات
    model1 = tf.keras.models.load_model(model1_path, compile=False)
    model2 = tf.keras.models.load_model(model2_path, compile=False)
    return model1, model2

# استدعاء الموديلات
try:
    model1, model2 = load_models()
    st.success("تم تحميل الموديلات بنجاح!")
except Exception as e:
    st.error(f"حدث خطأ أثناء تحميل الموديلات: {e}")
    st.write("تأكد أن المستودع على Hugging Face عام (Public) وأن أسماء الملفات صحيحة.")
