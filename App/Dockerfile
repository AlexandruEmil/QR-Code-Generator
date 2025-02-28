# Utilizăm o imagine Python oficială
FROM python:3.9-slim

# Setăm directorul de lucru
WORKDIR /app

# Copiem fișierele necesare
COPY requirements.txt .
COPY app.py .

# Instalăm dependințele
RUN pip install --no-cache-dir -r requirements.txt

# Expunem portul 5000
EXPOSE 5000

# Pornim aplicația
CMD ["python", "app.py"]