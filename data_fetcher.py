import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')

def fetch_data(animal_name):

    url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}&X-Api-Key={API_KEY}'
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching data from API")
        return[]

    return response.json()