import streamlit as st
import tensorflow as tf

# تحميل الموديل من نفس المجلد
@st.cache_resource
def load_models():
    # طالما الملفات مرفوعة في نفس فولدر الكود، المسار بيكون اسم الملف بس
    model1 = tf.keras.models.load_model("health_model.keras", compile=False)
    model2 = tf.keras.models.load_model("plant_model.keras", compile=False)
    return model1, model2

model1, model2 = load_models()
