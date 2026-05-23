import streamlit as st
import tensorflow as tf
import requests
import os

# نستخدم هذا السطر للتأكد من استخدام النسخة المدمجة مع تنسرفلو
from tensorflow import keras

@st.cache_resource
def load_models():
    # ... (نفس الكود السابق لتحميل الملفات من الرابط) ...
    
    # التعديل هنا: استخدام tf.keras.models.load_model مباشرة
    model1 = tf.keras.models.load_model("health_model.keras", compile=False)
    model2 = tf.keras.models.load_model("plant_model.keras", compile=False)
    return model1, model2
