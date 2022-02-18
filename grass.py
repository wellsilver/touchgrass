import discord
client = discord.Client()
token = 'OTQ0MzU0ODQyOTYzNTAxMDg3.YhAY-w.BrDq1UIRW5btYxSt7VEkkMDTIzo'
y = json.loads(open("a.json", "r"))
@client.event
async def on_ready():
    print("Bot started")
@client.event
async def on_message(i):
    c = i.content.lower()
    if i.author.bot:
        print()
    else:
        for i in y:
            if i in c:
                await i.channel.send(f"Touch some grass ", delete_after=30)
client.run(token)
