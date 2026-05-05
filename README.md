# My_Zootopia_part2

A simple Python project that fetches animal data from an external API and generates a dynamic HTML webpage displaying animal information. Users can search for animals and filter them by skin type.


Features

- Fetches real-time animal data from an API
- Generates a styled HTML page automatically
- Filters animals by skin type
- Handles missing or invalid animal searches gracefully
- Separates data fetching logic from website generation


Project Structure

My-Zootopia2/
│
├── animals_web_generator.py   # Main program (HTML generator)
├── data_fetcher.py            # Handles API requests
├── animals_template.html      # HTML template file
├── requirements.txt           # Project dependencies
├── .env                       # API key (not included in Git)
├── .gitignore                 # Files ignored by Git


How It Works

1. User enters an animal name
2. Program fetches data from the API
3. If the animal exists:
- Available skin types are displayed
- User selects a filter or chooses "all"
4. HTML page is generated with animal cards
5. If no animal is found:
- A custom error message is displayed in the HTML page


Environment Variables

This project uses an API key stored securely in a .env file.
Create a .env file in the project root:
API_KEY=your_api_key_here
- Never commit this file to GitHub.


Installation - use the terminal 'Bash'

1. Clone the repository:
git clone <repo-url>
cd My-Zootopia2

2. Create a virtual environment:
python -m venv .venv
source .venv/bin/activate   # Mac/Linux

3. Install dependencies:
pip install -r requirements.txt

4. ▶️ Running the Project
python animals_web_generator.py

   
Requirements

- Python 3.8+
- requests
- python-dotenv


Learning Purpose

This project demonstrates:
. API integration in Python
. Separation of concerns (data vs presentation)
. Basic web content generation
. Environment variable usage for security
. Clean project structuring


Security Notes
- API keys are stored in .env
- .env is excluded via .gitignore
- Sensitive data is never pushed to GitHub


Future Improvements
- Add more animal filters (diet, habitat, etc.)
- Improve HTML styling with CSS framework
- Convert into a Flask web application
- Add caching for API requests


Author

Created by José Miguel Rocha Ramos
Learning Python and building small real-world projects