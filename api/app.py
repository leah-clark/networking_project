from flask import Flask
from source import internet_protocol_service as ip_service
from flask import abort
from flask import jsonify

import logging

app = Flask(__name__)

@app.route('/api/ip', methods=["GET"])
def ip():
    return jsonify(ip_service.get_ip())

if __name__ == '__main__':
    app.run()
