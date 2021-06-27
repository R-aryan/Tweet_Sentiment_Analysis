from flask import Response
from flask_restful import Resource

from common.util.json import ComplexEncoder
from common.util.http_status import HttpStatus

import json


class Controller(Resource):

    @staticmethod
    def response_ok(data):
        return Response(json.dumps(data, cls=ComplexEncoder), status=HttpStatus.ok_200.value, mimetype="application/json")

    @staticmethod
    def response_error(message):
        return Response(message, status=HttpStatus.internal_server_error_500.value,
                        mimetype="application/json")

    @staticmethod
    def stream_response_ok(stream):
        return Response(stream, mimetype='multipart/x-mixed-replace; boundary=frame')
