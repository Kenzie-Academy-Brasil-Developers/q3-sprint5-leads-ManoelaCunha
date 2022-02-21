from http import HTTPStatus
from app.models.leads_model import LeadsModel
from flask import request, current_app, jsonify

from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation

def select_all():
    pass

def create():
    try:
        data = request.get_json()
        
        lead = LeadsModel(**data)
        
        current_app.db.session.add(lead)
        current_app.db.session.commit()
     
        return jsonify(lead), HTTPStatus.CREATED

    except ValueError as e:
        return dict(error=''.join(e.args)), HTTPStatus.BAD_REQUEST

    except KeyError as e:
        return dict(error=f"Missing key '{e.args[0]}'"), HTTPStatus.BAD_REQUEST

    except (AttributeError, TypeError):
        return dict(error='The value must be a string!'), HTTPStatus.BAD_REQUEST

    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation):
            return dict(error=' '.join(e.orig.pgerror.split()[9:])), HTTPStatus.CONFLICT
