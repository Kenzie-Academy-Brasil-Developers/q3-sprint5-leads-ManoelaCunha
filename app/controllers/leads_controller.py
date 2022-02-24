from http import HTTPStatus
from datetime import datetime as dt
from flask import request, current_app, jsonify

from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError, NoResultFound

from psycopg2.errors import UniqueViolation

from app.models.leads_model import LeadsModel
from app.services.decorators import verify_keys

def select_all():
    base_query = current_app.db.session.query(LeadsModel).order_by(desc('visits'))
    leads = base_query.all()

    if not leads:
        return dict(error="Data not found!"), HTTPStatus.NOT_FOUND

    return jsonify(leads), HTTPStatus.OK

@verify_keys(['name', 'email', 'phone'])
def create():
    try:
        data = request.get_json()
        
        lead = LeadsModel(**data)
        
        current_app.db.session.add(lead)
        current_app.db.session.commit()
     
        return jsonify(lead), HTTPStatus.CREATED

    except ValueError as e:
        return dict(error=''.join(e.args)), HTTPStatus.BAD_REQUEST

    except (AttributeError, TypeError):
        return dict(error='The value must be a string!'), HTTPStatus.BAD_REQUEST

    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation):
            return dict(error=' '.join(e.orig.pgerror.split()[9:])), HTTPStatus.CONFLICT

@verify_keys(['email'])
def update():
    try:
        data = request.get_json()
        email = data['email'].lower()

        for key in data.keys():
            if key != 'email':
                raise KeyError
        
        base_query = current_app.db.session.query(LeadsModel)
        
        lead = base_query.filter_by(email=email).one()
        lead.last_visit = dt.now()
        lead.visits = lead.visits + 1
    
        for key, value in data.items():
            setattr(lead, key, value.lower())
        
        current_app.db.session.add(lead)
        current_app.db.session.commit()

        return jsonify(lead), HTTPStatus.NO_CONTENT

    except NoResultFound:
        return dict(error="email not found"), HTTPStatus.NOT_FOUND

    except AttributeError:
        return dict(error='The value must be a string!'), HTTPStatus.BAD_REQUEST

@verify_keys(['email'])
def delete():
    try:
        data = request.get_json()
        email = data['email'].lower()

        for key in data.keys():
            if key != 'email':
                raise KeyError
    
        base_query = current_app.db.session.query(LeadsModel)
            
        lead = base_query.filter_by(email=email).one()

        current_app.db.session.delete(lead)
        current_app.db.session.commit()

        return jsonify(lead), HTTPStatus.NO_CONTENT
    
    except NoResultFound:
        return dict(error="email not found"), HTTPStatus.NOT_FOUND

    except AttributeError:
        return dict(error='The value must be a string!'), HTTPStatus.BAD_REQUEST
