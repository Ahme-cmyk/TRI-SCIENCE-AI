import streamlit as st
import tensorflow as tf
import zipfile
import os

# 1. فك الضغط تلقائياً عند تشغيل التطبيق
zip_file_path = 'ددددددددددددد.zip' # تأكد من تطابق الاسم تماماً
extract_to = '.' # يعني فك الضغط في نفس المجلد

if os.path.exists(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        st.write("تم فك ضغط الملفات بنجاح!")

# 2. تحميل الموديلات بعد فك الضغط
@st.cache_resource
def load_models():
    # تأكد أن هذه هي الأسماء الصحيحة للملفات بعد فك الضغط
    model1 = tf.keras.models.load_model("health_model.keras", compile=False)
    model2 = tf.keras.models.load_model("plant_model.keras", compile=False)
    return model1, model2

try:
    model1, model2 = load_models()
    st.success("تم تحميل الموديلات وتشغيل التطبيق بنجاح! 🎉")
except Exception as e:
    st.error(f"خطأ: {e}")
    st.write("تأكد أن أسماء ملفات الموديلات داخل الـ Zip هي health_model.keras و plant_model.keras")
