import os
import logging
from pyrogram import Client, filters
from telegraph import upload_file
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

Webot = Client(
   "Telegraph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Webot.on_message(filters.command("tgstart"))
async def start(client, message):
   if message.chat.type == 'private':
       await Webot.send_message(
               chat_id=message.chat.id,
               text="""<b>Hey There, I'm Telegraph Bot

I can upload photos or videos to telegraph. Made by @SOULxDED  

Hit /help button to find out more about how to use me</b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "NoBita", url="t.me/SOULxDED"),
                                        InlineKeyboardButton(
                                            "RiZoel", url="https://t.me/TheRiZoeL")
                                    ],[
                                      InlineKeyboardButton(
                                            "Support Group", url="https://t.me/GROUP_OF_HELL")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Webot.on_message(filters.command("helptg"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Webot.send_message(
               chat_id=message.chat.id,
               text="""<b>Telegraph Bot Help!

Just send a photo or video less than 5mb file size, I'll upload it to telegraph.

~ @GROUP_OF_HELL</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "NoBita", url="t.me/SOULxDED"),
                                        InlineKeyboardButton(
                                            "RiZoel", url="t.me/TheRiZoeL"),
                                  ],[
                                        InlineKeyboardButton(
                                            "Support Group", url="https://t.me/GROUP_OF_HELL")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Webot.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await Webot.send_message(
               chat_id=message.chat.id,
               text="""<b>About Telegraph Bot!</b>

<b>♞ owner:</b> <a href="https://t.me/SOULXDED">NoBita </a>

<b>♞ Support:</b> <a href="https://t.me/GROUP_OF_HELL">Michael Support </a>

<b>♞ GitHub:</b> <a href="https://github.com/archangelmichael01">here </a>

<b>~ @Its_Michael_robot</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="help"),
                                        InlineKeyboardButton(
                                            "Support Group", url="https://t.me/GROUP_OF_HELL")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Webot.on_message(filters.photo.command("telegraph"))
async def telegraphphoto(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Photo size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}\n\nJoin @GROUP_OF_HELL**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Webot.on_message(filters.video.command("telegraph"))
async def telegraphvid(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Video size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}\n\nJoin @GROUP_OF_HELL**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Webot.on_message(filters.animation.command("telegraph"))
async def telegraphgif(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Gif size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}\n\nJoin @GROUP_OF_HELL**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Webot.on_callback_query()
async def button(bot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(bot, update.message)
      elif "about" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
      elif "start" in cb_data:
        await update.message.delete()
        await start(bot, update.message)
      elif "telegraph" in cb_data:
        await update.message.delete()
        await telegraph(bot, update.message)

print(
    """
Bot Started!
Join @camila_support
"""
)

Webot.run()
