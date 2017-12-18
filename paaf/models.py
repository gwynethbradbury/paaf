# from . import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import dbconfig
import pymysql

import sqlalchemy as SqlAl

from paaf import app, db
# paaf_app = Flask(__name__)
# paaf_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'\
#     .format(dbconfig.db_user,
#             dbconfig.db_password,
#             dbconfig.db_hostname,
#             dbconfig.db_name)
#
# paaf_app.secret_key = 'super secret key'
# paaf_app.config['SESSION_TYPE'] = 'filesystem'
#
# SQLALCHEMY_BINDS={'paaf':'mysql+pymysql://{}:{}@{}/{}'\
#     .format(dbconfig.db_user,
#             dbconfig.db_password,
#             dbconfig.db_hostname,
#             dbconfig.db_name)}
# paaf_app.config['SQLALCHEMY_BINDS'] =SQLALCHEMY_BINDS
#
# db = SQLAlchemy(paaf_app)






from enum import Enum
# from time import strftime

from sqlalchemy.orm import relationship
# import datetime
# from subprocess import check_output, call
# from dbconfig import debug as is_debug


class Quality(Enum):
    OUTSTANDINGN = 5
    GOOD = 4
    OKAY = 3
    UNREMARKABLE = 2
    DEGRADED = 1
class Status(Enum):
    GOOD = 1
    MODERATE = 2
    LIMITED = 3
    PASSIVE = 4
    PROTECTED_AND_NON_EXPLOITABLE = 5
    MISSING_AND_NEEDED = 6
class Governance(Enum):
    PA_UNIT = 1
    MUNICIPALITY = 2
    STATE = 3
    FEDERAL = 4
    MULTIPLE = 5

#stores survey rating
class asset_value_domain_attributes(db.Model):
    __bind_key__ = 'paaf'
    id = db.Column(db.Integer, primary_key=True)
    park_id = db.Column(db.Integer, db.ForeignKey('park.id'))
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'))
    value_domain_id = db.Column(db.Integer, db.ForeignKey('value_domain.id'))

    inputter_id = db.Column(db.Integer, nullable=False)#ID of whoever entered the survey (randomised)
    description = db.Column(db.String(70), nullable=True)
    asset_quality = db.Column(db.Integer, default=0)
    value_generating_status = db.Column(db.Integer, default=0)
    location_descriptor = db.Column(db.String(70), nullable=True)
    governance_competency = db.Column(db.Integer, default=0)

    def __init__(self, asset_id=None, value_domain_id=None,inputter_id=None,description="",asset_quality=0,value_generating_status=0,location_descriptor="",governance_competency=0):
        self.asset_id = asset_id
        self.value_domain_id = value_domain_id
        self.description=description
        self.asset_quality=asset_quality
        self.value_generating_status=value_generating_status
        self.location_descriptor=location_descriptor
        self.governance_competency = governance_competency
        self.inputter_id=inputter_id

class park_asset(db.Model):
    __bind_key__ = 'paaf'
    id = db.Column(db.Integer, primary_key=True)
    park_id = db.Column(db.Integer, db.ForeignKey('asset.id'))
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'))
    description = db.Column(db.Text)

    def __init__(self,park_id=None, asset_id=None,desc=""):
        self.park_id=park_id
        self.asset_id=asset_id
        self.description=desc


class park_domains_of_value(db.Model):
    __bind_key__ = 'paaf'
    id = db.Column(db.Integer, primary_key=True)
    park_id = db.Column(db.Integer, db.ForeignKey('asset.id'))
    asset_value_domain_id = db.Column(db.Integer, db.ForeignKey('asset.id'))
    description = db.Column(db.Text)

    def __init__(self, park_id=None, asset_value_domain_id=None,desc=""):
        self.park_id = park_id
        self.asset_value_domain_id = asset_value_domain_id
        self.description=desc


class park_vgps(db.Model):
    __bind_key__ = 'paaf'
    id = db.Column(db.Integer, primary_key=True)
    park_id = db.Column(db.Integer, db.ForeignKey('asset.id'))
    asset_vgp_id = db.Column(db.Integer, db.ForeignKey('asset.id'))
    description = db.Column(db.Text)

    def __init__(self, park_id=None, asset_vgp_id=None, desc=""):
        self.park_id = park_id
        self.asset_vgp_id = asset_vgp_id
        self.description=desc





