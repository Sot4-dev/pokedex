import requests
import json

pokemon_id = int(input())
response=requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/")
if response.status_code==200:
    pokemon_data=response.json()
    name=pokemon_data['name']
    height=pokemon_data['height']/10
    weight=pokemon_data['weight']/10
    print(f"名前:{name}")
    print(f"高さ:{height}m")
    print(f"重さ:{weight}kg")
else:
    print("error")
