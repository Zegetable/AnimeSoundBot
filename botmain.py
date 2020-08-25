import discord
from discord.ext import commands
import asyncio
pillarthemeString = "pillar theme"
bakaString = "baka"
speedwagonString = "speedwagon"
godString = "god"
baseballString = "baseball"
konoString = "kono"
helpmeString = "help me"
jibunString = "jibun"
soundFileString= ""
correctSound= False



bot = commands.Bot(command_prefix = '!', case_insensitive = True)

@bot.event
async def on_ready():
    print("Time has run out JoJo...")

@bot.command()
async def oh(ctx, *, args):
    wamuuVC = ctx.author.voice.channel
    if args.lower() == pillarthemeString:
        soundFileString= './sounds/pillar men theme (quieter1).mp3'
        correctSound= True
        await ctx.send("Your time is nearly up Jojo!")
        #put timer stuff here if want it
    elif args.lower() == bakaString:
        soundFileString= './sounds/Stronheim- Baka monoga.mp3'
        correctSound= True
        await ctx.send("BRRRRRRAKA MONOGA")
    elif args.lower() == speedwagonString:
        soundFileString= './sounds/SpeeeedwaGONnnn.mp3'
        correctSound= True
        await ctx.send("SpeeeedwaGONnnn")
    elif args.lower() == godString:
        soundFileString= './sounds/oh god.mp3'
        correctSound= True
        await ctx.send("Ooohh Geerd!")
    elif args.lower() == baseballString:
        soundFileString= './sounds/Oh! That\'s A Baseball!.mp3'
        correctSound= True
        await ctx.send("oh.. dats a basebol?!")
    elif args.lower() == konoString:
        soundFileString= './sounds/kono Dio da!.mp3'
        correctSound= True
        await ctx.send("KONO DIO DA")
    elif args.lower() == helpmeString:
        soundFileString= './sounds/help me oh my god.mp3'
        correctSound= True
        await ctx.send("Help me, oh my goood!")
    elif args.lower() == jibunString:
        soundFileString= './sounds/jibun wo my god.mp3'
        correctSound= True
        await ctx.send("JIBUN WOOO")
    if correctSound == True:
        wamuuClient = await wamuuVC.connect(timeout=10.0, reconnect=False)
        wamuuClient.play(discord.FFmpegPCMAudio(soundFileString))
    correctSound = False
    while wamuuClient.is_playing():
        await asyncio.sleep(1)
    await wamuuClient.disconnect() #leaves after playing



#catches the exception thrown the the oh command doesn't have an arg
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        return

@bot.command()
async def stopwamuu(ctx):
    await ctx.voice_client.disconnect()
    
@bot.command()
async def wamuuc(ctx):
    commandsEmbed = discord.Embed(title = "Commands for Wamuu", description= "make sure you are in a voice channel")
    commandsEmbed.add_field(name= 'arguments for "!oh" command:', value= pillarthemeString +"\n"+ bakaString+"\n"+ speedwagonString+"\n"+ godString+"\n"+ shitString+"\n"+ holyshitString+"\n"+ helpmeString+"\n"+ bitchString+"\n", inline= False)
    await ctx.send(embed= commandsEmbed)


bot.run("YOUR BOT AUTH CODE HERE")

#timer stuff to play for certain time
#counter = 0
#duration = 14   # In seconds
#plays for seconds = duration
#while not counter >= duration:
#await asyncio.sleep(1)
#counter = counter + 1
#await wamuuClient.disconnect()

