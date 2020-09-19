import discord
from discord.ext import commands
import os
import re
from dotenv import load_dotenv

bot = commands.Bot('pod/')
load_dotenv()
admin_role_id = int(os.getenv("ADMIN_ROLE_ID"))

def main():
    bot.run(os.getenv("TOKEN"))


@bot.command(description="Create pod")
@commands.has_role(admin_role_id)
async def create(ctx, *, arg):
    pod_name = arg

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
