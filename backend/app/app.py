from flask import Flask, request, jsonify 
from flask_cors import CORS
from database import supabase
import donors_route, organ_route, patient_route

app = Flask(__name__)
CORS(app)


app.register_blueprint(donors_route.bp)
app.register_blueprint(organ_route.bp)
app.register_blueprint(patient_route.bp)

@app.route('/api/add_patient', methods = ['POST'])
def add_organ():
    data = request.json 
    if not data or 'donor_id' not in data or 'organ' not in data or 'hospital_location' not in data:
        return jsonify({"error":"Missing requires fields"}), 400
    
    response = supabase.table('organs').insert([{
        "patient_id":None,
        "donor_id":data['donor_id'],
        "organ":data['organ'],
        "organ_condition":data['organ_condition'],
        "transplant_time":data['time_elapsed'],
        "hospital_location":data['hospital_location']
    }]).execute()

    if response.get("status_code") == 201:
        return jsonify({"message":"Organ added successfully"}), 201
    else:
        return jsonify({"error":"Failed to add organ"})
    
# @app.route('/api/get_organ_id', methods=['POST'])
# def get_organ_id():
#     data = request.json
#     if 'organ_id' in data:
#         return jsonify({"organ_id": data['organ_id']})
#     return jsonify({"error": "organ_id not provided"}), 400

@app.route('/api/get_organ_id/', methods=['POST'])
def get_organ_id():
    data = request.json
    if not data or 'organ_id' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    
    organ_id = data['organ_id']
    response = supabase.table('organs').select('*').eq('organ_id', organ_id).execute()
    
    if response.data:
        return jsonify(response.data[0])
    else:
        return jsonify({"error": "Organ not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)