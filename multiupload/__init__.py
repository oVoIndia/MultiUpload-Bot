#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) oVoIndia | oVo-HxBots

from config import Config
from telethon import TelegramClient
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)


anjana = TelegramClient('anjana', api_id=Config.API_ID, api_hash=Config.API_HASH).start(bot_token=Config.BOT_TOKEN) 
