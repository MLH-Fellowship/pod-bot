import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv

bot = commands.Bot('pod/')
load_dotenv()
admin_role_id = int(os.getenv("ADMIN_ROLE_ID"))
file_path = None

def main(args):
    global file_path
    if len(args) > 2 and args[1] == "--file":
        file_path = args[2]
    bot.run(os.getenv("TOKEN"))

@bot.event
async def on_ready():
    print("Ready!")
    if file_path != None:
        await read_file(file_path)

@bot.command(description="Create Pod")
@commands.has_role(admin_role_id)
async def create(ctx, *, arg):
    await create_pod(arg)
    await ctx.send(f"Role and Category made for {arg}")
    
async def read_file(path):
    try:
        print("Reading file...")
        file = open(path, 'r')
        lines = file.readlines()
        for pod_name in lines:
            await create_pod(pod_name)
            print(f"{pod_name} created!")
        print("All pods created") 
    except Exception as e:
        print(f"Invalid file path: {e}")


async def create_pod(pod_name):
    guild = bot.get_guild(int(os.getenv("GUILD_ID")))
    pod_permission = discord.Permissions()
    pod_role = await guild.create_role(name=pod_name, permissions=pod_permission)
    
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        pod_role: discord.PermissionOverwrite(read_messages=True, send_messages=True)
    }

    pod_category = await guild.create_category(name=pod_name, overwrites=overwrites)
    await guild.create_text_channel(name="general", category=pod_category)