class asset(db.Model):
    __bind_key__='paaf'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)

    def __init__(self,name="",description="",parent_id=None):
        self.name=name
        if not parent_id ==None:
            self.parent_id=parent_id
        self.description = description

    def __repr__(self):
        return self.name

    def kids(self):
        return self.children


class value_generating_practice(db.Model):
    __bind_key__='paaf'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)


    def __init__(self,name="",description="",parent_id=None):
        self.name=name
        if not parent_id ==None:
            self.parent_id=parent_id
        self.description = description

    def __repr__(self):
        return self.name

    def kids(self):
        return self.children


class value_domain(db.Model):
    __bind_key__='paaf'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)

    def __init__(self,name="",description="",parent_id=None):
        self.name=name
        if not parent_id ==None:
            self.parent_id=parent_id
        self.description = description

    def __repr__(self):
        return self.name

    def kids(self):
        return self.children



class park(db.Model):
    __bind_key__='paaf'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)


    def all_ratings(self):
        return asset_value_domain_attributes.query.filter_by(asset_id=self.id).all()

    def ratings_collected_by_inputter(self):
        return asset_value_domain_attributes.query.filter_by(asset_id=self.id).all()

    def has_asset(self,asset_id):
        d=""
        ass=asset.query.get_or_404(asset_id)
        pa = park_asset.query.filter_by(asset_id=ass.id,park_id=self.id).all()
        if pa.__len__()>0:
            return True

        r= False
        for c in ass.children:
            r = self.has_asset(c.id)
            if r:
                return True
        return False

    def has_vgp(self,asset_id):
        d=""
        ass=value_generating_practice.query.get_or_404(asset_id)
        pa = park_vgps.query.filter_by(asset_vgp_id=ass.id,park_id=self.id).all()
        if pa.__len__()>0:
            return True

        r= False
        for c in ass.children:
            r = self.has_vgp(c.id)
            if r:
                return True
        return False

    def has_domains_of_value(self,asset_id):
        d=""
        ass=value_domain.query.get_or_404(asset_id)
        pa = park_domains_of_value.query.filter_by(asset_value_domain_id=ass.id,park_id=self.id).all()
        if pa.__len__()>0:
            return True

        r= False
        for c in ass.children:
            r = self.has_domains_of_value(c.id)
            if r:
                return True
        return False

    def asset_desc(self,asset_id):
        d=""
        pa = park_asset.query.filter_by(asset_id=asset_id,park_id=self.id).all()
        if pa.__len__()>0:
            d=pa[0].description
        return d

    def vgp_desc(self,asset_id):
        d=""
        pa = park_vgps.query.filter_by(asset_vgp_id=asset_id,park_id=self.id).all()
        if pa.__len__()>0:
            d=pa[0].description
        return d

    def value_desc(self,asset_id):
        d=""
        pa = park_domains_of_value.query.filter_by(asset_value_domain_id=asset_id,park_id=self.id).all()
        if pa.__len__()>0:
            d=pa[0].description
        return d

    def __init__(self,name="",desc=""):
        self.name=name
        self.description=desc

    def __repr__(self):
        return self.name

    def survey(self):
        pas = park_asset.query.filter_by(park_id=self.id).all()
        return pas

# "monkey-patched" because you cannot make self-references within a class definition.
asset.parent_id = db.Column(db.Integer, db.ForeignKey(asset.id))
asset.parent = relationship(asset, backref='children',
                            remote_side=asset.id, lazy="noload" )

value_generating_practice.parent_id = db.Column(db.Integer, db.ForeignKey(value_generating_practice.id))
value_generating_practice.parent = relationship(value_generating_practice, backref='children',
                                                remote_side=value_generating_practice.id, lazy="noload")

value_domain.parent_id = db.Column(db.Integer, db.ForeignKey(value_domain.id))
value_domain.parent = relationship(value_domain, backref='children',
                                   remote_side=value_domain.id, lazy="noload")



class survey():
    inputter_id=0

    options=[]

    def asset_heads(self):
        return asset.query.filter_by(parent=None).all()
    def practice_heads(self):
        return value_generating_practice.query.filter_by(parent=None).all()
    def value_heads(self):
        return value_domain.query.filter_by(parent=None).all()

    def restrict(self, options=[]):
        self.options=options

    def __init__(self,uid=1):
        self.inputter_id=uid
