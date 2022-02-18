import discord
client = discord.Client()
token = 'token'

@client.event
async def on_message(i):
    c = i.content.lower()
    if i.author.bot:
        print()
    else:
        if 'genshin' in c:
            await i.reply("Touch some grass")
        if 'nft' in c:
            await i.reply("Touch some grass")
        if 'league of legends' in c:
            await i.reply("Touch some grass")

client.run(token)
