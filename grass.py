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
    await self.bot.change_presence(game=discord.Game(name="Just restarted! v1.1", type=1))
    time.sleep(90)
    await self.bot.change_presence(game=discord.Game(name="V1.1", type=1))
    
@client.event
async def on_message(l):
    c = l.content.lower()
    if l.author.bot:
        return
    else:
        for i in data['names']:
            
            if i in c:
                await l.channel.send(f"Touch some grass {l.author.mention}", delete_after=30)
                print(f"{l.author} needed to touch some grass")
                return
client.run(token)
