import sqlite3
from constants import (DATABASE_COLUMNS)
from crawler import main
from datetime import datetime

# Here we wanted to check how long does it take for the crawler to run
before = datetime.now()
current_time = before.strftime("%H:%M:%S")
print("Start at:", current_time)


# The connection to the database
conn = sqlite3.connect('crawlerData.db')

# The conactions bettween the database and the program
data = main()
print("INSERTS TO DB")

# Making string of the data to our columns
stringToFill = ""
for key, value in DATABASE_COLUMNS.items():
    stringToFill += f" {key} {value} DEFAULT NULL,"

stringToFill = stringToFill[0:-1]

# Creates the tables needed
conn.execute(
    f'CREATE TABLE IF NOT EXISTS main (id INTEGER PRIMARY KEY, {stringToFill})')

# Insert the data into our sqlite database (data is a list of dictionaries)
for item in data:
    keyToFill = ""
    valueToFill = ""
    for key, value in item.items():
        keyToFill += f" {key},"
        if isinstance(value, str):
            valueToFill += f'"{value}",'
        else:
            valueToFill += f' "{value}",'

    # -1 to remove the last comma
    keyToFill = keyToFill[0:-1]
    valueToFill = valueToFill[0:-1]

    # This is the query to insert the data (FILL THE ROWS ACOEDING TO THE CUURENT KEYS)
    try:
        conn.execute(
            f"INSERT INTO main ({keyToFill}) VALUES ({valueToFill})")
    except:
        print("=========================================================================")
        print("ERROR IN INSERTING TO DATABASE: " + str(item))
        print("=========================================================================")
        print(keyToFill)
        print("=========================================================================")
        print(valueToFill)
        print("=========================================================================")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Finished at:", current_time)

# Always commit close the connection - DO NOT DELETE
conn.commit()
conn.close()
