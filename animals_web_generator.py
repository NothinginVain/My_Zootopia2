from data_fetcher import fetch_data


def load_html_template(file_path):
    """
    Load an HTML template file from disk.

    Args:
        file_path (str): Path to the HTML template file.

    Returns:
        str: The full content of the HTML file as a string.
    """
    with open(file_path, "r", encoding="utf-8",) as file:
        content = file.read()
        return content


def serialize_animal(animal_obj):
    """
    Convert a single animal dictionary into an HTML representation.

    Extracts relevant animal attributes (e.g., diet, habitat, color) and formats
    them into an HTML list item suitable for display in a card layout.

    Args:
        animal_obj (dict): Dictionary containing animal data, including
                           'name', 'locations', and 'characteristics'.

    Returns:
        str: HTML string representing the animal as a styled list item.
    """
    diet = animal_obj['characteristics'].get('diet', 'NA.')
    location = animal_obj.get['locations'][0]
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
    """
    Generate combined HTML for a list of animals.

    Iterates through the provided animal data and serializes each entry
    into HTML using `serialize_animal`.

    Args:
        animals_data (list[dict]): List of animal dictionaries.

    Returns:
        str: Concatenated HTML string for all animals.
    """
    out_put = ''
    for animal in animals_data:
        out_put += serialize_animal(animal)
    return out_put


def update_animals_web(file_path, html_content, filtered_animal_info):
    """
    Insert animal HTML into a template and write the result to a file.

    Replaces the placeholder string '__REPLACE_ANIMALS_INFO__' in the template
    with the provided animal HTML content, then writes the updated HTML to disk.

    Args:
        file_path (str): Output file path for the generated HTML page.
        html_content (str): Original HTML template content.
        filtered_animal_info (str): HTML string containing animal data.

    Returns:
        None
    """
    html_with_animal_list = html_content.replace(
        '__REPLACE_ANIMALS_INFO__',
        filtered_animal_info
    )
    with open(file_path, "w", encoding="utf-8") as new_file:
        new_file.write(html_with_animal_list)


def skin_type_filter(animals_data):
    """
    Extract unique skin types from animal data.

    Iterates through all animals and collects distinct 'skin_type' values
    found in their characteristics.

    Args:
        animals_data (list[dict]): List of animal dictionaries.

    Returns:
        set: A set of unique skin types.
    """
    skin_type_set = set()
    for animal in animals_data:
        if animal['characteristics'].get('skin_type') is not None:
            skin_type_set.add(animal['characteristics']['skin_type'])
    return skin_type_set


def skin_type_print(animals_data, user_input):
    """
    Filter animals by a specific skin type.

    Selects and returns animals whose 'skin_type' matches the user's input.

    Args:
        animals_data (list[dict]): List of animal dictionaries.
        user_input (str): Desired skin type to filter by.

    Returns:
        list[dict]: List of animals matching the specified skin type.
    """
    skin_type_select = [
        animal for animal in animals_data
        if animal['characteristics'].get('skin_type') == user_input
    ]
    return skin_type_select


def generate_error_page(file_path, animal_name, html_content):
    """
    Generate an error HTML page when no animal data is found.

    Creates a simple error message and injects it into the HTML template.

    Args:
        file_path (str): Output file path for the HTML page.
        animal_name (str): Name of the animal requested by the user.
        html_content (str): HTML template content.

    Returns:
        None
    """
    error_html = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'
    update_animals_web(file_path, html_content, error_html)


def generate_page(file_path, html_content, animal_data):
    """
    Generate a complete HTML page with animal data.

    Converts animal data into HTML and inserts it into the template.

    Args:
        file_path (str): Output file path for the HTML page.
        html_content (str): HTML template content.
        animal_data (list[dict]): List of animal dictionaries.

    Returns:
        None
    """
    animal_info = get_animal_info(animal_data)
    update_animals_web(file_path, html_content, animal_info )


def main():
    """
    Main program flow.

    - Loads the HTML template
    - Prompts the user for an animal name
    - Fetches animal data from an external source
    - Allows filtering by skin type
    - Generates an HTML page with results or an error message

    Returns:
        None
    """
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