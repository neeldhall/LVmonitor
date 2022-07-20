import time
import os
import zipfile
import discord
import requests
import json
import random
from bs4 import BeautifulSoup
from discord_webhook import DiscordEmbed, DiscordWebhook

# Discord localhost Louis Vuitton Product Monitor built by Neel Dhall (Posty#0002)

prods = ['ENTER PRODUCTS HERE']

webhook = 'ADD WEBHOOK HERE'

webhook1 = DiscordWebhook(url=webhook, username="Louis Vuitton Monitor")
webhook2 = DiscordWebhook(url=webhook, username="Louis Vuitton Monitor")
embed1 = DiscordEmbed(color=2303786)
embed1.set_footer(text="Posty#0002")
embed1.set_timestamp()
embed1.add_embed_field(name="Louis Vuitton Monitor", value="Monitoring SKUs: " + str(prods), inline=False)
webhook1.add_embed(embed1)
webhook1.execute()

session = requests.Session()
sessionHeaders = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    "accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "content-type": "application/json"
}

while True:
    prod = random.choice(prods)
    aval = session.get('https://api.louisvuitton.com/api/eng-us/catalog/availability/' + prod + '?.html', headers=sessionHeaders)
    scraped = aval.text
    cut1 = scraped.replace('{"@type":"ItemAvailability","@context":"http://schema.org","skuAvailability":[', '')
    cut2 = cut1.replace('],"identifier":"' + prod + '"}','')
    sizes = cut2.split('},{')
    size = random.choice(sizes)
    ele = size.split(',')
    if ele[4] == '"inStock":true':
        print('Random Size In Stock')
        sz = ele[1]
        pid = sz.replace('"skuId":"','')
        pidfinal = pid.replace('"','')
        print("Got " + pidfinal)
        embed2 = DiscordEmbed(color=2303786)
        embed2.set_footer(text="Posty#0002")
        embed2.set_timestamp()
        embed2.add_embed_field(name="Louis Vuitton Monitor", value=pidfinal + " In Stock\n" + "https://us.louisvuitton.com/eng-us/search/" + pidfinal, inline=False)
        webhook2.add_embed(embed2)
        webhook2.execute()
        time.sleep(1)







