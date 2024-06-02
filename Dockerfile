# Use the official Rasa image as a parent image
FROM rasa/rasa:3.6.2-full

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# By default, Rasa runs the `rasa run` command
CMD ["rasa", "run", "--cors", "*", "--enable-api", "--debug"]
