from flask import Blueprint
from app.controllers import leads_controller

bp = Blueprint("leads", __name__, url_prefix="/leads")

bp.get("")(leads_controller.select_all)

bp.post("")(leads_controller.create)

bp.patch("")(leads_controller.update)

bp.delete("")(leads_controller.delete)
