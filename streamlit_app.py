import streamlit as st
import tensorflow as tf
import requests
import zipfile
import os

# روابط درايف الخاصة بك (تأكد أن الملفات على "Shared with anyone with the link")
DRIVE_LINKS = {
    "health": "رابط_تحميل_ملف_الصحة_من_درايف",
    "plant": "رابط_تحميل_ملف_النباتات_من_درايف"
}

@st.cache_resource
def download_and_extract(url, zip_name, extract_to):
    # 1. تحميل الملف المضغوط من درايف
    if not os.path.exists(extract_to):
        response = requests.get(url, allow_redirects=True)
        with open(zip_name, 'wb') as f:
            f.write(response.content)
        
        # 2. فك الضغط
        with zipfile.ZipFile(zip_name, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
    return extract_to

# التحميل والتشغيل
with st.spinner('جاري جلب الموديلات من درايف...'):
    try:
        # فك ضغط الموديلات
        health_path = download_and_extract(DRIVE_LINKS["health"], "health.zip", "health_model")
        plant_path = download_and_extract(DRIVE_LINKS["plant"], "plant.zip", "plant_model")
        
        # تحميل الموديلات بعد فك الضغط (أدخل على المجلد)
        model1 = tf.keras.models.load_model(f"{health_path}/health_model.keras", compile=False)
        model2 = tf.keras.models.load_model(f"{plant_path}/plant_model.keras", compile=False)
        
        st.success("تم تشغيل التطبيق بنجاح!")
    except Exception as e:
        st.error(f"خطأ أثناء الاتصال بدرايف: {e}")
        
