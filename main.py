import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

try:
    with open('.discord_bot_key', 'r') as f:
        token = f.readline().strip()  # discord API key
        channel_id = int(f.readline().strip())  # channel ID
except FileNotFoundError:
    print("file not found")
    exit(1)

except Exception as e:
    print(f"Needed information is not there {e}")
    exit(1)

@client.event
async def on_ready():
    print(f'logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # respond with hello
    if message.content.lower() == 'hello' and message.channel.id == channel_id:
        await message.channel.send('Hello!')

client.run(token) # use token