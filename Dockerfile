FROM python:3.11-slim

WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё содержимое (collector, common, .env)
COPY . .

# Указываем, что искать модули нужно в /app
ENV PYTHONPATH=/app

# ЗАПУСК ЧЕРЕЗ МОДУЛЬ (без расширения .py и через точку)
CMD ["python", "-u", "-m", "main"]