# Используем базовый образ Python
FROM python:3.12

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
