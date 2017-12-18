from flask import render_template, request, redirect, url_for, abort, jsonify, flash, session, Response
from collections import defaultdict
from . import app, db
# from models import Status, Color, Service, software, software_user, user_license, wol_computer
from signals import task_created, mission_created
import time
# from paaf_app.auth.iaasldap import LDAPUser as LDAPUser

from threading import Lock
#from flask_socketio import SocketIO, emit, join_room, leave_room, \
#    close_room, rooms, disconnect
async_mode = None
import math

# current_user = LDAPUser()

from forms import SurveyForm, ParkForm, AssetForm

from models import park, park_asset, park_domains_of_value, park_vgps,\
    Status, Governance, Quality, survey as SurveyClass

@app.route('/pa/<park_id>', methods=["GET", "POST"])
def pa(park_id):
    p = park.query.get_or_404(park_id)
    return render_template('park/park.html',park=p)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_pa', methods=["GET", "POST"])
def add_park():
    form = ParkForm()
    if form.validate_on_submit():
        p = park(form.name.data,form.description.data)
        db.session.add(p)
        db.session.commit()
        return redirect('/admin/park/')
    return render_template('park/add_park.html',form=form)

@app.route('/add_pa_assets/<park_id>', methods=["GET", "POST"])
def add_pa_assets(park_id):
    form = AssetForm()
    pa_assets=[]
    rm_pa_assets=[]
    pa = park.query.get_or_404(park_id)
    if request.method == 'POST':

        for a in form.assets:#1
            for aa in a.kids():#1.1, 1.2
                if aa.kids().__len__()>0:
                    for aaa in aa.kids():#1.1.1, 1.1.2
                        p = request.form.get('{}'.format(aaa.id))
                        if pa.has_asset(aaa.id):
                            paa = park_asset.query.filter_by(park_id=park_id,asset_id=aaa.id).first()
                            if p==u'on':
                                d = request.form.get('{}_desc'.format(aaa.id))
                                paa.description = d
                                db.session.add(paa)
                            else:
                                db.session.delete(paa)
                        elif p == u'on':
                            d = request.form.get('{}_desc'.format(aaa.id))
                            pa_assets.append(park_asset(park_id=park_id, asset_id=aaa.id, desc=d))
                else:
                    p = request.form.get('{}'.format(aa.id))
                    if pa.has_asset(aa.id):
                        paa = park_asset.query.filter_by(park_id=park_id,asset_id=aa.id).first()
                        if p==u'on':
                            d = request.form.get('{}_desc'.format(aa.id))
                            paa.description = d
                            db.session.add(paa)
                        else:
                            db.session.delete(paa)
                    elif p==u'on':
                        d = request.form.get('{}_desc'.format(aaa.id))
                        pa_assets.append(park_asset(park_id=park_id,asset_id=aa.id,desc=d))

        for a in form.practice_heads:#1
            for aa in a.kids():#1.1, 1.2
                if aa.kids().__len__()>0:
                    for aaa in aa.kids():#1.1.1, 1.1.2
                        p = request.form.get('{}_vgp'.format(aaa.id))
                        if pa.has_vgp(aaa.id):
                            paa = park_domains_of_value.query.filter_by(park_id=park_id,asset_value_domain_id=aaa.id).first()
                            if p==u'on':
                                d = request.form.get('{}_vgp_desc'.format(aaa.id))
                                paa.description = d
                                db.session.add(paa)
                            else:
                                db.session.delete(paa)
                        elif p == u'on':
                            d = request.form.get('{}_vgp_desc'.format(aaa.id))
                            pa_assets.append(park_domains_of_value(park_id=park_id, asset_value_domain_id=aaa.id, desc=d))
                else:
                    p = request.form.get('{}_vgp'.format(aa.id))
                    if pa.has_vgp(aa.id):
                        paa = park_domains_of_value.query.filter_by(park_id=park_id,asset_value_domain_id=aa.id).first()
                        if p==u'on':
                            d = request.form.get('{}_vgp_desc'.format(aa.id))
                            paa.description = d
                            db.session.add(paa)
                        else:
                            db.session.delete(paa)
                    elif p==u'on':
                        d = request.form.get('{}_vgp_desc'.format(aaa.id))
                        pa_assets.append(park_domains_of_value(park_id=park_id,asset_value_domain_id=aa.id,desc=d))

        for a in form.value_heads:#1
            for aa in a.kids():#1.1, 1.2
                if aa.kids().__len__()>0:
                    for aaa in aa.kids():#1.1.1, 1.1.2
                        p = request.form.get('{}_domain'.format(aaa.id))
                        if pa.has_domains_of_value(aaa.id):
                            paa = park_domains_of_value.query.filter_by(park_id=park_id,asset_value_domain_id=aaa.id).first()
                            if p==u'on':
                                d = request.form.get('{}_domain_desc'.format(aaa.id))
                                paa.description = d
                                db.session.add(paa)
                            else:
                                db.session.delete(paa)
                        elif p == u'on':
                            d = request.form.get('{}_domain_desc'.format(aaa.id))
                            pa_assets.append(park_vgps(park_id=park_id, asset_value_domain_id=aaa.id, desc=d))
                else:
                    p = request.form.get('{}_domain'.format(aa.id))
                    if pa.has_domains_of_value(aa.id):
                        paa = park_domains_of_value.query.filter_by(park_id=park_id,asset_value_domain_id=aa.id).first()
                        if p==u'on':
                            d = request.form.get('{}_domain_desc'.format(aa.id))
                            paa.description = d
                            db.session.add(paa)
                        else:
                            db.session.delete(paa)
                    elif p==u'on':
                        d = request.form.get('{}_domain_desc'.format(aaa.id))
                        pa_assets.append(park_vgps(park_id=park_id,asset_value_domain_id=aa.id,desc=d))

        for pa_a in pa_assets:
            db.session.add(pa_a)
            db.session.commit()
        # return redirect('/admin/park/')
    s = SurveyClass()
    return render_template('park/add_assets_to_park.html',pa=pa,assets=s.asset_heads(),
                           practice_heads=s.practice_heads(),
                           value_heads=s.value_heads())


@app.route('/survey/<park_id>', methods=["GET", "POST"])
def survey(park_id=1):
    pa = park.query.get_or_404(park_id)
    pas = park_asset.query.filter_by(park_id=park_id).all()
    l=[]
    for p in pas:
        l.append(p.id)
    form = SurveyForm()
    form.survey.restrict(l)

    pa = park.query.get_or_404(park_id)

    return render_template('survey.html', form=form, qualities=Quality, statuses=Status, governances=Governance, pa=pa)


