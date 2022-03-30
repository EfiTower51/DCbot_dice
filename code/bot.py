import os
import random
import discord

intents = discord.Intents.all()

import json 
with open('Dice\GitHub\code\setting.json',mode='r',encoding='UTF-8') as Jfile:
    Fjd = json.load(Jfile)


bot = discord.Bot(command_prefix='5t-',intents=intents,debug_guilds=[int(Fjd['Tower'])])

master = [int(Fjd['WuYin']),int(Fjd['AiFe'])]
#悟音與艾菲的ID

#Event事件

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


@bot.event
async def on_message(msg):
    if msg.content.startwith('http'):
        await msg.channel.send('沒事放連結幹嘛(´・ω・`)')

@bot.event 
async def on_message(msg):
    call =['機器人助手','助手']
    if msg.content in call:
        if msg.author.id in master:
            await msg.channel.send('主人叫我有什麼事嗎(｡•ㅅ•｡)♡')
        elif msg.author !=bot.user:
            await msg.channel.send('哈囉，我是鐵塔的機器人助手(*‘ v`*)')
        

#Commands指令

@bot.command()
async def ping(ctx):
         await ctx.send(round(bot.latency*1000))
         print(f'pung!')


@bot.slash_command(name="intro",description="關於機器人的介紹。")
async def intro(ctx):
        await ctx.respond("屬於鐵塔的機器人助手！\n\n◎Minecraft-TowerServer訊息機器人（偶爾出現）\n◎設定提醒事項（製作中）\n◎TRPG骰子功能（製作中）\n◎關鍵字罐頭訊息回覆\n\n——\n\n這裡什麼都沒有，或許之後會出現什麼吧。")


@bot.slash_command(name="load",description="reload files.")
async def load(ctx,extension):
         bot.load_extension(f'{extension}')
         await ctx.respond(f'Loaded {extension} Done.')
         print(f'Loaded {extension}')


#骰子
@bot.slash_command(name="roll",description="來骰顆骰子吧！")
async def roll(ctx,fre,dice): 
        random.seed()
        result = random.randint(int(fre),int(fre) * int(dice))
        print(result)
        await ctx.respond(f'擲 {fre} 顆 {dice} 面骰：' & result)


##TRPG-CoC7e
@bot.slash_command(name="7e",description="適用於TRPG當中CoC-7e的技能檢定骰。")
async def coc7e(ctx,number):
    random.seed()
    roll = random.randint(1,100)
    number=int(number)
    
    if roll == 1:
     await ctx.respond(f"""1D100 ≦ {number}\n檢定結果：{roll}\n哇！！大成功！""")
     return

    elif number > 50 and roll == 100:
        await ctx.respond(f"""1D100 ≦ {number}\n檢定結果：{roll}\nㄨㄚˊ，大失敗！""")
        return

    elif number < 50 and 96 <= roll <= 100:
        await ctx.respond(f"""1D100 ≦ {number}\n檢定結果：{roll}\nㄨㄚˊ，大失敗！""")
        return

    elif roll > number:
        await ctx.respond(f"""1D100 ≦ {number}\n檢定結果：{roll}\n啊，失敗了。""")
        return

    elif roll <= number:
        if roll < number/5:
             await ctx.respond(f"""1D100 ≦ {number}\n檢定結果：{roll}\n極限成功DA！""")
             return

        if roll <= number/2 and roll > number/5:
             await ctx.respond(f"""1D100 ≦ {number}\n檢定結果：{roll}\n恭喜，困難成功！""")
             return

        if roll > number/2:
             await ctx.respond(f"""1D100 ≦ {number}\n檢定結果：{roll}\n你成功了！""")
             return

         

#for filename in os.listdir('./Dice/GitHub'):
#    if filename.endswith('.py'):
#     bot.load_extension('code.'+ filename[:-3])


if __name__ == "__main__" :
  bot.run(Fjd['TOKEN'])



