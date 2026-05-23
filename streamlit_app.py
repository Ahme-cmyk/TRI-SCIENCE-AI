import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from PIL import Image
import os

st.set_page_config(page_title="TRI-SCIENCE AI", page_icon="🌿", layout="centered")

st.html("""
    <style>
    .main-title { font-size: 34px; color: #2ecc71; text-align: center; font-weight: bold; margin-bottom: 5px; font-family: sans-serif; }
    .sub-title { font-size: 16px; color: #7f8c8d; text-align: center; margin-bottom: 20px; font-family: sans-serif; }
    .report-box { background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-right: 5px solid #2ecc71; margin-top: 20px; text-align: right; }
    .section-title { color: #2c3e50; font-weight: bold; margin-top: 10px; }
    </style>
    <div class="main-title">📊 منصة TRI-SCIENCE للذكاء الاصطناعي</div>
    <div class="sub-title">النظام الذكي المتكامل لتصنيف النباتات وتشخيص أمراض الصوب الزجاجية</div>
""")

def get_treatment_sheet(disease_name):
    sheet = {
        'Basil_Downy_Mildew': {
            'عربي': 'البياض الزغبي على الريحان (Basil Downy Mildew)',
            'الأسباب': 'رطوبة عالية جداً، نقص تهوية، وزيادة مياه الري على الأوراق.',
            'العلاج الطبيعي': 'تقليل الري فوراً، زيادة المسافات بين النباتات للتهوية، وقص الأوراق المصابة بشدة.',
            'العلاج الكيميائي': 'الرش بمبيدات فطرية تحتوي على النحاس أو أكسي كلوريد النحاس.'
        },
        'Basil_Leaf_Spot': {
            'عربي': 'تبقع الأوراق على الريحان (Basil Leaf Spot)',
            'الأسباب': 'عدوى بكتيرية أو فطرية تنتقل عن طريق رذاذ المياه المستقر على الأوراق لفترات طويلة.',
            'العلاج الطبيعي': 'ري النبات من الأسفل (الجذور) وتجنب رش الأوراق بالماء.',
            'العلاج الكيميائي': 'استخدام مبيدات فطرية وقائية واسعة المدى، أو رش كبريت ميكروني بحذر.'
        },
        'Mint_Powdery_Mildew': {
            'عربي': 'البياض الدقيقي على النعناع (Mint Powdery Mildew)',
            'الأسباب': 'طقس دافئ وجاف مع رطوبة ليلية مرتفعة، ونقص ضوء الشمس المباشر.',
            'العلاج الطبيعي': 'رش محلول بيكربونات البوتاسيوم أو الحليب المخفف بالماء لتغيير حموضة الورقة.',
            'العلاج الكيميائي': 'الرش بمبيدات فطرية جهازية متخصصة في البياض الدقيقي مثل (Penconazole).'
        },
        'Mint_Rust': {
            'عربي': 'صدأ النعناع (Mint Rust)',
            'الأسباب': 'فطر الصدأ الشهير الذي ينتشر في درجات الحرارة المعتدلة والرطوبة العالية ويظهر كبقع برتقالية.',
            'العلاج الطبيعي': 'حش النبات بالكامل بالقرب من سطح التربة والتخلص من الأوراق تماماً خارج الصوبة.',
            'العلاج الكيميائي': 'الرش الفوري بمبيدات فطرية تحتوي على مادة التيبوكونازول (Tebuconazole).'
        }
    }
    return sheet.get(disease_name, None)

uploaded_file = st.file_uploader("📸 ارفع صورة ورقة النبات هنا لفحصها فوراً...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image_display = Image.open(uploaded_file)
    st.image(image_display, caption="📸 الصورة المرفوعة", use_container_width=True)
    
    with st.spinner("⏳ جاري استدعاء عقول الذكاء الاصطناعي وفحص الصورة..."):
        try:
            # قراءة الموديلات من المجلد الرئيسي
            model_plant = tf.keras.models.load_model('../plant_model.keras')
            model_health = tf.keras.models.load_model('../health_model.keras')
            
            img = image_display.resize((224, 224))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = x / 255.0

            plant_preds = model_plant.predict(x, verbose=0)
            plant_labels = {0: 'Basil (ريحان)', 1: 'Mint (نعناع)'}
            detected_plant = plant_labels[np.argmax(plant_preds)]
            plant_conf = np.max(plant_preds) * 100

            health_preds = model_health.predict(x, verbose=0)
            health_labels = {0: 'Basil_Downy_Mildew', 1: 'Basil_Leaf_Spot', 2: 'Mint_Powdery_Mildew', 3: 'Mint_Rust'}
            detected_disease = health_labels[np.argmax(health_preds)]
            health_conf = np.max(health_preds) * 100
            
            treatment = get_treatment_sheet(detected_disease)
            
            st.markdown('### 📊 التقرير الطبي الشامل للمحصول:')
            report_html = f"""
            <div class="report-box" dir="rtl">
                <h4 class="section-title">🌿 نوع النبات المكتشف:</h4>
                <p><b>{detected_plant}</b> (بنسبة تأكيد: {plant_conf:.2f}%)</p>
                <hr>
                <h4 class="section-title">🔍 التشخيص النهائي للمرض:</h4>
                <p><b>{treatment['عربي']}</b> (بنسبة تأكيد: {health_conf:.2f}%)</p>
                <hr>
                <h4 class="section-title">⚠️ أسباب الإصابة المتوقعة:</h4>
                <p>{treatment['الأسباب']}</p>
                <hr>
                <h4 class="section-title">🌱 خطة العلاج الطبيعية (البيئية):</h4>
                <p>{treatment['العلاج الطبيعي']}</p>
                <hr>
                <h4 class="section-title">💊 خطة العلاج الكيميائية والمبيدات:</h4>
                <p>{treatment['العلاج الكيميائي']}</p>
            </div>
            """
            st.html(report_html)
            st.balloons()
            
        except Exception as e:
            st.error(f"❌ حصلت مشكلة أثناء الفحص الفوري: {str(e)}")