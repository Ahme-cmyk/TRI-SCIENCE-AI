import streamlit as st
import tensorflow as tf
import requests
import os

# روابط الموديلات اللي إنت بعتها
model_urls = {
    "health_model.keras": "https://huggingface.co/spaces/ahmedhosny2052005/TRI-SCIENCE-AI/resolve/main/health_model.keras?download=true",
    "plant_model.keras": "https://huggingface.co/spaces/ahmedhosny2052005/TRI-SCIENCE-AI/resolve/main/plant_model.keras?download=true"
}

# دالة لتحميل الموديلات إذا لم تكن موجودة
@st.cache_resource
def load_models():
    for filename, url in model_urls.items():
        if not os.path.exists(filename):
            st.write(f"جاري تحميل {filename}... استنى لحظة.")
            r = requests.get(url, allow_redirects=True)
            with open(filename, 'wb') as f:
                f.write(r.content)
    
    # تحميل الموديلات في الرامات
    model1 = tf.keras.models.load_model("health_model.keras")
    model2 = tf.keras.models.load_model("plant_model.keras")
    return model1, model2

# تشغيل التحميل
st.title("تطبيق تشخيص النباتات الذكي")
model1, model2 = load_models()
st.success("تم تحميل الموديلات بنجاح! الموقع جاهز للاستخدام.")

# هنا حط باقي كود الـ UI الخاص بيك (رفع الصورة، النتيجة، إلخ...)
