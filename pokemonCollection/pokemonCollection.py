def pokemonCollection(pokemons):
    pokedex = []
    for catch in pokemons:
        if catch not in pokedex:
            pokedex.append(catch)
    return 151 - len(pokedex)
