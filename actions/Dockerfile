# actions/Dockerfile
FROM rasa/rasa-sdk:latest
USER root
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["start", "--actions", "actions"]