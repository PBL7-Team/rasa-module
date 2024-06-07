# Dockerfile
FROM rasa/rasa:latest-full

WORKDIR /app

# Copy all necessary files
COPY ./config /app/config
COPY ./data /app/data
COPY ./domain.yml /app/domain.yml
COPY ./credentials.yml /app/credentials.yml
COPY ./endpoints.yml /app/endpoints.yml

# Create the models directory
RUN mkdir -p /app/models

# Train the model if no tar.gz file is present in the models directory
RUN if ! ls /app/models/*.tar.gz 1> /dev/null 2>&1; then \
      rasa train; \
    fi

CMD ["run", "--enable-api", "--cors", "*", "--debug"]
