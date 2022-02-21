from flask import Blueprint
from app.controllers import leads_controller

bp = Blueprint("leads", __name__, url_prefix="/leads")

bp.post("")(leads_controller.create)
