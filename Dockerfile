FROM python:3

# устанавливаем параметры сборки
RUN apt-get update && apt-get install -y gcc make apt-transport-https ca-certificates build-essential

# проверяем окружение python
RUN python3 --version
RUN pip3 --version

# задаем рабочую директорию для контейнера
WORKDIR  /usr/src/app

# устанавливаем зависимости python
COPY /test /usr/src/app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["chmod", "+x", "main.py"]
CMD ["python3", "main.py * Running on http://127.0.0.1:5000/"]
