FROM python:3.13.5-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

# نسخ الملفات
COPY . .

EXPOSE 7860

# أمر الفحص السحري اللي هيخلي السيرفر يلقط الإشارة فوراً على البورت 7860
HEALTHCHECK --interval=30s --timeout=15s --start-period=60s --retries=3 \
    CMD curl --fail http://localhost:7860/_stcore/health || exit 1

# تشغيل الملف بالاسم والمسار الصحيحين
CMD ["python3", "-m", "streamlit", "run", "src/streamlit_app.py", "--server.port", "7860", "--server.address", "0.0.0.0"]