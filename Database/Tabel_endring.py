import sqlite3
con = sqlite3.connect("guid.db")
cur = con.cursor()
cur.execute("""CREATE TABLE Person(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            FORNAVN TEXT NOT NULL, 
            ETTERNAVN TEXT NOT NULL,
            AGE INT NOT NULL)"""
            )
cur.execute("""CREATE TABLE Bruker_konto(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            BRUKERNAVN TEXT NOT NULL,
            PASSORD TEXT NOT NULL)"""
            )
cur.execute("""CREATE TABLE Tur_info(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            LAND TEXT,
            STED TEXT NOT NULL,
            NAVN TEXT,
            BESKRIVELSE TEXT)""")


