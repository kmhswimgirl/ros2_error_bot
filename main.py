import discord
from ros_errors import ROSErrors as ros

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

def bot_test(channel_id):
    if channel_id == channel_id:
        return True
    else:
        return False

@client.event
async def on_ready():
    print(f'logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # respond with a ros error
    if message.content.lower() == 'ros' and bot_test(message.channel.id): 
        ros_msg = ros.get_error_msg()
        await message.channel.send(f"`{ros_msg}`")

    elif message.content.lower() == 'rosrun' and bot_test(message.channel.id):
        await message.channel.send('AHHHHHHH ROS1 Reference!')

client.run(token) # use token