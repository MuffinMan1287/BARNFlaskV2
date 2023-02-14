import json
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.users import User

user_api = Blueprint('user_api', __name__,
                   url_prefix='/api/users')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(user_api)
class UserAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            name = body.get('name')
            if name is None or len(name) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 210
            # validate uid
            
            atts = body.get('atts')
            if atts is None or len(atts) < 2:
                return {'message': f'Atts is missing, or is less than 2 characters'}, 210
            
            comps = body.get('comps')
            if comps is None or len(comps) < 2:
                return {'message': f'Comps is missing, or is less than 2 characters'}, 210

            yards = body.get('yards')
            if yards is None or len(yards) < 2:
                return {'message': f'Yards is missing, or is less than 2 characters'}, 210

            tds = body.get('tds')
            if tds is None:
                return {'message': f'TDs is missing, or is less than 2 characters'}, 210
            
            pimage = body.get('pimage')
            if pimage is None:
                return {'message': f'Image is missing, or is less than 2 characters'}, 210
            
            ''' #1: Key code block, setup USER OBJECT '''
            uo = User(name=name, 
                    atts=atts,
                    comps=comps,
                    yards=yards,
                    tds=tds,
                    pimage=pimage)
            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            qb = uo.create()
            # success returns json of user
            if qb:
                return jsonify(qb.read())
            # failure returns error
            return {'message': f'Processed {name}'}, 210

    class _Read(Resource):
        def get(self):
            qbs = User.query.all()    # read/extract all users from database
            json_ready = [qb.read() for qb in qbs]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')