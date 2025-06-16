# Базовый образ Python
FROM python:3.9

# Установить рабочую директорию в контейнере
WORKDIR /app

# Скопировать все файлы проекта внутрь контейнера
COPY . .

# Установить зависимости (если есть файл requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Открыть порт
EXPOSE 5000

# Команда запуска Flask-приложения
CMD ["python", "app.py"]