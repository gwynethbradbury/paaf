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


# class asset_asset_types(db.Model):
#     __bind_key__ = 'paaf'
#     id = db.Column(db.Integer, primary_key=True)
#     asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'))
#     asset_type_id = db.Column(db.Integer, db.ForeignKey('asset_type.id'))
#
#     def __init__(self, asset_id, asset_type_id):
#         self.asset_id = asset_id
#         self.asset_type_id = asset_type_id
#
# class asset_asset_vgps(db.Model):
#     __bind_key__ = 'paaf'
#     id = db.Column(db.Integer, primary_key=True)
#     asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'))
#     asset_vgp_id = db.Column(db.Integer, db.ForeignKey('asset_value_generating_practice.id'))
#
#     def __init__(self, asset_id, asset_vgp_id):
#         self.asset_id = asset_id
#         self.asset_vgp_id = asset_vgp_id




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
        pa = park_asset.query.filter_by(asset_id=asset_id,park_id=self.id).all()
        if pa.__len__()>0:
            d=pa[0].description
        return pa.__len__()>0,d

    def __init__(self,name="",desc=""):
        self.name=name
        self.description=desc

    def __repr__(self):
        return self.name

# "monkey-patched" because you cannot make self-references within a class definition.
asset.parent_id = db.Column(db.Integer, db.ForeignKey(asset.id))
asset.parent = relationship(asset, backref='children',
                            remote_side=asset.id)

value_generating_practice.parent_id = db.Column(db.Integer, db.ForeignKey(value_generating_practice.id))
value_generating_practice.parent = relationship(value_generating_practice, backref='children',
                                                remote_side=value_generating_practice.id)

value_domain.parent_id = db.Column(db.Integer, db.ForeignKey(value_domain.id))
value_domain.parent = relationship(value_domain, backref='children',
                                   remote_side=value_domain.id)



class survey():
    inputter_id=0


    def asset_heads(self):
        return asset.query.filter_by(parent=None).all()
    def practice_heads(self):
        return value_generating_practice.query.filter_by(parent=None).all()
    def value_heads(self):
        return value_domain.query.filter_by(parent=None).all()
