import json
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.players import Player

player_api = Blueprint('player_api', __name__,
                   url_prefix='/api/players')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(player_api)

class PlayerAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            user = body.get('user')
            if user is None or len(user) < 2:
                return {'message': f'User is missing, or is less than 2 characters'}, 400
            # validate uid
            player = body.get('player')
            if player is None or len(player) < 2:
                return {'message': f'Player Name is missing, or is less than 2 characters'}, 400
            
            position = body.get('position')
            if position is None or len(position) < 2:
                return {'message': f'Position is missing, or is less than 2 characters'}, 400
            
            team = body.get('team')
            if team is None or len(team) < 2:
                return {'message': f'Team is missing, or is less than 2 characters'}, 400
            
            league = body.get('league')
            if league is None or len(league) < 2:
                return {'message': f'League is missing, or is less than 2 characters'}, 400
            
            # look for password and dob

            ''' #1: Key code block, setup USER OBJECT '''
            uo = Player(user=user, 
                      player=player,
                      position=position,
                      team=team,
                      league=league)
            
            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            fplayer = uo.create()
            # success returns json of user
            if fplayer:
                return jsonify(fplayer.read())
            # failure returns error
            return {'message': f'Processed {name}, either a format error or User ID {uid} is duplicate'}, 400

    class _Read(Resource):
        def get(self):
            fplayers = Player.query.all()    # read/extract all users from database
            json_ready = [fplayer.read() for fplayer in fplayers]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps
    


            

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')