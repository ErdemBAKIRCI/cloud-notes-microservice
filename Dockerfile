# 1. Hafif bir Python imajı kullanıyoruz
FROM python:3.10-slim

# 2. Çalışma dizinini ayarlıyoruz
WORKDIR /code

# 3. Bağımlılıkları kopyalayıp yüklüyoruz
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 4. Tüm kodları içeri kopyalıyoruz
COPY ./app /code/app

# 5. Uygulamayı dış dünyaya açıyoruz
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
