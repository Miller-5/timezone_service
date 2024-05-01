# Dockerfile for containerizing the Flask app
FROM python:3.9

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the Flask app code
COPY app/. .

# Generate the SSL certificate
RUN chmod +x generate_certificate.sh && ./generate_certificate.sh

# Set the command to start the Flask server
CMD ["python", "web_server.py"]