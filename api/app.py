from flask import Flask
from flask import request
from source import internet_protocol_service as ip_service
from flask import abort
from flask import jsonify
import time

import logging
from exceptions import custom_exceptions

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/api/ip', methods=["POST"])
def ip():
    typeOfIp = request.json['ip_type']
    if (typeOfIp):
        try:
            return jsonify(ip_service.get_ip(typeOfIp))
        except custom_exceptions.InputError as e:
           logging.error(str(e.message))
           abort(400, "IP type provided = " + str(e.expression) + ", error = " + str(e.message))
        except Exception as e:
           logging.error("Unknown Exception occured" + str(e))
           abort(500, "Unknown error occured")
    else:
        logging.error("No type parameter provided")
        abort(400, "Please provide a type parameter")

if __name__ == '__main__':
    app.run()
