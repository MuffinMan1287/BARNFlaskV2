""" database dependencies to support sqliteDB examples """
from random import randrange
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError


''' Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along '''

# Define the Post class to manage actions in 'posts' table,  with a relationship to 'users' table
class Post(db.Model):
    __tablename__ = 'posts'

    # Define the Notes schema
    id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    note = db.Column(db.Text, unique=False, nullable=False)
    image = db.Column(db.String, unique=False)
    # Define a relationship in Notes Schema to userID who originates the note, many-to-one (many notes to one user)

    # Constructor of a Notes object, initializes of instance variables within object


    # Returns a string representation of the Notes object, similar to java toString()
    # returns string

    # CRUD create, adds a new record to the Notes table
    # returns the object added or None in case of an error


# Define the User class to manage actions in the 'users' table
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) User represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Player(db.Model):
    __tablename__ = 'favplayes'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _user = db.Column(db.String(255), unique=False, nullable=False)
    _player = db.Column(db.String(255), unique=False, nullable=False)
    _position = db.Column(db.String(255), unique=False, nullable=False)
    _team = db.Column(db.String(255), unique=False, nullable=False)
    _league = db.Column(db.String(255), unique=False, nullable=False)

    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, user, player, position, team, league):
        self._user = user    # variables with self prefix become part of the object, 
        self._player = player
        self._position = position
        self._team = team
        self._league = league

    # a name getter method, extracts name from object
    @property
    def user(self):
        return self._user
    
    # a setter function, allows name to be updated after initial object creation
    @user.setter
    def user(self, user):
        self._user = user
    
    @property
    def player(self):
        return self._player
    
    # a setter function, allows name to be updated after initial object creation
    @player.setter
    def player(self, player):
        self._player = player

    @property
    def position(self):
        return self._position
    
    # a setter function, allows name to be updated after initial object creation
    @position.setter
    def position(self, position):
        self._position = position

    @property
    def team(self):
        return self._team
    
    # a setter function, allows name to be updated after initial object creation
    @team.setter
    def team(self, team):
        self._team = team

    @property
    def league(self):
        return self._league
    
    # a setter function, allows name to be updated after initial object creation
    @league.setter
    def league(self, league):
        self._tds = league

    # output content using str(object) in human readable form, uses getter
    # output content using json dumps, this is ready for API response
    def __str__(self):
        return json.dumps(self.read())

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "id": self.id,
            "user" : self.user,
            "player" : self.player,
            "position" : self.position,
            "team" : self.team,
            "league": self.league
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, user, player, position, team, league):
        """only updates values with length"""
        if len(user) > 0:
            self.user = user
        if len(player) > 0:
            self.player = player
        if len(position) > 0:
            self.position = position
        if len(team) > 0:
            self.team = team
        if len(league) > 0:
            self.league = league
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing """


# Builds working data for testing
def initPlayers():
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        """Tester data for table"""
        p1 = Player(user='joe', player='Joe Burrow', position='qb', team='bengals', league='nfl')

        pyers = [p1]
        for pyer in pyers:
            try:
                pyer.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {pyer.name}")