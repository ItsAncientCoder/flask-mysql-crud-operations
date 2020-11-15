from app_config import app, logger
from models import t_advance_search

from flask_negotiate import consumes, produces
from flask import jsonify, request, abort

@app.route('/savedSearches', methods=['GET'])
def getAllSavedSearchesByEmail():
    query_params = request.args;
    logger.info('Query Params: %s', query_params);

    email = query_params.get('email');
    
    if ((email is None) or (len(email) == 0)):
        msg = 'Please specify valid Email.';
        logger.error(msg);
        return jsonify({'message': msg}), 400;
    
    searches = t_advance_search.objects(email=email).all();
    logger.info('Successfully fetched all records for email=%s. Response size = %s', email, len(searches));
    searches = sorted(searches, key=lambda search: search.last_modified_time, reverse=True);
    return jsonify({'results': [search.toJson() for search in searches]});

@app.route('/savedSearch', methods=['GET'])
@produces('application/json')
def getSavedSearchByIdAndEmail():
    query_params = request.args;
    logger.info('Query Params: %s', query_params);

    id = query_params.get('id');
    email = query_params.get('email');
    
    if ((id is None) or (email is None)):
        msg = 'Please specify ' + ('Email' if id else 'Id') +' in the request.';
        logger.error(msg);
        return jsonify({'message': msg}), 400;
    
    try:
        savedSearch = t_advance_search.objects(id=id, email=email).first();
    except Exception as ex:
        logger.error(ex);
        return jsonify({'message': str(ex)}), 500;
    
    if savedSearch is None:
        logger.info('No record found for id=%s and email=%s', id, email);
        #return Response(status=404); # Another way to return response
        #abort(404, 'No Saved Search found.');
        return jsonify({'message': 'No records found.'}), 404;
    
    logger.info('Successfully fetched data by id=%s and email=%s. response = %s', id, email, savedSearch);
    return jsonify(savedSearch.toJson());

@app.route('/savedSearch/save', methods=['POST'])
@consumes('application/json')
# @produces('application/json')
def save_search():
    request_body = request.get_json();
    logger.info('Request Body: %s', request_body);
    
    if 'email' not in request_body.keys():
        msg = 'email is missing in the request body.';
        logger.error(msg);
        return jsonify({'message': msg}), 400;
    if 'search_name' not in request_body.keys():
        msg = 'search_name is missing in the request body.';
        logger.error(msg);
        return jsonify({'message': msg}), 400;
    if 'search_query' not in request_body.keys():
        msg = 'search_query is missing in the request body.';
        logger.error(msg);
        return jsonify({'message': msg}), 400;

    email = request_body.get('email');
    search_name = request_body.get('search_name');
    search_query = request_body.get('search_query');
        
    logger.info('Parsed data: email=%s, search_name=%s, search_query=%s', email, search_name, search_query);
    
    savedSearch = None;
    try:
        savedSearch = t_advance_search.create(email=email, search_query=search_query, search_name=search_name);
    except Exception as ex:
        logger.error(ex);
        return jsonify({'message': str(ex)}), 500;
    
    logger.info('Successfully saved the data.');
    return jsonify({'ID': savedSearch.id}), 201;

@app.route('/savedSearch/delete', methods=['DELETE'])
# @consumes('application/json')
# @produces('application/json')
def delete_saved_search():
    query_params = request.args;
    logger.info('Query Params: %s', query_params);
    
    id = query_params.get('id');
    email = query_params.get('email');
    
    if ((id is None) or (email is None)):
        msg = 'Please specify ' + ('Email' if id else 'Id') +' in the request.';
        logger.error(msg);
        return jsonify({'message': msg}), 400;
    
    savedSearch = None;
    
    try:
        savedSearch = t_advance_search.objects(id=id, email=email).first();

        if savedSearch is None:
            logger.info('No record found for id=%s and email=%s', id, email);
            return jsonify({'message': 'No records found.'}), 404;
        
        savedSearch.delete();
    except Exception as ex:
        logger.error(ex);
        return jsonify({'message': str(ex)}), 500;
    
    logger.info('Successfully deleted the record by id=%s and email=%s', savedSearch.id, savedSearch.email);
    return jsonify({'ID': savedSearch.id}), 204;