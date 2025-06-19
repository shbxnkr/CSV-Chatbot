import requests

BASE_URL = 'http://127.0.0.1:5000'

csv_path = csv_path = r'C:\Users\shobh\OneDrive\Desktop\csv chatbot\country.csv' 

load_response = requests.post(f'{BASE_URL}/load_csv', json={'csv_path': csv_path})
print("Load CSV response:", load_response.json())


question = "What is the capital of France?"

ask_response = requests.post(f'{BASE_URL}/ask', json={'question': question})
print("Ask question response:", ask_response.json())
