import discord
from ros_errors import ROSErrors as ros
import os
import yaml

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
token = os.environ.get('DISCORD_BOT_KEY')

class errorBot:
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        try:
            with open('config.yaml', 'r') as f:
                config = yaml.safe_load(f)
        except FileNotFoundError:
            print('config not found')
            exit(1)
        
        self.channel = config['channels']['bot_test']
        
    @client.event
    async def on_ready():
        print(f'logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        # respond with a ros error
        if message.content.lower() == 'ros': 
            ros_msg = ros.get_error_msg()
            await message.channel.send(f"`{ros_msg}`")
            print(f'sent ros error to: {message.channel.id}')

        # be mad at a Noetic reference
        elif message.content.lower() == 'rosrun':
            await message.channel.send('AHHHHHHH ROS1 Reference!')
            print(f'Noetic reference detected in channel: {message.channel.id}')

if __name__ == '__main__':
    client.run(token) 