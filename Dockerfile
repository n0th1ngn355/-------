# Используем базовый образ Python
FROM python:3.13.0a6-slim-bookworm

# Устанавливаем рабочую директорию в /app
WORKDIR /app

# Копируем зависимости в образ
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем содержимое текущей директории в образ в /app
COPY . .

# Запускаем приложение при старте контейнера
CMD ["python", "server.py"]
