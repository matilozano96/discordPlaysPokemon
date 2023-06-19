import time
import discord
import os
import sqlite3

# Set up database connection
conn = sqlite3.connect("DATABASE.db")
cursor = conn.cursor()

intents = discord.Intents.default()  
intents.message_content = True
client = discord.Client(intents = intents)

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

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print("Message detected")
    if message.author == client.user:
        return
    
    input = message.content.lower()
    print("Evaluating " + input)
    if input in valid_commands:
        # Get the corresponding SQL key for the command
        sql_key = valid_commands[input]
        # Update the value in the database
        cursor.execute("UPDATE Inputs SET {} = 1".format(sql_key))
        conn.commit()
        print("Valid")
        await message.delete()
        
        print("Waiting")
        time.sleep(0.001)
        
        print("Reverting input")
        cursor.execute("UPDATE Inputs SET {} = 0".format(sql_key))
        conn.commit()
    else:
        print("Invalid")
    print("----------")

TOKEN = "MTExNDM5MjU4Njk3MTUyOTI0Ng.G_cG1K.LiXZuLVqNYirJjXJEjODLfCHVBytHN1YI0Y2j4"
client.run(TOKEN)