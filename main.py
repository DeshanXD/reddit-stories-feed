import sys
import subprocess
import os

# Install all the dependancies need for the program

subprocess.check_call([sys.executable, '-m' , 'pip', 'install',  'discord-webhook'])
subprocess.check_call([sys.executable, '-m' , 'pip', 'install',  'requests'])

# Third party dependancies
from lib import *    
from discord_webhook import DiscordWebhook

def main(w_hook):

    # Get random post by calling all the subreddits
    d = scrape_data()
    title, body, author = content_pool(d)

    em = embed_builder(content_filter(title), body, author) # build embed with content filtering

    webhook = DiscordWebhook(url=w_hook) # discord-webhook url
    webhook.add_embed(em)
    
    webhook.execute()
    
if __name__ == "__main__":

    # Get the webhook url
    w_url = sys.argv[1]
    main(w_url)
    
