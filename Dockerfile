# Dockerfile
FROM rasa/rasa:latest-full
USER root
WORKDIR /app

# Copy all necessary files
COPY ./config.yml /app/config.yml
COPY ./data /app/data
COPY ./domain.yml /app/domain.yml
COPY ./credentials.yml /app/credentials.yml
COPY ./endpoints.yml /app/endpoints.yml

# Create the models directory
RUN mkdir -p /app/models


# Copy the entrypoint script
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]