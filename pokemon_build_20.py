
import requests as r

def build_poke(url):
     
     pokemon = r.get(url)
     if pokemon.status_code == 200:
          pokemon = pokemon.json()

     name = pokemon['name']
     abilities = pokemon['abilities'][0]['ability']['name']
     types = pokemon['types'][0]['type']['name']
     weight = pokemon['weight']
     ind_poke_dict = {}
     master_poke_dict = {}

     ind_poke_dict["name"] = name 
     ind_poke_dict["abilities"] = abilities 
     ind_poke_dict["types"] = types 
     ind_poke_dict["weight"] = weight 

     master_poke_dict[name] = ind_poke_dict
     print(master_poke_dict)

for n in range(1,21):
     output = build_poke(f'https://pokeapi.co/api/v2/pokemon/{n}')



# print(master_poke_dict)