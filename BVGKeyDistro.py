import discord
import os
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands

client = discord.Client()
keymessages = {}
path = "SteamKeys.txt"
pathRedeemed = "C:\SteamKeys\SteamKeysRedeemed.txt"
RedeemedKeysChannel = '406792982273065002'
AvalibleKeysChannel = '406793113265242138'

@client.event
async def on_ready():
    print("Logged in as :")
    print(client.user.name)
    print("ID:")
    print(client.user.id)
    print("Ready to use")
    
@client.event
async def on_message (message):
    if message.author == client.user:
        return
    
    elif message.content.startswith("!Test"):
        lines = open(path, 'r').readlines()
        if len(lines) == 0:
            await client.send_message(message.author,'ERROR: OUT OF KEYS - Contact @ Swanton007 in public chat so a fix can be made')
        
        else:
            file = open(path, 'w')
            for line in lines:
                await client.send_message(discord.Object(AvalibleKeysChannel),line)
            file.close()  
        
    elif message.content.startswith("!getkeys"):
        async for message in client.logs_from(discord.Object(AvalibleKeysChannel),limit=1000):
            print ("Object Added to Dict:")
            print(discord.Object(message.id))
            print ("Object Type Added to Dict:")
            print(type(discord.Object(message.id)))
            
            keymessages.update({message.content:message.id})

    elif message.content.startswith("!gibbekey"):
        givenKey = keymessages.popitem()
        print(type(givenKey[1])) 
        print(givenKey[1])
        await client.send_message(message.author,givenKey[0])
        
        client.delete_message(discord.Object(givenKey[1]))
      
client.run(os.getenv('TOKEN'))

#discord.on_member_join(member)
