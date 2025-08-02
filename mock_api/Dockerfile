# Используем официальный образ Python
FROM python:3.13-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код и данные
COPY main.py .
COPY responses/ responses/

# Указываем порт, который будет слушать uvicorn
EXPOSE 8000

# Запускаем сервер
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
