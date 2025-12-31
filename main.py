import os
import discord

# optional: load a local .env file for development; don't fail if python-dotenv isn't installed
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception as e:
    print('python-dotenv not available or failed to load .env:', e)

# import keep-alive starter (keep_alive is resilient and falls back if Flask missing)
try:
    from keep_alive import start as keep_alive_start
except Exception as e:
    # keep_alive should be robust, but guard here too
    print('keep_alive import failed:', e)
    keep_alive_start = None

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
    if callable(keep_alive_start):
        try:
            keep_alive_start()
        except Exception as e:
            print('Warning: keep_alive failed to start:', e)

    token = os.environ.get('DISCORD_TOKEN')
    if not token:
        print('ERROR: DISCORD_TOKEN not found in environment. Set DISCORD_TOKEN as a secret in Replit or in a local .env file.')
    else:
        client.run(token)