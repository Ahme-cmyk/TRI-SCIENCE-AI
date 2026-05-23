from huggingface_hub import hf_hub_download
import tensorflow as tf

@st.cache_resource
def load_models():
    # تحميل الملفات من Hugging Face
    model1_path = hf_hub_download(repo_id="اسم_اليوزر_بتاعك/اسم_المستودع", filename="health_model.keras")
    model2_path = hf_hub_download(repo_id="اسم_اليوزر_بتاعك/اسم_المستودع", filename="plant_model.keras")
    
    # تحميل الموديلات بعد تنزيلها محلياً في السيرفر
   model1_path = hf_hub_download(repo_id="Ahme-cmyk/TRI-SCIENCE-AI", filename="health_model.keras")
model2_path = hf_hub_download(repo_id="Ahme-cmyk/TRI-SCIENCE-AI", filename="plant_model.keras")
    return model1, model2
