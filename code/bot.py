import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
import json 
with open('Dice\GitHub\code\setting.json',mode='r',encoding='UTF-8') as Jfile:
    Fjd = json.load(Jfile)


bot = discord.Bot(command_prefix='5t-',intents=intents,debug_guilds=[int(Fjd['Tower'])])

master = ['WuYin悟音#5318','艾菲MK#4816']

@bot.event
#機器人之事件
async def on_ready():
 print(f"{bot.user} online!")


#@bot.event
#async def on_member_join(member):
#    chaanel = bot.get_channel(865942368887767081)
#    await chaanel.send(f'{member}加入了伺服器 :server_icon:')
#    #await:協程功能綴首
#    print(f'{member} join!')


#@bot.event
#async def on_member_remove(member):
#    chaanel = bot.get_channel(865942368887767081)
#    await chaanel.send(f'{member}離開了伺服器 :server_icon:')
#    print(f'{member} leave.')


@bot.command()
async def ping(ctx):
    await ctx.send(round(bot.latency*1000))
    print(f'pung!')


@bot.slash_command(name="intro",description="關於機器人的介紹。")
async def intro(ctx):
    await ctx.respond("""
    屬於鐵塔的機器人助手！
    
    ◎Minecraft-TowerServer訊息機器人（偶爾出現）
    ◎設定提醒事項（製作中）
    ◎TRPG骰子功能（製作中）
    ◎關鍵字罐頭訊息回覆
    
    ——
    
    這裡什麼都沒有，或許之後會出現什麼吧。""")


@bot.command()
async def load(ctx,extension):
    bot.load_extension(f'{extension}')
    await ctx.send(f'Loaded {extension} Done.')
    print(f'Loaded {extension}')

@bot.event
async def on_message(msg):
    if msg.content.startswith('http'):
        await msg.channel.send('沒事放連結幹嘛(´・ω・`)')

@bot.event 
async def on_message(msg):
    call =['機器人助手','助手']
    
    if msg.content in call and msg.author is master :
        await msg.channel.send('主人叫我有什麼事嗎(｡•ㅅ•｡)♡')




bot.run(Fjd['TOKEN'])



