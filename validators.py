import jsonschema
import hashlib

from flask import jsonify

import config

USER_POST = {
    'type': 'object',
    'properties':  {
        'name': {
            'type': 'string'
        },
        'password': {
            'type': 'string'
        },
        'email': {
            'type': 'string',
        }
    },
    'required' : ['name', 'password', 'email']
}

ADV_POST = {
    'type': 'object',
    'properties':  {
        'title': {
            'type': 'string'
        },
        'description': {
            'type': 'string'
        },
        'owner_id': {
            'type': 'integer'
        }
    },
    'required': ['title', 'owner_id']
}


def validate_user_post(request):
    data = request.json
    try:
        jsonschema.validate(data, schema=USER_POST)
        password = data['password']
        pass_hash = hashlib.md5(password.encode()).hexdigest() + config.SALT
        data['password'] = pass_hash
        return data
    except jsonschema.ValidationError as er:
        response = jsonify({'error': 'Ошибка ввода данных'})
        response.status_code = 400
        return response


def validate_adv_post(request):
    try:
        jsonschema.validate(request.json, schema=ADV_POST)
        return request
    except jsonschema.ValidationError as er:
        response = jsonify({'error': 'Ошибка ввода данных'})
        response.status_code = 400
        return response
