from flask import jsonify, make_response, request, abort
from app_main import db
from flask import current_app as app
from models.CDR import Cdr


@app.route('/save', methods=['POST'])
def save_cdr():
    if request.json and 'origin_num' in request.json and 'termi_num' in request.json and 'call_duration' in request.json:
        json = request.json
        cdr = Cdr(origin_num=json.get('origin_num'), termi_num=json.get(
            'termi_num'), call_duration=json.get('call_duration'))
        db.session.add(cdr)
        db.session.commit()
        return make_response({'cdrId': cdr.id}, 201)
    else:
        abort(400, description="Request body is invalid")


@app.route('/', methods=['GET'])
def get_all_cdrs():
    cdrs = Cdr.query.all()
    return make_response({'cdrs': cdrs}, 200)


@app.route('/cdr/<id>', methods=['GET', 'DELETE'])
def get_or_delete_cdr(id):
    # TODO: Implement id validation

    if request.method == 'GET':
        cdr = Cdr.query.get(int(id))
        return jsonify({'cdr': cdr})
    else:
        isDeleted = Cdr.query.filter_by(id=id).delete()
        db.session.commit()
        return jsonify({'deleted': isDeleted})
