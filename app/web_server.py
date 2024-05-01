import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Get the API key from the environment variable
API_KEY = os.getenv("IPGEOLOCATION_API_KEY")

@app.route('/timezone', methods=['GET'])
def get_timezone():
    ip_address = request.args.get('ip')

    if not API_KEY:
        return jsonify({'error': 'API key is not set'}), 500

    if not ip_address:
        return jsonify({'error': 'IP address is required'}), 400

    response = requests.get(
        f"https://api.ipgeolocation.io/timezone?apiKey={API_KEY}&ip={ip_address}"
    )

    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch data from IP Geolocation API'}), 500

    data = response.json()
    return jsonify({'timezone': data.get('timezone')}), 200


@app.route('/health', methods=['GET'])
def health(): 
    return jsonify({'status': 'OK'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, ssl_context=('server.crt', 'server.key'))
