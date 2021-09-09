import os
from dotenv import load_dotenv
from PIL import ImageDraw
from PIL import Image
from PIL import ImageFont
import io
from process_image import draw_meme

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
                image = draw_meme(str(message.content).split("!meme")[1])
                image.save(image_binary, 'png')
                image_binary.seek(0)
                await message.channel.send(file=discord.File(fp=image_binary, filename='image.png'))
client.run(os.getenv('TOKEN'))