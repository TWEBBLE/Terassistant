import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path

MATCH_DATA = "Football_Project\Data\WorldCupMatches.csv"
MATCH_DATA_PATH = Path(MATCH_DATA)
df = pd.read_csv(MATCH_DATA)

print(df.head())

# Refined Dataframe down to goals and games
#goals_per_game = df.loc[:, [
#    "MatchID", "Home Team Name", "Away Team Name", "Home Team Goals", "Away Team Goals"]]

# Define a dictionary containing Country and Goals
#countries = []
#goals = []

#for team in (goals_per_game[["Home Team Name"], ["Away Team Name"]]):
#    if (goals_per_game[["Home Team Name"], ["Away Team Name"]]) != team in countries:
#        countries.append(team)

#country_goals = {country : goal for country, goal in zip(countries, goals)}

#if (goals_per_game[["Home Team Name"], ["Away Team Name"]]) 





#for country : goals in 

# Convert the dictionary into DataFrame
#df = pd.DataFrame(data)

# Declare a list that is to be converted into a column
#address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']

# Using 'Address' as the column name
# and equating it to the list
#df['Address'] = address

# Observe the result
#df











# Refined cases_per_month down to cases only in the US
#cases_USA = cases_per_month[cases_per_month.countryterritoryCode == "USA"]

# Refined Cases in the US by month

#monthly_cases = dict()
#months = cases_USA.month.unique()


#def get_monthly_cases(dataframe, month):
#    return dataframe[dataframe.month == month]


#for month in months:
#    monthly_cases[month] = get_monthly_cases(cases_USA, month)

#sum_of_cases = dict()
#
# Sum of cases in the US by month
#for month in monthly_cases.keys():
#    sum_of_cases[month] = monthly_cases[month]["cases"].sum()
