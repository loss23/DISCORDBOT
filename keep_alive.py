from flask import Flask
from threading import Thread
from discord.ext import commands
import keep_alive #don't forget to import the file!
import discord
import os

bot = commands.Bot(
    command_prefix="TW",
    case_insensitive=True,  # e.g. !hElP
    strip_after_prefix=True  # e.g. ! help
)

app = Flask('')

@app.route('/')
def main():
  return "Your Bot Is Ready"

def run():
  app.run(host="0.0.0.0", port=8000)


client = discord.Client()

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('!ping'):
		await message.channel.send('Pong!')

# Secret
my_secret = "Key"

keep_alive.keep_alive()
client.run(os.environ(my_secret))