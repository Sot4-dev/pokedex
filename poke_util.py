import config
def help():
    print("情報を知りたいポケモンのidを入力してください。")
    print(f"{config.MAX_POKEDEX_NUNBER}以下は通常のポケモン図鑑番号です。")
    print(f"{config.MAX_POKEDEX_NUNBER}以上{config.FORM_DATA_START-1}以下は空白です。")
    print(f"フォルムチェンジなどの情報は{config.FORM_DATA_START}以上にあります。")
    print()
    print(f"{config.HELP_KEY}を入力すると、この文章を再表示します")
    print(f"{config.EXIT_KEY}を入力するとプログラムを終了します。")
    return

def get_type(pokemon_data):
    type_data=pokemon_data['types']
    types=[config.TYPE_DICT[type_entry['type']['name']] for type_entry in type_data]
    return " ".join(types)
    