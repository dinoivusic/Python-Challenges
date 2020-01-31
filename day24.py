#One line solution
def cakes(recipe, available):
  return min(available.get(k, 0)/recipe[k] for k in recipe)


#Longer way of solving it
def cakes(recipe, available):
    new = []
    shared = set(recipe.keys() & set(available.keys()))
    if not len(shared) == len(recipe.keys()) and len(shared) == len(available.keys()):
        print('Not all keys are shared')
    if len(recipe.keys()) > len(available.keys()):
        return 0
    for key in available.keys():
        if key in recipe.keys():
            res = available[key]//recipe[key]
            new.append(res)
    return sorted(new)[0]