import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
intents.typing = True
intents.messages = True
intents.reactions = True
intents.presences = True

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

@commands.Cog.listener()
async def on_message(self,msg):
    kw = ['http','https']
    if msg.content in kw:
        print(f'someone send link.')
        await msg.channel.send(f'@{member}沒事發連結幹嘛(´・ω・`)')



bot.run('TOKEN')



