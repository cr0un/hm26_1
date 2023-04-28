# Укажите базовый образ с Python
FROM python:3.10

RUN python -m venv /app/env
ENV PATH="/app/env/bin:$PATH"

# Установите рабочую директорию
WORKDIR /app

# Копируйте файлы проекта в контейнер
COPY . .

# Установите зависимости проекта
RUN pip install -r requirements.txt

# Запускайте миграции и команду для загрузки данных
RUN python manage.py migrate
RUN python manage.py load_data

# Запускайте приложение на порту 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
