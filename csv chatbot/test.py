import requests
import json

csv_path = r'C:\Users\shobh\OneDrive\Desktop\csv chatbot\country.csv'
load_url = 'http://127.0.0.1:5000/load_csv' 
load_data = {"csv_path": csv_path}

load_response = requests.post(load_url, json=load_data)
print("Status Code:", load_response.status_code)
print("Raw Response:", load_response.text)

question = "What is the capital of France?"
ask_url = 'http://127.0.0.1:5000/ask'
ask_data = {"question": question}

ask_response = requests.post(ask_url, json=ask_data)
print("Answer:", ask_response.json())