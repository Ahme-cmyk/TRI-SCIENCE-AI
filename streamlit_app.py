import streamlit as st
import tensorflow as tf
import zipfile
import os

# 1. فك ضغط الملف
zip_file_path = 'ددددددددددددد.zip' 
if os.path.exists(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall('.')

# 2. دالة البحث عن الملفات في أي مكان
def find_file(filename):
    for root, dirs, files in os.walk("."):
        if filename in files:
            return os.path.join(root, filename)
    return None

@st.cache_resource
def load_models():
    path1 = find_file("health_model.keras")
    path2 = find_file("plant_model.keras")
    
    if not path1 or not path2:
        raise FileNotFoundError(f"لم أجد الملفات! الملفات الموجودة حالياً: {os.listdir('.')}")
        
    return tf.keras.models.load_model(path1, compile=False), \
           tf.keras.models.load_model(path2, compile=False)

try:
    with st.spinner('جاري البحث عن الموديلات وتحميلها...'):
        model1, model2 = load_models()
        st.success("تم العثور على الموديلات وتشغيل التطبيق بنجاح! 🎉")
except Exception as e:
    st.error(f"خطأ: {e}")
