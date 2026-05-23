from huggingface_hub import hf_hub_download
import tensorflow as tf

@st.cache_resource
def load_models():
    # تحميل الملفات من Hugging Face
    model1_path = hf_hub_download(repo_id="اسم_اليوزر_بتاعك/اسم_المستودع", filename="health_model.keras")
    model2_path = hf_hub_download(repo_id="اسم_اليوزر_بتاعك/اسم_المستودع", filename="plant_model.keras")
    
    # تحميل الموديلات بعد تنزيلها محلياً في السيرفر
    model1 = tf.keras.models.load_model(model1_path, compile=False)
    model2 = tf.keras.models.load_model(model2_path, compile=False)
    return model1, model2
