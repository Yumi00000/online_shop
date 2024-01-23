FROM python:3.9

RUN apt-get update && \
    apt-get install -y postgresql postgresql-contrib gcc libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /online_shop

COPY alembic alembic
COPY requirements.txt requirements.txt
COPY static static
COPY models models
COPY urls urls
COPY templates templates
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
