import discord
import json
#import time

client = discord.Client()
token = 'OTQ0MzU0ODQyOTYzNTAxMDg3.YhAY-w.BrDq1UIRW5btYxSt7VEkkMDTIzo'
f = open('a.json',)
data = json.load(f)
@client.event
async def on_ready():
    print("Bot started")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f'Just restarted! V1.1'))
    
@client.event
async def on_message(l):
    c = l.content.lower()
    if l.author.bot:
        print()
    else:
        for i in data['names']:
            print(i)
            if i in c:
                await l.channel.send(f"Touch some grass {l.author.mention}", delete_after=30)
                return
client.run(token)
