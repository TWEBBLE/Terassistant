import sqlite3

#Created Python connecter to SQLite3 and created Database
connector = sqlite3.connect("world_cup_matches.db")

#created cursor for connector
cursor = connector.cursor()

#Created table for database
cursor.execute('''CREATE TABLE matches (
    Year INTEGER,
    Datetime DATE,
    Stage VARCHAR(20),
    Stadium VARCHAR(50),
    City VARCHAR(20),
    Home_Team_Name VARCHAR(50),
    Home_Team_Goals INTEGER,
    Away_Team_Goals INTEGER,
    Away_Team_Name VARCHAR(50),
    Win_conditions VARCHAR(50),
    Attendance INTEGER,
    Half_time_Home Goals,
    Half_time_Away Goals,
    Referee VARCHAR(50),
    Assistant_1 VARCHAR(50),
    Assistant_2 VARCHAR(50),
    RoundID INTEGER,
    MatchID INTEGER,
    Home_Team_Initials VARCHAR(5),
    Away_Team_Initials VARCHAR(5)
)''')

