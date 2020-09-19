import discord
from discord.ext import commands
import os
import re
from dotenv import load_dotenv

bot = commands.Bot('pod/')

def main():
    load_dotenv()
    bot.run(os.getenv("TOKEN"))

@bot.command(description="Create pod")
async def create(ctx):
    message = ctx.message.clean_content
    args = message.split(' ')
    pod_name = ""

    if args[1][0] == '"':
        matches = re.findall(r'\"(.+?)\"', message)
        pod_name = ",".join(matches)
    elif len(args) > 2:
        args.pop(0)
        for name in args:
            pod_name += name + ' '
    else:
        pod_name = args[1]

    guild = bot.get_guild(int(os.getenv("GUILD_ID")))
    pod_permission = discord.Permissions()
    pod_role = await guild.create_role(name=pod_name, permissions=pod_permission)
    
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        pod_role: discord.PermissionOverwrite(read_messages=True)
    }

    pod_category = await guild.create_category(name=pod_name, overwrites=overwrites)
    await guild.create_text_channel(name="general", category=pod_category)
    await ctx.send(f"Role and Category made for {pod_name}")
