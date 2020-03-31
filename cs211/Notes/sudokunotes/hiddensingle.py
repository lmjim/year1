'''Pseudocode for Hidden Single'''


LEFTOVERS = set(CHOICES)
for tile in group:
    LEFTOVERS -= {tile.value}  # remove it from set leftovers

for value in LEFTOVERS:
    places_to_put_value = []
    for tile in group:
        # can value go in tile?
        # if it can go there,
            # add to places to put value
    if len(places_to_put_value) == 1:
        # put the value there!





# NOTE:
# USE METHOD TO SET THE VALUE
# GRAPHICS AND STUFF WON'T UPDATE RIGHT IF YOU DON'T USE THE METHOD