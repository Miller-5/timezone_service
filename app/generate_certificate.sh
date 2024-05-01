#!/bin/bash

openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout server.key -out server.crt \
    -subj "/C=US/ST=California/L=San Francisco/O=My Organization/OU=Dev/CN=localhost"
