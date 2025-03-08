import requests
import os
from openai import OpenAI
from dotenv import load_dotenv 
from supabase import create_client, Client
import json 
from database import supabase


load_dotenv()


#from config import OPENAI_API_KEY

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def fetch_organ_id():
    response = requests.post("http://localhost:5000/api/get_organ_id", json={})
    if response.status_code == 200:
        return response.json().get("organ_id")
    return None

# Get organ details
def get_organ(organ_id):
    response = supabase.table("organs").select("organ, organ_condition, transplant_time, hospital_location").eq("organ_id", organ_id).execute()
    
    if response.data:
        return response.data[0]
    else:
        return {"error": "Organ not found"}

# Fetch organ_id first
organ_id = fetch_organ_id()
if organ_id:
    organ = get_organ(organ_id)
else:
    print("Organ not found")

patients = (
    supabase.table("patients")
    .select("age", "health_conditions", "habits", "hospital_location")
    .execute()
)

prompt = f"Calculate the urgency of each patient in {patients} in needing a {organ} transplant. Give only the results in decimal from 0 to 1. If a patient does not need the transplant, give them an urgency of 0.0. Also prioritize how close the distance between hospital_location of the organ and the hospital_location of the patient is. Return only a python-parseable json list of lists without any tags, with key 'result', of patient_id and urgency rating for patients who's urgency scores is greater than 0.0"
length = 150

response = client.chat.completions.create(
    model="gpt-4o",
    messages = [
        {"role":"system","content":"You are a healthcare professional evaluating the urgency of different patients for organ transplant"},
        {"role":"user","content":prompt}
    ],
    response_format = {"type":"json_object"}
)

result = response.choices[0].message.content
urgent_list = json.loads(result)
urgent_list = urgent_list['result']
patient_id = urgent_list[0][0]
urgent_patient = supabase.table('patients').select('*').eq('patient_id', patient_id).execute()
