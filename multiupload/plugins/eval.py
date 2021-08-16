#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) oVoIndia | oVo-HxBots

import asyncio
import io
import os
import sys
import traceback
from telethon import events
from multiupload import anjana


async def bash(cmd):

	process = await asyncio.create_subprocess_shell(
		cmd,
		stdout=asyncio.subprocess.PIPE,
		stderr=asyncio.subprocess.PIPE,
	)
	stdout, stderr = await process.communicate()
	err = stderr.decode().strip()
	out = stdout.decode().strip()
	return out, err

@anjana.on(events.NewMessage(pattern='^/bash ?(.*)'))
async def runner(event):
	kk = await event.get_chat()
	if kk.id == int(os.environ.get("OWNRID")):
		pass
	else:
		return await anjana.send_message(event.chat_id, "You are not a Developer")

	cmd = "".join(event.message.message.split(maxsplit=1)[1:])
	out, err = await bash(cmd)
	if out:
		await anjana.send_message(event.chat_id, f'**CMD:** `{cmd}`\n**OUTPUT:**\n `{out}`')
	elif err:
		await anjana.send_message(event.chat_id, f'**CMD:** `{cmd}`\n**ERROR:**\n `{err}`')
	elif out and err:
		await anjana.send_message(event.chat_id, f'**CMD:** `{cmd}`\n**ERROR:**\n `{err}`\n**OUTPUT:**\n `{out}`')
	else:
		await anjana.send_message(event.chat_id, f'**CMD:** `{cmd}`')

@anjana.on(events.NewMessage(pattern='^/eval ?(.*)'))
async def evaluation_cmd_t(event):
	kk = await event.get_chat()
	if kk.id == int(os.environ.get("OWNRID")):
		pass
	else:
		return await anjana.send_message(event.chat_id, "You are not a Developer")

	status_message = await event.reply("Processing...")

	cmd = event.message.message.split(" ", maxsplit=1)[1]

	old_stderr = sys.stderr
	old_stdout = sys.stdout
	redirected_output = sys.stdout = io.StringIO()
	redirected_error = sys.stderr = io.StringIO()
	stdout, stderr, exc = None, None, None

	try:
		await aexec(cmd, event)
	except Exception:
		exc = traceback.format_exc()

	stdout = redirected_output.getvalue()
	stderr = redirected_error.getvalue()
	sys.stdout = old_stdout
	sys.stderr = old_stderr

	evaluation = ""
	if exc:
		evaluation = exc
	elif stderr:
		evaluation = stderr
	elif stdout:
		evaluation = stdout
	else:
		evaluation = "Success"

	final_output = "**EVAL**: ```{}```\n\n**OUTPUT**:\n```{}``` \n".format(cmd, evaluation.strip())

	if len(final_output) > 4096:
		with open("eval.text", "w+", encoding="utf8") as out_file:
			out_file.write(str(final_output))
		await status_message.reply(
			file="eval.text",
			text=cmd
		)
		os.remove("eval.text")
		await status_message.delete()
	else:
		await status_message.edit(final_output)


async def aexec(code, event):
	exec(
		f'async def __aexec(event): ' +
		''.join(f'\n {l}' for l in code.split('\n'))
	)
	return await locals()['__aexec'](event)