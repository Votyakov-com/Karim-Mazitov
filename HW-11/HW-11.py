recursive_salad = []
recursive_salad.append('lettuce')
recursive_salad.append('chiken')
recursive_salad.append('cheese')
recursive_salad.append('sauce')
recursive_salad.append('tomatoes')
recursive_salad.append('croutons')
recursive_salad.append(recursive_salad)
salad1 = recursive_salad.copy()
recursive_salad[6].append("salt")
recursive_salad[6].append("pepper")
print(salad1[-1][-3][-3][4], salad1[-1][-1])