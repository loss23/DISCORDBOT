print("Booting up...")

# Modules
from discord.ext import commands
from termcolor import cprint
import os
import discord
from discord import Game
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
from dotenv import load_dotenv
from discord import TextChannel

# Secret
my_secret = "Key"

# Variables
bot = commands.Bot(
    command_prefix="TW",
    case_insensitive=True,  # e.g. !hElP
    strip_after_prefix=True  # e.g. ! help
)


# Bot events
@bot.event
async def on_ready():
    cprint(f"✅ {bot.user}", "green")
    activity = discord.Game(name="Penis Sex Penis Balls Cum On Me", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)


async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements :rolling_eyes:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have all the requirements :angry:")


load_dotenv()
client = bot

players = {}


# Bot commands
@bot.command()
async def StandList(ctx):
    await ctx.send(f"```The World```")


@bot.command()
async def ilovemen(ctx):
    await ctx.send(f"🤔")


@bot.command()
@commands.has_permissions(ban_members=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')


@bot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name,
                                               member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


@bot.command()
async def dc(ctx):
    await ctx.voice_client.disconnect()


@bot.command()
async def disconnect(ctx):
    await ctx.voice_client.disconnect()


# command to play sound from a youtube URL
@bot.command()
async def play(ctx, url):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options':
        '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn'
    }
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        await ctx.send('Bot is playing')

# check if the bot is already playing
    else:
        await ctx.send("Bot is already playing")
        return


# command to resume voice if it is paused
@bot.command()
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.send('Bot is resuming')


# command to pause voice if it is playing
@bot.command()
async def pause(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.send('Bot has been paused')


# command to stop voice
@bot.command()
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
        await ctx.send('Stopping...')


# command to clear channel messages
@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send("Messages have been cleared")


# Checks if the secret exists in the Secrets tab
if my_secret not in os.environ:
    cprint(
        f"\n\n------ WARNING! ------\nI could not find any secret named {my_secret!a} in the Secrets tab.\n\nhttps://media.discordapp.net/attachments/995031912026492938/1005463769712967821/unknown.png?width=342&height=418\n",
        "red")
    while True:
        pass
# Run the bot
bot.run(os.getenv(my_secret))
