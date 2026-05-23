import streamlit as st
import tensorflow as tf

# هذه الدالة هي كل اللي محتاجه الـ Space
@st.cache_resource
def load_models():
    # طالما الملفات مرفوعة جوه الـ Space، بنفتحها بالاسم مباشرة
    model1 = tf.keras.models.load_model("health_model.keras", compile=False)
    model2 = tf.keras.models.load_model("plant_model.keras", compile=False)
    return model1, model2

# استدعاء الموديلات
try:
    model1, model2 = load_models()
    st.success("تم تشغيل التطبيق بنجاح!")
except Exception as e:
    st.error(f"خطأ: {e}")
