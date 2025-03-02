from flask import Blueprint, jsonify
from database import supabase

bp = Blueprint('organs', __name__, url_prefix='/api/organs')

@bp.route('/', methods=['GET'])
def get_all_organs():
    response = supabase.table('organs').select('*').execute()
    return jsonify(response.data)

@bp.route('/<int:user_id>', methods=['GET'])
def get_organ(user_id):
    response = supabase.table('organs').select('*').eq('id', user_id).execute()
    if response.data:
        return jsonify(response.data[0])
    return jsonify({"error": "User not found"}), 404