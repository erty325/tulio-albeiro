import os
from dotenv import load_dotenv
import discord

# optional: load a local .env file for development
load_dotenv()

from keep_alive import start as keep_alive_start

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


if __name__ == '__main__':
    # start a small webserver to keep the repl awake (Replit, uptime monitors, etc.)
    try:
        keep_alive_start()
    except Exception:
        # non-fatal if Flask isn't available locally; we'll still try to run the bot
        pass

    token = os.environ.get('DISCORD_TOKEN')
    if not token:
        print('ERROR: DISCORD_TOKEN not found in environment. Set DISCORD_TOKEN as a secret in Replit or in a local .env file.')
    else:
        client.run(token)