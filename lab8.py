import requests
import random
import json

class Episode:
    def __init__(self, id, name, air_date, episode, characters):
        self.id = id
        self.name = name
        self.air_date = air_date
        self.episode = episode
        self.characters = characters

    def display_info(self):
        print(f"Episode {self.episode}: {self.name} ({self.air_date})")
        print(f"Characters: {', '.join(self.characters)}\n")

class Character:
    def __init__(self, id, name, status, species, gender, origin, location, image, **kwargs):
        self.id = id
        self.name = name
        self.status = status
        self.species = species
        self.gender = gender
        self.origin = origin
        self.location = location
        self.image = image

        # Process any additional attributes
        for key, value in kwargs.items():
            setattr(self, key, value)

    def display_info(self):
        print(f"{self.name} ({self.species}) - {self.status}")
        print(f"Gender: {self.gender}")
        print(f"Origin: {self.origin}")
        print(f"Location: {self.location}")
        print(f"Image: {self.image}\n")

def initialize_module():
    with open("__init__.py", "w") as init_file:
        init_file.write("# Initialization file for the module")

def get_random_character():
    random_character_id = random.randint(1, 826)
    character_url = f'https://rickandmortyapi.com/api/character/{random_character_id}'
    character_response = requests.get(character_url).json()
    return Character(**character_response)

def main():
    # Initialize module
    initialize_module()

    # Task 2 - Get random character
    random_character = get_random_character()

    # Display character information
    random_character.display_info()

if __name__ == "__main__":
    main()
