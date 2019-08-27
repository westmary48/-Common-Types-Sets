showroom = {'bentley', 'range rover', 'tesla', 'audi'}

print(showroom)

showroom.add('bentley')

print(showroom)

showroom.add('bentley')

print(showroom)

showroom.update({'mercedes', 'lexus'})

print(showroom)

showroom.discard('audi')

print(showroom)

junkyard = {'dodge', 'mercedes', 'honda', 'audi', 'range rover'}

junkyard_and_showroom = showroom.intersection(junkyard)

print(junkyard_and_showroom)

print(junkyard.union(showroom))