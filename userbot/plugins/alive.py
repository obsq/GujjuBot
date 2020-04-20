"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("Hey,this is a message from my master @obsquriel..Oh shit..I should have never called him by name..forgive me master^.^\n\nMessage goes like this●●●\nIf any one want to talk with me first take approval from my bot.. if you get approval also I will be taking with you only if Iam free--by @obsquriel\n\n\nAll read the message?? Okay..there is no need to take approval to join my masters channel @crackedapps_obsq 【Remember that if channel attains 1k subs he will give bots like me free..】\nNever spam in my master's inbox... I will block you.. okay?Don't make my master angry\nFree approval for malayalees.. yeah keri va makkale\n\n`"
                     f"`My owner`: {DEFAULTUSER}\n\n"
                     "`Bot name:obsqofficialbot(jinn)\nfork by:` @obsquriel\n"
                     "`Database Status: Databases functioning normally!\n\nAlways with you, my master!\n`")
                     
