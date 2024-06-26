import asyncio

from PAKHIMUSIC import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


@app.on_message(filters.command(["ping","alive"]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://graph.org/file/e999c40cb700e7c684b75.mp4",
        caption=_["ping_1"].format(app.mention),
        )
    pytgping = await Anony.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
        reply_markup=InlineKeyboardMarkup(
              [
            InlineKeyboardButton(
                text="⎯꯭‌✭𝆺꯭𝅥𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁✭", url=f"https://t.me/InnocentIdkaaa"
            ),
            InlineKeyboardButton(
                text="⎯꯭‌✭𝆺꯭𝅥𝚂𝚄𝙿𝙿𝙾𝚁𝚃✭", url=f"https://t.me/friendship_forever_group143"
            ),
        ],
                [
            InlineKeyboardButton(
                text="⎯꯭‌✭𝆺꯭𝅥𝚄𝙿𝙳𝙰𝚃𝙴✭", url=f"https://t.me/manmarziiyaan"
            ),
                ],
                [
                    InlineKeyboardButton(
                        "⛧ᴄʟᴏsᴇ⛧", callback_data="close"
                    )
                ],
            ],
        )
    )
