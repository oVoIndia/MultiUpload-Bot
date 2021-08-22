#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) oVoIndia | oVo-HxBots

import asyncio, os, requests, time
from requests import post
from multiupload import anjana
from telethon.sync import events, Button
from multiupload.utils import downloader, humanbytes
from config import Config

@anjana.on(events.NewMessage(pattern='^/ufile'))
async def ufile(event):
	user_id = event.sender_id
	if event.reply_to_msg_id:
		pass
	else:
		return await event.edit("Please Reply to File")

	async with anjana.action(event.chat_id, 'typing'):
		await asyncio.sleep(2)
	msg = await event.reply("**Processing...**")
	amjana = await event.get_reply_message()


	##UPLOADING...
	result = await downloader(
		f"downloads/{amjana.file.name}",
		amjana.media.document,
		msg,
		time.time(),
		f"**🏷 Downloading...**\n➲ **File Name:** {amjana.file.name}",
	)

	async with anjana.action(event.chat_id, 'document'):
		await msg.edit("Now Uploading to UFile")
		r = post('https://up.ufile.io/v1/upload/create_session',
			data={'file_size': amjana.file.size})

		r2 = post('https://up.ufile.io/v1/upload/chunk',
			data={'chunk_index': 1, 'fuid': r.json()["fuid"]},
			files={'file': open(f'{result.name}','rb')}
			)

		url = "https://up.ufile.io/v1/upload/finalise"
		r3 = post(url, data={
			'fuid': r.json()["fuid"],
			'file_name': result.name,
			'file_type': result.name.split(".")[-1],
			'total_chunks': 1
			})
	await anjana.action(event.chat_id, 'cancel')

	hmm = f'''File Uploaded successfully !!
Server: UFile

**~ File name:** __{amjana.file.name}__
**~ File size:** __{humanbytes(amjana.file.size)}__
NOTE: Bandwidth limit is 1MB/s. After a month files will be deleted.'''
	await msg.edit(hmm, buttons=(
		[Button.url('📦 Download', r3.json()['url'])],
		[Button.url('Support Chat 💭', 't.me/hxsupport')]
		))

	os.remove(result.name)
