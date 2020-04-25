from flask import current_app as app
from flask import jsonify

@app.errorhandler(400)
def request_body_not_valid(ex):
    return jsonify({'message': 'Request body is invalid'})