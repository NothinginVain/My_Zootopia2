import json
from data_fetcher import fetch_data


def load_html_template(file_path):
    """Read and return the full content of an HTML template file."""
    with open(file_path, "r", encoding="utf-8",) as file:
        content = file.read()
        return content


def serialize_animal(animal_obj):
    """Convert a single animal dictionary into an HTML list item string."""
    diet = animal_obj['characteristics'].get('diet', 'NA.')
    location = animal_obj['locations'][0]
    temperament = animal_obj['characteristics'].get('temperament', 'NA.').title()
    type_ = animal_obj['characteristics'].get('type', 'NA.').title()
    color = animal_obj['characteristics'].get('color', 'NA.').title()
    habitat = animal_obj['characteristics'].get('habitat', 'NA.').title()
    name = animal_obj["name"]

    animal_charact = {
        'Diet': diet,
        'Location': location,
        'Temperament': temperament,
        'Type': type_,
        'Color': color,
        'Habitat': habitat
    }

    update_animal_char = [
        f'<li class="animal-item"><strong>{key}: </strong>{value}</li>'
        for key, value in animal_charact.items() if value != 'Na.'
    ]
    animals_char_to_html = '\n'.join(update_animal_char)

    out_put = (
        f'<li class="cards__item">\n<div class="card__title">'
        f'{name}</div>\n<div class ="card__text">\n '
        f'<ul class="animal-list">\n'
        f'{animals_char_to_html}\n'
        f'</ul>\n'
        f'</div>\n'
        f'</li>\n'
    )

    return out_put


def get_animal_info(animals_data):
    """Build and return the HTML for all animals in the given list."""
    out_put = ''
    for animal in animals_data:
        out_put += serialize_animal(animal)
    return out_put


def update_animals_web(file_path, html_content, filtered_animal_info):
    """Insert animal HTML into the template and write the result to a file."""
    html_with_animal_list = html_content.replace(
        '__REPLACE_ANIMALS_INFO__',
        filtered_animal_info
    )
    with open(file_path, "w", encoding="utf-8") as new_file:
        new_file.write(html_with_animal_list)


def skin_type_filter(animals_data):
    """Return a set of unique skin types found in the animal data."""
    skin_type_set = set()
    for animal in animals_data:
        if animal['characteristics'].get('skin_type') is not None:
            skin_type_set.add(animal['characteristics']['skin_type'])
    return skin_type_set


def skin_type_print(animals_data, user_input):
    """Return a list of animals whose skin type matches the user's input."""
    skin_type_select = [
        animal for animal in animals_data
        if animal['characteristics'].get('skin_type') == user_input
    ]
    return skin_type_select


def generate_error_page(file_path, animal_name, html_content):
    error_html = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'
    update_animals_web(file_path, html_content, error_html)


def generate_page(file_path, html_content, animal_data):
    animal_info = get_animal_info(animal_data)
    update_animals_web(file_path, html_content, animal_info )


def main():
    """Load data, ask the user for a skin type, and generate the HTML page."""
    html_template = load_html_template('animals_template.html')

    animal_name = input('Type the animal name: ').title().strip()

    json_animal_data = fetch_data(animal_name)
    file_path = 'animals.html'

    if not json_animal_data:
        generate_error_page(file_path, animal_name, html_template)
        print("no animal found, HTML page generated with error message.")
        return

    skin_type_list = skin_type_filter(json_animal_data)
    print(list(skin_type_list))

    skin_choice = input('Type one of the skin type from the list or "all": ').title()

    if skin_choice == 'All':
        generate_page(file_path, html_template, json_animal_data)
        print("Website was successfully generated to the file animals.html.")

    elif skin_choice in skin_type_list:
        selected_animals = skin_type_print(json_animal_data, skin_choice)
        generate_page(file_path, html_template, selected_animals)
        print("Website was successfully generated to the file animals.html.")

    else:
        print('Typing was not correct, By by!')


if __name__ == "__main__":
    main()