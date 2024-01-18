
FROM python:3.9


RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev


WORKDIR /online_shop
COPY requirements.txt /online_shop/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt



COPY . /online_shop/


CMD ["python", "app.py"]
