import os

class Config(object):
   # The Telegram API things
   API_ID= int(os.environ.get("API_ID"))
   API_HASH = os.environ.get("API_HASH")
   # get a token from @BotFather
   BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
   # channel id = -100 (for logs)
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))   
   # Array to store users who are authorized to use the bot 
   AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())    
   # force sub user to the channel (without @)
   CHNAME = os.environ.get("CHNAME")
   # Heroku App Name Full Eg:- {appname}.herokuapp.com
   APP_NAME = os.environ.get("APP_NAME")
   # Port No. Leave it blank if you don't know.
   PORT = int(os.environ.get("PORT", "8080"))
