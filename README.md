# Timezone Service

This service provides the time zone of an IP address. It is implemented as an HTTPS endpoint using Flask and uses `https://ipgeolocation.io` to retrieve the time zone of the given IP address.

## Requirements
* Docker - https://docs.docker.com/get-docker/
* ipgeolocation.io API key - https://app.ipgeolocation.io/login

## Getting Started

1. Clone the repository and navigate to the project directory:
    ```bash
    git clone https://github.com/Miller-5/timezone_service.git
    cd timezone_service
    ```

2. Build the Docker container:
    ```bash
    docker build -t timezone_service .
    ```
3. Run the docker container and provide your ipgeolocation.io API key:
    * Replace ***[your-api-key]*** with the key you got from ipgeolocation.io
    ```bash
    docker run -p 5000:443 --env IPGEOLOCATION_API_KEY=[your-api-key] timezone_service
    ```
4. Access the service at https://127.0.0.1:5000/timezone?ip=***[required-ip]***
    * Replace ***[required-ip]*** with the ip you want to get the timezone of, for example:
        https://127.0.0.1:5000/timezone?ip=8.8.8.8