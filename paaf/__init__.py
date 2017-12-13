from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

import dbconfig

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'\
    .format(dbconfig.db_user,
            dbconfig.db_password,
            dbconfig.db_hostname,
            dbconfig.db_name)

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

SQLALCHEMY_BINDS={}
SQLALCHEMY_BINDS['paaf']='mysql+pymysql://{}:{}@{}/{}'\
    .format(dbconfig.db_user,
            dbconfig.db_password,
            dbconfig.db_hostname,
            dbconfig.db_name)

SQLALCHEMY_BINDS['iaas']='mysql+pymysql://{}:{}@{}/{}'\
    .format(dbconfig.db_user,
            dbconfig.db_password,
            dbconfig.db_hostname,
            'iaas')
app.config['SQLALCHEMY_BINDS'] =SQLALCHEMY_BINDS

db = SQLAlchemy(app)



from flask_admin.contrib.sqla import ModelView
from models import asset, asset_value_domain_attributes, value_generating_practice, value_domain, park,park_asset

# Flask and Flask-SQLAlchemy initialization here

admin = Admin(app, name='PAAF', template_mode='bootstrap3')

admin.add_view(ModelView(asset_value_domain_attributes, db.session))
admin.add_view(ModelView(park, db.session))

class MyModelView(ModelView):
    column_list = ('id','name', 'description','parent_id','parent','children')
    column_display_pk = True
admin.add_view(MyModelView(asset, db.session))
admin.add_view(MyModelView(value_generating_practice, db.session))
admin.add_view(MyModelView(value_domain, db.session))
class MyParkAssetView(ModelView):
    column_list = ('id','park_id', 'park','asset','asset_id','description')
    column_display_pk = True
admin.add_view(MyParkAssetView(park_asset, db.session))


import views
import filters
import plugin_filters
import models
import logger


from paaf.plugins import load_plugins

load_plugins()


