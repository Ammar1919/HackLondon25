import sys
import os

# Add the directory containing config.py to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

import openai
from config import OPENAI_API_KEY

patients = {
    "patient 1": "55 Female Lung Cancer Cisplatin, Etoposide AB- Former smoker",
    "patient 2": "45 Male Kidney Disease Ramipril, Furosemide O+ Non-smoker",
    "patient 3": "60 Female Liver Cirrhosis Spironolactone, Propranolol A- Non-smoker, No alcohol"
}
organ = "liver"
prompt = f"Calculate the urgency of each patient in {patients} in needing a {organ} transplant. Give the results in decimal from 0 to 1. If a patient does not need the transplant, give them an urgency of 0.0"
length = 150

response = openai.ChatCompletion.create(
    model="gpt-4",
    prompt=prompt,
    max_tokens=length
)

print(response["choices"][0]["text"])