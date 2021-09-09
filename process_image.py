from PIL import Image,ImageDraw, ImageFont
import textwrap
import requests

#draws the text on the meme
def draw_meme(text):
    url="https://picsum.photos/200/300?random=2"
    text = str(text).lstrip()
    font = ImageFont.truetype("DejaVuSans.ttf", 15)
    im = Image.open(requests.get(url, stream=True).raw)
    lines = textwrap.wrap(text, width=int(im.size[0]/10),break_long_words=True)
    result = Image.new(im.mode, (im.width, im.height+ len(lines)*30), (0, 0, 255))
    result.paste(im, (0, 0))
    im = result
    draw = ImageDraw.Draw(im)
    draw.rectangle(((0, im.size[1]), (im.size[0], im.size[1]-(30)*len(lines))), fill="black")
    for count, line in enumerate(reversed(lines)):
        draw.text((10,im.size[1]-(25)*(count+1)), line, font=font)
    return im
    
    