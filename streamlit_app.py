import streamlit as st
import tensorflow as tf
import requests
import os

# إعداد الصفحة
st.set_page_config(page_title="تشخيص النباتات", layout="centered")
st.title("🌱 تطبيق تشخيص أمراض النباتات")

# الروابط المباشرة للموديلات
MODEL_URLS = {
    "health_model.keras": "https://huggingface.co/spaces/ahmedhosny2052005/TRI-SCIENCE-AI/resolve/main/health_model.keras?download=true",
    "plant_model.keras": "https://huggingface.co/spaces/ahmedhosny2052005/TRI-SCIENCE-AI/resolve/main/plant_model.keras?download=true"
}

# دالة تحميل الموديلات
@st.cache_resource
def load_models():
    for filename, url in MODEL_URLS.items():
        if not os.path.exists(filename):
            with st.spinner(f"جاري تحميل {filename}..."):
                response = requests.get(url)
                with open(filename, 'wb') as f:
                    f.write(response.content)
    
    model1 = tf.keras.models.load_model("health_model.keras")
    model2 = tf.keras.models.load_model("plant_model.keras")
    return model1, model2

# تشغيل التحميل
try:
    model1, model2 = load_models()
    st.success("الموديلات جاهزة للعمل!")
except Exception as e:
    st.error(f"خطأ في تحميل الموديل: {e}")

# واجهة رفع الصورة
uploaded_file = st.file_uploader("ارفع صورة نبات هنا...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="الصورة المرفوعة", use_column_width=True)
    st.write("جاري المعالجة...")
    # هنا تحط كود التوقع بتاعك (Prediction)
