import discord
from discord import guild
from discord import embeds
from discord import message
from discord.ext import commands
from discord.ext.commands.core import has_guild_permissions
from threading import Thread
from time import sleep
from csv import writer
import csv
import re
client = commands.Bot(command_prefix = '+', help_command=None)
@client.event
async def on_ready():
    print("online")
@client.command()
async def add(ctx, member1, num): 
    await ctx.send("Updated")
    list_data=[member1, num]
    with open("Scores.csv",'r') as file:
        lines = file.readlines()
    with open("Scores.csv",'w') as file:
        for line in lines:
            if line.find(member1) != -1:
                pass
            else:
                file.write(line)
    with open('Scores.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(list_data)  
        f_object.close()
@client.command()
async def currentscore(ctx):
    file1 = open("Scores.csv","r+") 
    lines = file1.read()
    print(lines)
    await ctx.send(lines)
@client.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="+add @name overallscore to update score   +currentscore for leaderboard", colour=discord.Color.green())
    await ctx.send(embed=embed)
client.run('Token')
