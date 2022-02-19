import discord
from discord.ext import commands
intents = discord.Intents.all()
TOKEN = ''

bot = commands.Bot(command_prefix='5t-',intents=intents)

@bot.event
#機器人之事件
async def on_ready():
 print("bot online!")

@bot.event
async def on_member_join(member):
    chaanel = bot.get_channel(865942368887767081)
    await chaanel.send(f'{member}加入了伺服器 :server_icon:')
    #await:協程功能綴首
    print(f'{member} join!')


@bot.event
async def on_member_remove(member):
    chaanel = bot.get_channel(865942368887767081)
    await chaanel.send(f'{member}離開了伺服器 :server_icon:')
    print(f'{member} leave.')

@bot.command()
async def ping(ctx):
    await ctx.send(round(bot.latency*1000))

@bot.event
async def on_message(msg):
    if msg.content.startswith('http'):
        await msg.channel.send('沒事放連結幹嘛(´・ω・`)')
        print(f'someone send link.')
        



bot.run(TOKEN)



