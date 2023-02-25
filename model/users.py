""" database dependencies to support sqliteDB examples """
from random import randrange
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError


''' Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along '''

# Define the Post class to manage actions in 'posts' table,  with a relationship to 'users' table
class Post(db.Model):
    __tablename__ = 'stats'

    # Define the Notes schema
    id = db.Column(db.Integer, db.ForeignKey('stats.id'), primary_key=True)
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
class User(db.Model):
    __tablename__ = 'qbstats'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(255), unique=False, nullable=False)
    _atts = db.Column(db.String(255), unique=False, nullable=False)
    _comps = db.Column(db.String(255), unique=False, nullable=False)
    _yards = db.Column(db.String(255), unique=False, nullable=False)
    _tds = db.Column(db.String(255), unique=False, nullable=False)
    _pimage = db.Column(db.String, unique=False)

    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, name, atts, comps, yards, tds, pimage):
        self._name = name    # variables with self prefix become part of the object, 
        self._atts = atts
        self._comps = comps
        self._yards = yards
        self._tds = tds
        self._pimage = pimage

    # a name getter method, extracts name from object
    @property
    def name(self):
        return self._name
    
    # a setter function, allows name to be updated after initial object creation
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def atts(self):
        return self._atts
    
    # a setter function, allows name to be updated after initial object creation
    @atts.setter
    def atts(self, atts):
        self._atts = atts

    @property
    def comps(self):
        return self._comps
    
    # a setter function, allows name to be updated after initial object creation
    @comps.setter
    def comps(self, comps):
        self._comps = comps

    @property
    def yards(self):
        return self._yards
    
    # a setter function, allows name to be updated after initial object creation
    @yards.setter
    def yards(self, yards):
        self._yards = yards

    @property
    def tds(self):
        return self._tds
    
    # a setter function, allows name to be updated after initial object creation
    @tds.setter
    def tds(self, tds):
        self._tds = tds

    @property
    def pimage(self):
        return self._pimage
    
    @pimage.setter
    def pimage(self, pimage):
        self._pimage = pimage
    
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
            "name" : self.name,
            "atts" : self.atts,
            "comps" : self.comps,
            "yards" : self.yards,
            "tds": self.tds,
            "pimage": self.pimage
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, name, atts, comps, yards, tds, pimage):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(atts) > 0:
            self.atts = atts
        if len(comps) > 0:
            self.comps = comps
        if len(yards) > 0:
            self.yards = yards
        if len(tds) > 0:
            self.tds = tds
        if len(pimage) > 0:
            self.pimage = pimage
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
def initUsers():
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        """Tester data for table"""
        p1 = User(name='Patrick Mahomes', atts='648', comps='435', yards='5250', tds='41', pimage='{{ site.baseurl }}/images/pm.png')
        p2 = User(name='Justin Herbert', atts='699', comps='477', yards='4739', tds='25', pimage='{{ site.baseurl }}/images/jh.png')
        p3 = User(name='Tom Brady', atts='733', comps='490', yards='4694', tds='25', pimage='{{ site.baseurl }}/images/tb.png')
        p4 = User(name='Kirk Cousins', atts='643', comps='424', yards='4547', tds='29', pimage='{{ site.baseurl }}/images/kc.png')
        p5 = User(name='Joe Burrow', atts='606', comps='414', yards='4475', tds='35', pimage='{{ site.baseurl }}/images/jb.png')
        p6 = User(name='Jared Goff', atts='587', comps='382', yards='4438', tds='29', pimage='{{ site.baseurl }}/images/jg.png')
        p7 = User(name='Josh Allen', atts='567', comps='359', yards='4283', tds='35', pimage='{{ site.baseurl }}/images/ja.png')
        p8 = User(name='Geno Smith', atts='572', comps='399', yards='4283', tds='30', pimage='{{ site.baseurl }}/images/gs.png')
        p9 = User(name='Trevor Lawrence', atts='584', comps='387', yards='4113', tds='25', pimage='{{ site.baseurl }}/images/tl.png')
        p10 = User(name='Jalen Hurts', atts='460', comps='306', yards='3701', tds='22', pimage='{{ site.baseurl }}/images/jhurts.png')
        qbs = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
        for qb in qbs:
            try:
                qb.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {qb.name}")