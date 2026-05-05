import requests

API_KEY = 'Nl4RW0pTDV134aCTQd7ofGHTstT3KJEW8Te148R4'

def fetch_data(animal_name):

    url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}&X-Api-Key={API_KEY}'
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching data from API")
        return[]

    return response.json()