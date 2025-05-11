import requests
import json
from config import EXIT_KEY, HELP_KEY, MAX_POKEDEX_NUNBER, FORM_DATA_START
from poke_util import help, get_type 
help()

while True:
    pokemon_id_input = input()
    if pokemon_id_input.isdecimal():
        pokemon_id=int(pokemon_id_input)
        response=requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/")
        if response.status_code==200:
            pokemon_data=response.json()
            name=pokemon_data['name']
            height=pokemon_data['height']/10
            weight=pokemon_data['weight']/10
            poke_type=get_type(pokemon_data)
            print(f"名前:{name}")
            print(f"タイプ:{poke_type}")
            print(f"高さ:{height}m")
            print(f"重さ:{weight}kg")
        else:
            print("API問い合わせがエラーになりました")
    elif pokemon_id_input==EXIT_KEY:
        break
    elif pokemon_id_input==HELP_KEY:
        help()
    else:
        print("入力が不正です")
    print()
