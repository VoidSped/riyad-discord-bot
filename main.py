import discord
from webserver import keep_alive
import os
import random
import asyncio
import datetime
import tracemalloc
tracemalloc.start()

intents = discord.Intents.all()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_member_remove(member):
    channel = client.get_channel(1046213127521435728)
    await channel.send(f"{member} left because they're a snake. they're banned now honey, don't you worry..")
    await member.ban()

@client.event
async def on_message_delete(message):
    deleted_text = message.content
    with open("deleted_messages.txt", "a") as file:
        file.write(message.author + ": " + deleted_text + "\n")

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    if ("junaid" in str(message.content) or "dia" in str(message.content)) or message.author.id == 256876746861707264:

        x = random.randint(1,3)
        if x == 1:
            with open("junaid.txt", "r") as f:
                lines = f.readlines()
            random_line = random.choice(lines)
            await message.channel.send(random_line)
        
    if random.randint(1, 20) == 1:
        with open("dialogue.txt") as file:
            lines = file.readlines()
        random_line = random.choice(lines)
        start = random_line.find('"')
        end = random_line.find('"', start + 1)
        filtered_line = random_line[start + 1:end]
        channel = client.get_channel(message.channel.id)
        await channel.send(filtered_line)
    if message.author == client.get_user(285021062578700289) and isinstance(message.channel, discord.DMChannel):
            channel = client.get_channel(1046211746030952460)
            await channel.send(message.content)

    if message.author.id == 511157402222198788 and random.randint(1,12) == 1:
        await message.add_reaction("🤓")

    if message.author != client.get_user(285021062578700289) and isinstance(message.channel, discord.DMChannel):
        with open("dms.txt", "a") as file:
            file.write(f"[{message.author}] : {message.content}\n")

    if message.author.id == 256876746861707264:
        with open("junaid.txt", "a") as file:
            msg = message.content.replace('\n', ' ')
            file.write(f"{msg}\n")

@client.event
async def on_member_update(before, after):
    if after.id == 285021062578700289:
        print("Hey")
        if before.status != after.status:
            with open("user_log.txt", "w") as file:
                now = datetime.datetime.now()
                file.write(f"[{now}] {after.name}'s status changed from {before.status} to {after.status}\n")
            dm_user = client.get_user(285021062578700289)
            await dm_user.send(f"{after.name}'s status changed from {before.status} to {after.status}")

@client.event
async def on_raw_reaction_add(payload):
    if payload.user_id == 285021062578700289:
        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        await message.add_reaction(payload.emoji)

@client.event
async def on_member_join(member):
    channel = client.get_channel(1046211746030952460)
    await channel.send(f"yo {member.mention} welcome to my server")

@client.event
async def on_presence_update(before: discord.Member, after: discord.Member):
    if after.id == 511157402222198788:
        if before.status != after.status:
            with open("user_status_log.txt", "a") as file:
                now = datetime.datetime.now()
                file.write(f"[{now}] {after.name}'s status changed from {before.status} to {after.status}\n")
            dm_user = client.get_user(285021062578700289)
            await dm_user.send(f"{after.name}'s status changed from {before.status} to {after.status}")

@client.event
async def on_ready():
    print("I am back from offline Haha")
    
            
keep_alive()
TOKEN = os.environ.get('token')
client.run(TOKEN)
