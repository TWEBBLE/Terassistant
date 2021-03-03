import sqlite3
import pandas as pd

#created dataframe with world cup match data
df = pd.read_csv(
    r"C:\Users\Thomas\OneDrive\Documents\Football_Project_Github\Data\WorldCupMatches.csv")

#refine dataframe
refined_df = (df[['Year', 
                  'Stadium',
                  'Home Team Name' ,
                  'Home Team Goals',
                  'Away Team Goals',
                  'Away Team Name', 
                  'Attendance',
                  'RoundID',
                  'MatchID',
                  ]])

print(refined_df.head())
