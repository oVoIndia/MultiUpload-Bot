import os

class Config(object):
   # The Telegram API things
   API_ID= int(os.environ.get("API_ID"))
   API_HASH = os.environ.get("API_HASH")
   # get a token from @BotFather
   BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
   
