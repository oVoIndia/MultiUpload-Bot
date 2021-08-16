#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) oVoIndia | oVo-HxBots


import math
import time, aiohttp, asyncio
from datetime import datetime
from multiupload.fastdl import download_file as downloadable

async def progress(current, total, event, start, type_of_ps):
    """Generic progress_callback for both
    upload.py and download.py"""
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "[{0}{1}]\n● **Percent:** {2}%\n".format(
            "".join(["◾️" for i in range(math.floor(percentage / 12.5))]),
            "".join(["▫️" for i in range(8 - math.floor(percentage / 12.5))]),
            round(percentage, 2),
        )
        tmp = progress_str + "● **Status:** {0} of {1}\n● **Speed:** {2}/s\n● **ETA:** {3}".format(
            humanbytes(current), humanbytes(total), humanbytes(speed), time_formatter(estimated_total_time)
        )
        await event.edit("{}\n {}".format(type_of_ps, tmp))

'''async def tgdownloader(amjana, msg):
    k = time.time()
    pamka = "./downloads/"
    await msg.edit("Processing...")
    file_path = await amjana.download_media(
                progress_callback=lambda pamka, t: asyncio.get_event_loop().create_task(
                    progress(pamka, t, msg, k, f"**🏷 Downloading...\n➲ File Name: {amjana.file.name}**")
                )
            )
    return file_path'''
    

async def downloader(filename, file, event, taime, msg):
    d = "downloads/"
    t = time_formatter(((datetime.now() - datetime.now()).seconds) * 1000)
    with open(filename, "wb") as fk:
        result = await downloadable(
            client=event.client,
            location=file,
            out=fk,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d,
                    t,
                    event,
                    taime,
                    msg,
                ),
            ),
        )
    return result
    

def convert_from_bytes(size):
    power = 2 ** 10
    n = 0
    units = {0: "", 1: "kilobytes", 2: "megabytes", 3: "gigabytes", 4: "terabytes"}
    while size > power:
        size /= power
        n += 1
    return f"{round(size, 2)} {units[n]}"


def humanbytes(size):
    """Input size in bytes,
    outputs in a human readable format"""
    # https://stackoverflow.com/a/49361727/4723940
    if not size:
        return ""
    # 2 ** 10 = 1024
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "K", 2: "M", 3: "G", 4: "T"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


def time_formatter(milliseconds: int) -> str:
    """Inputs time in milliseconds, to get beautified time,
    as string"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + " day(s), ") if days else "")
        + ((str(hours) + " hour(s), ") if hours else "")
        + ((str(minutes) + " minute(s), ") if minutes else "")
        + ((str(seconds) + " second(s), ") if seconds else "")
        + ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    )
    return tmp[:-2]


async def download_file(url, file_name, message, start_time, bot):
    async with aiohttp.ClientSession() as session:
        time.time()
        await download_coroutine(session, url, file_name, message, start_time, bot)
    return file_name
