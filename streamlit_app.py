import streamlit as st
import tensorflow as tf
import os
import requests

@st.cache_resource
def load_models():
    # روابط الموديلات (إذا كانت عندك على Google Drive، ضع الروابط هنا)
    # إذا لم تكن متوفرة، سأعطيك حلاً آخر فوراً
    model1 = tf.keras.models.load_model("https://github.com/Ahme-cmyk/TRI-SCIENCE-AI/raw/main/health_model.keras", compile=False)
    model2 = tf.keras.models.load_model("https://github.com/Ahme-cmyk/TRI-SCIENCE-AI/raw/main/plant_model.keras", compile=False)
    return model1, model2

# ... باقي كود التطبيق الخاص بك
