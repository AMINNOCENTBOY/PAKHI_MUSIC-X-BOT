import time
import asyncio
import random
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
import config
from PAKHIMUSIC import app
from PAKHIMUSIC.misc import _boot_
from PAKHIMUSIC.plugins.sudo.sudoers import sudoers_list
from PAKHIMUSIC.utils.database import get_served_chats, get_served_users, get_sudoers
from PAKHIMUSIC.utils import bot_sys_stats
from PAKHIMUSIC.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from PAKHIMUSIC.utils.decorators.language import LanguageStart
from PAKHIMUSIC.utils.formatters import get_readable_time
from PAKHIMUSIC.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS, AMOP
from strings import get_string

EMOJIOS = [
    "❤️",
    "🧡",
    "💛",
    "💚",
    "💙",
    "💜",
    "🤎",
    "🖤",
    "🤍",
    "♥️",
]

STICKER = [
"CAACAgUAAx0Cd9xEawACEQlmLuvFijxhTZXjFbLPOsZFBoZzYQAC2AUAAkVZsVftrDRpvXZTAAE0BA",
"CAACAgUAAx0Cd9xEawACEQhmLuvFeujHQdaxeDtr3MZThRXa1QACkgcAArZSuVfbJAABQq5pIc80BA",
"CAACAgUAAx0Cd9xEawACEQdmLuvFQdwX-ySKIrmq-JPWItfhhgACwQUAAi9GuVfYV7lLP7xl4zQE",
"CAACAgUAAx0Cd9xEawACEQVmLuuiUNrymw5wWSie-agvZ-_MdgACNAQAAi9GsFf3M2dSfxH-YDQE",
"CAACAgUAAx0Cd9xEawACEQNmLuuKwCEUmunIPFoxUL1Kr2Dp1AAChQgAApAXsFeIwfQvrfbmjjQE",
"CAACAgUAAx0Cd9xEawACEQJmLut22O_5LobAKvCBNlOHbCnQcQAC8gQAAmRQsVdeP26A2AJofzQE",
"CAACAgUAAx0Cd9xEawACEQABZi7rYhnPjPsm_g37JvqoH7qB10gAAsgEAAJWgShXcBbC69nedAY0BA",
"CAACAgUAAx0Cd9xEawACEP9mLutgBdWYCVPqQ_kvUGgYoNVIVwACrAYAAof0IFc6sUwgfJZw6zQE",
"CAACAgEAAx0Cd9xEawACEPtmLusPo3kBvdEigRxbcqGOMSF9cgAC8wMAAqpT6UU55jSF8wAByTc0BA",
"CAACAgEAAx0Cd9xEawACEPpmLusJTIEch-TXN5KsPkvdfnypNgACbwIAAkoY6UUP_O3RGOXeSTQE",
"CAACAgEAAx0Cd9xEawACEPlmLusBSvWNswwz99iOXBMIos0s_QACGAMAAtfI6EX4deIoUongJDQE",
"CAACAgEAAx0Cd9xEawACEPdmLuropCmTrN0Xv4_C7plvS45D3gACrwIAAqyx6EVOdFVb4d8VsDQE",
"CAACAgUAAx0Cd9xEawACEOhmLurMc76ZYy9ZWB0dcuWfNJVSzQACLwUAAk-LuVelZAHYP-pxnTQE",
"CAACAgUAAx0Cd9xEawACEOZmLuq8MMZnoz-txKJ9QEow9qDKxQACKwQAAvbXuVf7GDiuoypXFzQE",
"CAACAgUAAx0Cd9xEawACEORmLuq3Mm3dzamR5W8JZhZHgbPWKwACJwcAAvQcsFefMIzhat8ZtDQE",
"CAACAgUAAx0Cd9xEawACEONmLuqxMsLOLjCsMIf86_QuZH0AAaAAAusMAAIRzNhVUrENdULkjis0BA",
"CAACAgUAAx0Cd9xEawACEOFmLuqryqMN4_7KPq_LLZNIq0OPEgACJAwAAm5mwVXkZ2Ycjy1rRjQE",
"CAACAgUAAx0Cd9xEawACEN9mLuqlG8RAw-L8e1Pv3909WrYMhgACwBUAAh-sOVQ3vSSCUJbSYzQE",
]


ANNIE_VID = [
"https://telegra.ph/file/1726f9434ef52f54c12eb.mp4",
"https://telegra.ph/file/a4d90b0cb759b67d68644.mp4",
"https://telegra.ph/file/c6c1ac9aee4192a8a3747.mp4",
"https://telegra.ph/file/2b75449612172a96d4599.mp4",
"https://telegra.ph/file/0b53cfe4a712af439d50f.mp4",
"https://telegra.ph/file/64291485c422535f0143d.mp4",
"https://telegra.ph/file/30ec7c936db6cd2ce7c61.mp4",
"https://telegra.ph/file/e8bcb814e2c52c11a0f1d.mp4",
"https://telegra.ph/file/9b7e1b820c72a14d90be7.mp4",
"https://telegra.ph/file/37d1815385f8244f9a282.mp4"


]




@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            return await message.reply_video(
                random.choice(ANNIE_VID),
                caption=_["help_1"].format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
            )
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("🔎")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = _["start_6"].format(
                title, duration, views, published, channellink, channel, app.mention
            )
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=_["S_B_8"], url=link),
                        InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_CHAT),
                    ],
                ]
            )
            await m.delete()
            await app.send_video(
                chat_id=message.chat.id,
                video=thumbnail,
                caption=searched_text,
                reply_markup=key,
            )
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
    else:
        out = private_panel(_)
        accha = await message.reply_text(
            text=random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("👻")
        await asyncio.sleep(0.2)
        await accha.edit("✨")
        await asyncio.sleep(0.2)
        await accha.edit("🥀")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await message.reply_sticker(sticker=random.choice(STICKER))
        await asyncio.sleep(2)
        await umm.delete()
        await message.reply_video(
            random.choice(ANNIE_VID),
            caption=_["start_2"].format(message.from_user.mention, app.mention),
            reply_markup=InlineKeyboardMarkup(out),
        )
        if await is_on_off(2):
            return await app.send_message(
                chat_id=config.LOGGER_ID,
                text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
            )

@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_video(
        random.choice(ANNIE_VID),
        caption=_["start_1"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
    )
    return await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass
            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)
                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)
                await message.reply_video(
                    random.choice(ANNIE_VID),
                    caption=_["start_3"].format(
                        message.from_user.mention,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)
