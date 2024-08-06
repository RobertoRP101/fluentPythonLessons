lax_coordinates = (23.3432, -235.2344231)
city, year, pop, chg, area = ('Mexico', 2024, 34_658, 0.23, 8723)

traveler_ids = [('USA', '145672457'), ('MEX', '23987322'), ('JAP', '2343462')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport) # %s Treats each item asa separe field

for contry, _ in traveler_ids: # Dummy variable 
    print(contry)