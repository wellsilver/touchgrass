import discord
import json
import time

client = discord.Client()
token = 'OTQ0MzU0ODQyOTYzNTAxMDg3.YhAY-w.BrDq1UIRW5btYxSt7VEkkMDTIzo'
f = open('a.json',)
data = json.load(f)
@client.event
async def on_ready():
    print("Bot started")
    while true:
        print("Tick!")
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f'1.2 | Grass help'))
        time.sleep(600)
@client.event
async def on_message(l):
    c = l.content.lower()
    if l.author.bot:
        return
    else:
        if c == "grass help":
            l.reply("The grass bot has no commands sadly, you can see the .json with all keywords (and submit pull requests) that triggers the bot here https://wellsilver.github.io/a/dis.json")
        for i in data['names']:
            
            if i in c:
                await l.channel.send(f"Touch some grass {l.author.mention}", delete_after=30)
                print(f"{l.author} needed to touch some grass")
                return
client.run(token)
