import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("𝐘𝐨𝐮𝐫 𝐕𝐞𝐫𝐲 𝐥𝐮𝐜𝐤𝐲 🤞 𝐈 𝐚𝐦 𝐚𝐥𝐢𝐯𝐞 ❤️ 𝐩𝐫𝐞𝐬𝐬 /start 𝐮𝐬𝐞 𝐦𝐞")


@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")
