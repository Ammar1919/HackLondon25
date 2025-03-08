from flask import Blueprint, jsonify
from database import supabase

bp = Blueprint('patients', __name__, url_prefix='/api/patients')

@bp.route('/', methods=['GET'])
def get_all_patients():
    response = supabase.table('patients').select('patient_id, age, gender, blood_type, health_conditions, prescriptions, hospital_location').execute()
    return jsonify(response.data)

@bp.route('/<int:user_id>', methods=['GET'])
def get_patient(user_id):
    response = supabase.table('patients').select('*').eq('id', user_id).execute()
    if response.data:
        return jsonify(response.data[0])
    return jsonify({"error": "User not found"}), 404
