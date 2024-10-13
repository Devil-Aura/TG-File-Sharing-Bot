#Nothing is here


































from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import OWNER_ID  # Import owner ID from config.py

# Command handler for /dev
@Client.on_message(filters.command("dev"))
async def dev_command(client: Client, message: Message):
    await message.reply_text(
        text = f"<b>○   Oᴡɴᴇʀ - </b> <a href='tg://user?id={OWNER_ID}'>Devil</a>\n"
               f"<b>○   Dᴇᴠᴇʟᴏᴘᴇʀ - </b> <a href='https://t.me/IamRealDevil'>Cʟɪᴄᴋ Hᴇʀᴇ</a>\n"
               f"<b>○   Cʜᴀɴɴᴇʟ - </b> <a href='https://t.me/CrunchyRollOfficialChannel'>Aɴɪᴍᴇ Channel</a>\n"
               f"<b>○   Cʜᴀɴɴᴇʟ - </b> <a href='https://t.me/CrunchyRollOfficialChannel'>Jᴏɪɴ Nᴏᴡ</a>\n"
               f"<b>○   Cʜᴀɴɴᴇʟ - </b> <a href='https://t.me/CrunchyRollOfficialChannel'>Jᴏɪɴ Nᴏᴡ</a>\n"
               f"<b>○   Dɪsᴄᴜssɪᴏɴ Gʀᴏᴜᴘ - </b> <a href='https://t.me/+RyYOjVpfNMFmN2Q1'>Jᴏɪɴ Nᴏᴡ</a>",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⚡Cʟᴏsᴇ", callback_data="close"),
                    InlineKeyboardButton('⛄Aɴɪᴍᴇ Channel', url='https://t.me/CrunchyRollOfficialChannel')
                ]
            ]
        )
    )

# Callback query handler
@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    data = query.data
    if data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

