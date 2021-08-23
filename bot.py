import os
from dotenv import load_dotenv
from PIL import ImageDraw
from PIL import Image
from PIL import ImageFont
import io
load_dotenv()
dotenv_path =  "local.env"
load_dotenv(dotenv_path)

import discord
client = discord.Client()
import asyncio

@client.event
async def on_message(message):
    if message.content.find("!meme") != -1:
            with io.BytesIO() as image_binary:
                
                image = Image.open('./images/picture.jpg')
                draw = ImageDraw.Draw(image)
                fontsize=32
                font = ImageFont.truetype("arial.ttf", fontsize)
                draw.text((0, 0),str(message.content).split(" ")[1], fill='red',font=font)
                image.save(image_binary, 'png')
                image_binary.seek(0)
                await message.channel.send(file=discord.File(fp=image_binary, filename='image.png'))
client.run(os.getenv('TOKEN'))