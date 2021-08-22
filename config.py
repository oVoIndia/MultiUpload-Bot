import os

class Config(object):
   # The Telegram API things
   API_ID= int(os.environ.get("API_ID"))
   API_HASH = os.environ.get("API_HASH")
   # get a token from @BotFather
   BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
   HELPMSG = '''
➖ **Help Menu | MultiUpload Bot**➖
● `/gofile` - Upload files to GoFile
● `/anonfile` - Upload files to AnonFile
● `/ufile` - Upload files to UFile
● `/bayfiles` - Upload files to BayFiles
● `/tsh` - Upload files to TransferSH
● `/tninja` - Upload files to TmNinja
● `/fileio` - Upload files to FileIO
● `/mixdrop` - Upload files to MixDrop
✦ **Powered By [oVoIndia]**(https://github.com/oVoIndia)
✦ Made with ♥️ by [HxBots](t.me/hxbots)'''
