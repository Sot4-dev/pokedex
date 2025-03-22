import requests
import json
max_pokedex_number=1025
form_data_start=10001
exit_key="end"
help_key="h"

type_dict={
    "grass" :"くさ",
    "fire"  :"ほのお",
    "water" :"みず",
    "flying":"ひこう",
    "poison":"どく",
    "steel" :"はがね",
    "ground":"じめん",
    "rock"  :"いわ",
    "dragon":"ドラゴン",
    "ghost" :"ゴースト",
    "normal":"ノーマル",
    "fighting":"かくとう",
    "psychic":"エスパー",
    "ice"   :"こおり",
    "electric":"でんき",
    "bug"   :"むし",
    "dark"  :"あく",
    "fairy" :"フェアリー"
}

def help():
    print("情報を知りたいポケモンのidを入力してください。")
    print(f"{max_pokedex_number}以下は通常のポケモン図鑑番号です。")
    print(f"{max_pokedex_number}以上{form_data_start-1}以下は空白です。")
    print(f"フォルムチェンジなどの情報は{form_data_start}以上にあります。")
    print()
    print(f"{help_key}を入力すると、この文章を再表示します")
    print(f"{exit_key}を入力するとプログラムを終了します。")
    return

def get_type(pokemon_data):
    type_data=pokemon_data['types']
    types=[type_dict[type_entry['type']['name']] for type_entry in type_data]
    return " ".join(types)
    

help()

while True:
    pokemon_id = input()
    if pokemon_id.isdecimal():
        pokemon_id=int(pokemon_id)
        response=requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/")
        if response.status_code==200:
            pokemon_data=response.json()
            name=pokemon_data['name']
            height=pokemon_data['height']/10
            weight=pokemon_data['weight']/10
            type=get_type(pokemon_data)
            print(f"名前:{name}")
            print(f"タイプ:{type}")
            print(f"高さ:{height}m")
            print(f"重さ:{weight}kg")
        else:
            print("API問い合わせがエラーになりました")
    elif pokemon_id==exit_key:
        break
    elif pokemon_id==help_key:
        help()
    else:
        print("入力が不正です")
    print()
