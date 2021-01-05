from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='^')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def Vtuber(ctx):
    await ctx.send('白上フブキを推していけ')


@bot.command()
async def kzrn(ctx):
    await ctx.send('kzrnはみんなの嫁<解釈一致>')    


@bot.command()
async def apex(ctx):
    await ctx.send('apexしようぜ')    

        
@bot.command()
async def youtubeAme(ctx):
    await ctx.send(' https://www.youtube.com/channel/UC6F-6adNROnUXE0jUQt1j3Q ')    

        
@bot.command()
async def thisiskzrn(ctx):
    await client.send_file(message.channel,"C:\Users\muno_negi\Downloads\Kawaiiuwu.mp4")    

        
bot.run(token)
