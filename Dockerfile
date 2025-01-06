# Задаём базовый образ
FROM tiangolo/uwsgi-nginx-flask:python3.10

WORKDIR /app

# Копируем файл requirements.txt в рабочую директорию контейнера
COPY ./requirements.txt ./
# Запускаем установку необходимых зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копируем файл uwsgi.ini в рабочую директорию контейнера
COPY ./uwsgi.ini ./

# Копируем содержимое папки ./app в рабочую директорию контейнера
COPY ./app ./

