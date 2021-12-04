import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.ext.commands import CommandError
from discord.ext.commands import Bot, has_permissions, CheckFailure
from discord.utils import get
from discord import Client, Intents, Embed
from discord_slash import SlashCommand, SlashContext
import sys
import os
import base64
import time
import json
import requests
import re
from collections.abc import Sequence
from discord import Client
import DiscordUtils
from dotenv import load_dotenv
import random

load_dotenv()

bot = commands.Bot(command_prefix=["LS"], help_command=None)

async def is_owner(ctx):
    return ctx.author.id == 569334038326804490
    return ctx.author.id == 804649076787642408

@bot.command()
async def help(ctx):
    embed1=discord.Embed(title="Help Page 1", description='Official Lime Studios Bot')
    embed1.set_author(name="Version: v1.0.0", url="https://github.com/Xylo4388")
    embed1.add_field(name="LShelp", value="Shows this list of commands.", inline=False)
    embed1.add_field(name="LSReactionRoles", value="Will create the Reaction Roles Menu (Administrator Only).", inline=False)

    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx)
    paginator.add_reaction('⬅', "back")
    paginator.add_reaction('➡', "next")
    paginator.remove_reactions = True
    embeds = [embed1]
    await paginator.run(embeds)

@bot.command()
@commands.check(is_owner)
async def ReactionRoles(ctx):
    embed1=discord.Embed(title="**__Welcome to Lime Studios__**", description="React to Verify")
    embed1.add_field(name="**Read our Rules**", value="Please Read our <#916154436986994698> before you continue")
    embed1.add_field(name="**Verify Here**", value="React with ✅ to gain access to the Lime Studios Discord Server.", inline=False)

    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx)
    embeds = [embed1]
    await paginator.run(embeds)

@bot.event
async def on_message(message):
    if "suggestion:" in message.content.lower():
        emoji1 = '✅'
        emoji2 = '❌'
        await message.add_reaction(emoji1)
        await message.add_reaction(emoji2)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.channel.send("""
        Sorry, this is not a Command, come back later with other commands.
        """)
    elif isinstance(error, CheckFailure):
        await ctx.channel.send("Sorry mate, but your opinion is irrelevant.")
    else:
        print("An unhandled error has occured.")
        await ctx.channel.send("```{error}```".format(error=error))

bot.run(os.getenv('TOKEN'))
