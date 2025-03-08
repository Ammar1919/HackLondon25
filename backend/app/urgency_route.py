from flask import Blueprint, jsonify
from urgency import organ, urgent_patient as patient

bp = Blueprint('urgency', __name__, url_prefix='/api/urgency')

@bp.route('/patient', methods=['GET'])
def get_patient():
    return jsonify(patient)

@bp.route('/organ', methods=['GET'])
def get_organ():
    return jsonify(organ)


