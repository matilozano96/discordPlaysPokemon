import sqlite3
import time

# Set up database connection
conn = sqlite3.connect("DATABASE.db")
cursor = conn.cursor()

# Define valid commands and their corresponding SQL keys
valid_commands = {
    "a": "A",
    "b": "B",
    "start": "Start",
    "select": "SEL",
    "up": "move_Up",
    "down": "move_Down",
    "left": "move_Left",
    "right": "move_Right",
    "d": "move_Down",
    "u": "move_Up",
    "l": "move_Left",
    "r": "move_Right",
    "lt": "L",
    "rt": "R"
}



while True:
    user_input = input("Enter a command: ")

    # Convert the input to lowercase for case insensitivity
    user_input = user_input.lower()

    if user_input in valid_commands:
        # Get the corresponding SQL key for the command
        sql_key = valid_commands[user_input]
        # Update the value in the database
        cursor.execute("UPDATE Inputs SET {} = 1".format(sql_key))
        
        time.sleep(0.2)
        cursor.execute("UPDATE Inputs SET {} = 0".format(sql_key))
        conn.commit()
    else:
        print("Invalid.")

# Close the database connection when done
conn.close()
