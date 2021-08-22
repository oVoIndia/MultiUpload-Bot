#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) oVoIndia | oVo-HxBots

import asyncio, random
from config import Config
from telethon import events, Button
from multiupload import anjana

s = ["CAADBAADxgkAAjQF0VL5yl4Td0utTgI",
	"CAADBAADoAsAAv3iYFGE3u_w4y_1zgI",
	"CAADBAADMggAAq0Q0FK1ZIUPLNxGcAI",
	"CAADBAAD7AoAAr8i2VGALarwosnJIgI",
	"CAADBAADrQoAAmzO0VFDq1aGz7rGHgI",
	"CAADBAADbQgAAhI40VH51AABGZuwl74C"]

@anjana.on(events.NewMessage(pattern='^/start'))
async def start(event):
	async with anjana.action(event.chat_id, 'typing'):
		await asyncio.sleep(3)
	user_id = event.sender_id
	xx = await event.get_chat()
	await event.reply(f"Hey [{xx.first_name}]({xx.id}), I am **MultiUploader Bot**", buttons=[
				Button.url('Support Chat 💭', 't.me/hxsupport')
			])


@anjana.on(events.NewMessage(pattern='^/help'))
async def help(event):
	async with anjana.action(event.chat_id, 'typing'):
		await asyncio.sleep(3)
	user_id = event.sender_id
	xx = await event.get_chat()
	 await event.reply(Config.HELPMSG, buttons=[
				Button.url('Support Chat 💭', 't.me/hxsupport')
			], link_preview=False)
