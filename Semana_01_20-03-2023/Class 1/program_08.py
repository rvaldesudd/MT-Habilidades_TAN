name = 'Earth'
moons = 1
earth_name = 'Earth'
earth_moons = 1
jupiter_name = 'Jupiter'
jupiter_moons = 79
planet = {
    'name': 'Earth',
    'moons': 1
}
print(planet.get('name'))
# planet['name'] is identical to using planet.get('name')
print(planet['name'])

wibble = planet.get('wibble') # Returns None
#wibble = planet['wibble'] # Throws KeyError
planet.update({'name': 'Makemake'})
print(planet['name'])
planet['name'] = 'Makemake'
print(planet['name'])
# Using update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})
print(planet['name'])
planet['orbital period'] = 4333
print(planet)
planet.pop('orbital period')
print(planet)
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}
print(planet)
print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}
for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1
for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was {total_rainfall}cm in the last quarter')



