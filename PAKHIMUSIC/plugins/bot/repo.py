from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PAKHIMUSIC import app
from config import BOT_USERNAME

start_txt = """**
✪ 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐌𝐔𝐒𝐈𝐂 𝐑𝐄𝐏𝐎 ✪
 
𝐂𝐋𝐈𝐂𝐊 𝐁𝐄𝐋𝐎𝐖 𝐁𝐔𝐓𝐓𝐎𝐍 𝐓𝐎 𝐆𝐄𝐓 𝐑𝐄𝐏𝐎
**"""

@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
     
            [ 
            InlineKeyboardButton("✭ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ✭", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
     
            [
             InlineKeyboardButton("⎯꯭‌✭𝆺꯭𝅥ᴿᴱᴾᴼ .𓈀✔", url="https://t.me/friendship_forever_group143"),
             InlineKeyboardButton("⎯꯭‌✭𝆺꯭𝅥𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁✭", url="https://t.me/InnocentIdkaaa"),
             ],
    
       ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/5730046b13f9755ebe5bc.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
