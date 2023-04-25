import os
import random
import requests
from datetime import datetime
from sys import version_info
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import app
from YukkiMusic.utils.decorators.admins import AdminActual
from strings import get_command



disable_cut = []

@app.on_message(
filters.command(["المطور","السورس"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/7f87be8bf898631bc70f5.jpg",
        caption=f""" 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝗍𝗈 𝗍𝗁𝖾 𝗆𝗈𝗈𝗇 𝗆𝗎𝗌𝗂𝖼 𝖻𝗈𝗍 .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "𝖺𝖡𝗌 𝖠𝗁𝗆𝖾𝖽", url=f"https://t.me/r6r8r")
                ],[
                    InlineKeyboardButton(
                       "𝖬𝗒 𝖲𝖳𝗎𝖿𝖿", url=f"https://t.me/UZZDD")
              
                 ],

            ]

        ),

    )
