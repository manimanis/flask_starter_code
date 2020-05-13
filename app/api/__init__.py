from flask import Blueprint, jsonify

api = Blueprint('api', __name__)


@api.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type, accept, Authorization, true')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,POST,PATCH,DELETE,OPTIONS')
    return response


@api.route('/tests')
def api_tests():
    return jsonify({
        'success': True,
        'data': [i for i in range(5)]
    })
