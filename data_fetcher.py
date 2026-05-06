import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')

def fetch_data(animal_name):
    """
    Fetch animal data from the external API based on a given name.

    Sends a GET request to the API Ninjas animals endpoint using the provided
    animal name and API key loaded from environment variables.

    Args:
        animal_name (str): Name of the animal to search for.

    Returns:
        list[dict]: A list of animal data dictionaries returned by the API.
                    Returns an empty list if the request fails or no data is found.

    Side Effects:
        Prints an error message if the API request is unsuccessful.
    """
    url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}&X-Api-Key={API_KEY}'
    response = requests.get(url, timeout=15)

    if response.status_code != 200:
        print("Error fetching data from API")
        return[]

    return response.json()