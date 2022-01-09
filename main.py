import sys
import subprocess
import os
from lib import *
from discord_webhook import DiscordWebhook

def install_dependancies():
    # subprocess.check_call(['apt', 'install', 'git']) # TODO: setup auto commit system
    subprocess.check_call([sys.executable, '-m' , 'pip3', 'install',  'discord-webhook'])
    subprocess.check_call([sys.executable, '-m' , 'pip3', 'install',  'requests'])
    


def main(w_hook):
    # Install all the dependancies need for the program
    install_dependancies()

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
    
