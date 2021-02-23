import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import csv

with open(r'C:\Users\Thomas\OneDrive\Documents\Football_Project\Data\WorldCupMatches.csv') as teams:
    teams_reader = csv.DictReader(teams)
    countries = []
    for row in teams_reader:
        countries.append(row['Home Team Name'])
        countries.append(row['Away Team Name'])

countries_refined = []
for team in countries:
    if team in countries_refined:
        continue
    else:
        countries_refined.append(team)

def update(list, to_delete, to_replace):
    for item in list:
        if item == to_delete:
            list.remove(to_delete)
            list.append(to_replace)
    return

del countries_refined[-1]

update(countries_refined, 'rn">United Arab Emirates', 'United Arab Emirates')
update(countries_refined, 'rn">Republic of Ireland', 'Republic of Ireland')
update(countries_refined, 'rn">Trinidad and Tobago', 'Trinidad and Tobago')
update(countries_refined, "Cï¿½te d'Ivoire", 'Ivory Coast')
update(countries_refined, 'rn">Serbia and Montenegro',
       'Serbia and Montenegro')
update(countries_refined, 'rn">Bosnia and Herzegovina',
       'Bosnia and Herzegovina')

print(countries_refined)