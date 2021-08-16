#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) oVoIndia | oVo-HxBots

import asyncio, random
from config import Config
from telethon import events, Button
from multiupload import anjana
from telethon.tl.functions.channels import GetParticipantRequest as p
from telethon.errors import UserNotParticipantError

async def check_participant(user_id, chat_id, reply_id, cb=False):
	try:
		await anjana(p(chat_id, user_id))
		return True
	except:
		if not cb:
			await anjana.send_message(user_id, '**You are not joined to my update channel. Please join to my update channel and start me again 👀**', buttons=[
				Button.url('Join Now!', f't.me/{Config.CHNAME}'),
				Button.inline('Check', data='chk')
			], reply_to=reply_id)
		return False

s = ["CAADBAADxgkAAjQF0VL5yl4Td0utTgI",
	"CAADBAADoAsAAv3iYFGE3u_w4y_1zgI",
	"CAADBAADMggAAq0Q0FK1ZIUPLNxGcAI",
	"CAADBAAD7AoAAr8i2VGALarwosnJIgI",
	"CAADBAADrQoAAmzO0VFDq1aGz7rGHgI",
	"CAADBAADbQgAAhI40VH51AABGZuwl74C"]

@anjana.on(events.CallbackQuery(pattern='chk'))
async def _(event):
	try:
		await anjana(p(f'@{Config.CHNAME}', event.sender_id))
	except:
		await event.answer("💬 You are not Join. Please Join to Channel.", alert=True)
	else:
		await event.answer("💬 Thanks for Supporting.", alert=True)
		await event.delete()
		await anjana.send_file(event.chat_id, random.choice(s), reply_to=event)
		await event.reply(f"Hey [{xx.first_name}]({xx.id}), I am **oVo MultiUploader Bot**", buttons=[
				Button.url('Support Chat 💭', 't.me/hxsupport')
			])
