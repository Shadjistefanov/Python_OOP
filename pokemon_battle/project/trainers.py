from project.pokemon import Pokemon
# from typing import List

class Trainer:

    name: str
    pokemon: List[Pokemon]

    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f'Caught {pokemon.pokemon_details()}'

        return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        pokemon_list = [poks.name for poks in self.pokemon]

        if pokemon_name not in pokemon_list:
            return f"Pokemon is not caught"

        del self.pokemon[pokemon_name.index(pokemon_name)] # TODO
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        trainer_info = [
            f'Pokemon Trainer {self.name}'
            f'Pokemon count {len(self.pokemon)}'
        ]
        pokemon_info = [f'- {p.pokemon_details()}' for p in self.pokemon]
        return '\n'.join(trainer_info + pokemon_info) + "\n"



# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
