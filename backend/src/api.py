import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
db_drop_and_create_all()


# ROUTES
@app.route('/drinks')
def drinks():
    try:
        drinks = Drink.query.all()
        drinks_formatted = [drink.short() for drink in drinks]

        return jsonify({
            'success': True,
            'drinks': drinks_formatted
        })
    except:
        abort(400)


@app.route('/drinks-detail')
@requires_auth('get:drinks-detail')
def get_drinks_detail(payload):
    try:
        drinks = Drink.query.all()
        drinks_formatted = [drink.long() for drink in drinks]

        return jsonify({
            'success': True,
            'drinks': drinks_formatted
        })

    except:
        abort(400)


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def post_drinks_detail(payload):
    try:
        body = request.get_json()
        req_title = body.get('title', None)
        req_recipe = body.get('recipe', None)
        drink = Drink(title=req_title, recipe=json.dumps(req_recipe))
        drink.insert()
        drinks = Drink.query.all()
        drinks_formatted = [drink.long() for drink in drinks]

        return jsonify({
            'success': True,
            'drinks': drinks_formatted
        })

    except:
        abort(400)


@app.route('/drinks/<int:id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drinks(payload, id):
    try:
        drink = Drink.query.filter(Drink.id == id).one_or_none()
        if drink is None:
            return json.dumps({
                'success': False,
                'error': 'Drink #' + id + ' not found to be edited'
            }), 404

        drink.delete()
        drinks = Drink.query.all()
        drinks_formatted = [drink.long() for drink in drinks]

        return jsonify({
            'success': True,
            'drinks': drinks_formatted
        })
    except:
        abort(400)


@app.route('/drinks/<int:id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def patch_drinks(payload, id):
    try:
        body = request.get_json()
        req_title = body.get('title', None)
        req_recipe = body.get('recipe', None)

        drink = Drink.query.filter(Drink.id == id).one_or_none()
        if drink is None:
            return json.dumps({
                'success': False,
                'error': 'Drink #' + id + ' not found to be edited'
            }), 404

        if req_title is not None:
            drink.title = req_title
        if req_recipe is not None:
            drink.recipe = req_recipe
        drink.update()
        drinks = Drink.query.all()
        drinks_formatted = [drink.long() for drink in drinks]

        return jsonify({
            'success': True,
            'drinks': drinks_formatted
        })

    except:
        abort(400)


# Error Handling
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
                    "success": False,
                    "error": 422,
                    "message": "unprocessable"
                    }), 422


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400
