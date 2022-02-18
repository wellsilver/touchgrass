import discord
client = discord.Client()
token = 'OTQ0MzU0ODQyOTYzNTAxMDg3.YhAY-w.BrDq1UIRW5btYxSt7VEkkMDTIzo'

@client.event
async def on_ready():
    print("Bot started")
@client.event
async def on_message(i):
    c = i.content.lower()
    if i.author.bot:
        print()
    else:
        if 'genshin' in c:
            await i.channel.send("Touch some grass", delete_after=5)
        if 'nft' in c:
            await i.channel.send("Touch some grass", delete_after=5)
        if 'league of legends' in c:
            await i.channel.send("Touch some grass", delete_after=5)

client.run(token)
