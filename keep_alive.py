from flask import Flask
from threading import Thread
from discord.ext import commands
import metronome_loop
import discord

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

def keep_alive():
  server = Thread(target=run)
  server.start()
