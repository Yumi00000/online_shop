FROM python:3.9


RUN apt-get update && \
    apt-get install -y postgresql postgresql-contrib gcc libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy necessary files
COPY alembic alembic
COPY models models
COPY static static
COPY templates templates
COPY urls urls
COPY requirements.txt requirements.txt


RUN pip install --upgrade pip && pip install -r requirements.txt

# Create a non-root user
RUN useradd -ms /bin/bash celeryuser

# Set the working directory
WORKDIR /app

# Change ownership of the application files to the non-root user
RUN chown -R celeryuser /app

# Switch to the non-root user
USER celeryuser

COPY . .


EXPOSE 5000


ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Command to run Celery worker and Flask app
CMD ["sh", "-c", "celery -A tasks worker --loglevel=info & python app.py"]