# class Service(db.Model):
#     __bind_key__ = 'it_monitor_app'
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(70))
#     status = db.Column(db.Integer,default=1) #1: down; 3: runnng; 2: running but some problem identified
#
#     def __init__(self,name="no name",status=3):
#         self.name=name
#         self.status=status
#
#     def status_style(self):
#         if self.status==3:
#             return 'btn-success'
#         if self.status==1:
#             return 'btn-danger'
#         return 'btn-warning'
#
#     def status_content(self):
#         if self.status==3:
#             return 'OK'
#         if self.status==1:
#             return 'Not OK'
#         return 'Status Unknown'
#
# class wol_computer(db.Model):
#     __bind_key__ = 'it_monitor_app'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(8))
#     computer = db.Column(db.String(20))
#
#     def __init__(self,username="unknown",computer="unknown"):
#         self.username=username
#         self.computer=computer
#
#     def get_status(self):
#         return self.is_awake()
#
#     def status_style(self):
#         if self.get_status() == 3:
#             return 'btn-success'
#         if self.get_status() == 1:
#             return 'btn-danger'
#         return 'btn-warning'
#
#
#     def wake_on_lan(self,uid):
#         if uid == self.username:
#             if is_debug:
#                 return 3,"debug version"
#
#             call(["/usr/local/bin/wol_by_name", self.computer])
#
#             r = self.is_awake()
#             if r==1:
#                 return r, "{} is still asleep.".format(self.computer)
#             elif r==3:
#                 return r, "{} is awake!".format(self.computer)
#             else:
#                 return r, "Something went wrong.."
#
#
#
#         return self.is_awake()
#
#
#     def do_remotedesktop(self):
#         pass
#
#     def is_awake(self):
#         if is_debug:
#             return 3
#
#         r = check_output(["/usr/local/bin/is_up", self.computer])
#         rr = r.split('\n')
#         if rr[0] == 'up':
#             return 3
#         elif rr[0] == 'down':
#             return 1
#         return 2
#
#     def get_guac_id(self):
#         if is_debug:
#             return str(1)
#
#         dbe = DBEngine(db='mysql+pymysql://{}:{}@{}/{}' \
#                     .format(dbconfig.db_user,
#                             dbconfig.db_password,
#                             dbconfig.db_hostname,
#                             'guac'))
#         r = dbe.E.execute("SELECT connection_id from guacamole_connection where connection_name='{}';".format(self.computer))
#         r=r.fetchone()
#         return str(r[0])
#
#
# class user_license(db.Model):
#     __bind_key__ = 'it_monitor_app'
#     id = db.Column(db.Integer, primary_key=True)
#     software_user_id = db.Column(db.Integer, db.ForeignKey('software_user.id'))
#     software_id = db.Column(db.Integer, db.ForeignKey('software.id'))
#
#     def __init__(self,software_user_id,software_id):
#         self.software_user_id = software_user_id
#         self.software_id = software_id
#
#
# class software(db.Model):
#     __bind_key__ = 'it_monitor_app'
#     id = db.Column(db.Integer, primary_key=True)
#     software_name = db.Column(db.String(70))
#     link=db.Column(db.String(100))
#     downloadlink=db.Column(db.String(100))
#     license=db.Column(db.Text())
#     #admin
#     license_expires=db.Column(db.Boolean,default=True)#is this a perpetual license
#     license_expiry_date=db.Column(db.DateTime)# when does the software license expire
#     license_renewal_date=db.Column(db.DateTime)# when does the software need to be renewed (sometimes before the exp date - this is for IT mgmt)
#     owner=db.Column(db.String(100), default="IT")# who owns the license? group or school?
#     count=db.Column(db.Integer,default=-1)#also determines type (site vs count)
#     explicit_approval_required=db.Column(db.Boolean,default=True)#true - generate support request, false - generate download link on mirror.ouce
#
#
#     users = relationship("software_user",
#                     secondary=user_license.__table__,
#                     backref="softwares")
#
#     def __init__(self, sw_name,link="#",downloadlink="#", license="no license text",lexpires=True,
#                  lexpiry=datetime.datetime.utcnow() + datetime.timedelta(days=(365)),
#                  lrenew=datetime.datetime.utcnow() + datetime.timedelta(days=(365)),
#                  owner="IT",count=-1,approve=False):
#         self.software_name=sw_name
#         self.link=link
#         self.downloadlink=downloadlink
#         self.license=license
#         self.license_expires = lexpires
#         self.license_expiry_date= lexpiry
#         self.license_renewal_date = lrenew
#         self.owner = owner
#         self.count = count
#         self.explicit_approval_required = approve
#
#     def accepted_by_user(self,user):
#         if user in self.users:
#             return True
#         return False
#
#     def is_available(self):
#         pass
#
#     def licence_type(self):
#         if self.count<0:
#             return 'site license'
#         else:
#             return '{} licenses avilable for this software'.format(self.count)
#
#     def __str__(self):
#         return 'id: {},\n' \
#                'software_name: {},\n' \
#                'link: {},\n' \
#                'downloadlink: {},\n' \
#                'license: {},\n' \
#                'ADMIN INFO:\n' \
#                'license_expires: {},\n' \
#                'license_expiry_date: {},\n' \
#                'license_renewal_date: {},\n' \
#                'owner: {},\n' \
#                'count: {},\n' \
#                'explicit_approval_required'.format(self.id ,self.software_name ,self.link,self.downloadlink,self.license,
#                                                    self.license_expires,self.license_expiry_date,self.license_renewal_date,self.owner,self.count,self.explicit_approval_required)
#
#
# class software_user(db.Model):
#     __bind_key__ = 'it_monitor_app'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(8),unique=True)
#
#     def __init__(self,username="unknown"):
#         self.username = username
#
#
#
