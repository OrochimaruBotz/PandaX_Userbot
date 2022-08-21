# Copyright (C) 2020 Catuserbot <https://github.com/sandy1709/catuserbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# ••••••••••••••••••••••√•••••••••••••√√√••••••••
from pyrogram import __version__ as pyrover
import sys
import Panda
from Panda import utils
LOGS = Panda.core.logger.logging.getLogger("PandaUserbot")
from .utils import P, M, V, A
from .Session.multisession_ import Pyrogram, Telethon


## Memulai ••••••••••√√√√√•••••••

try:
    LOGS.info(Panda.__copyright__)
    LOGS.info("Licensed under the terms of the " + Panda.__license__)
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()

## Install Modules ••••••√√√√√••••••
cmdhr = Panda.Config.COMMAND_HAND_LER

MSG_ON = """
Gojo-Userbot
━━
Pyrogram Version - `{}'
Ketik `{}alive` untuk Mengecheck Bot
━━
"""

async def memulai():
    await utils.loads(f"{P}")
    await utils.loads(f"{M}")
    await utils.buka(f"{V}")
    await utils.buka(f"{A}")
    


def start():
    if Panda.PandaBot:
        Panda.PandaBot.loop.run_until_complete(memulai())
        Panda.PandaBot.loop.run_until_complete(utils.join())
        Panda.PandaBot.loop.run_until_complete(utils.ongrup())
        LOGS.info(f"꧁༺ Gojo Userbot ༻꧂\n⚙️ Version:{Panda.__version__} [TELAH DIAKTIFKAN]")


async def ongruppyro():
    if Panda.pyrobot:
        try:
            await Panda.pyrobot.send_message(BOTLOG_CHATID, MSG_ON.format(pyrover, cmdhr))
            if Panda.pyrobot2:
                await Panda.pyrobot2.send_message(BOTLOG_CHATID, MSG_ON.format(pyrover, cmdhr))
            if Panda.pyrobot3:
                await Panda.pyrobot3.send_message(BOTLOG_CHATID, MSG_ON.format(pyrover, cmdhr))
            if Panda.pyrobot4:
                await Panda.pyrobot4.send_message(BOTLOG_CHATID, MSG_ON.format(pyrover, cmdhr))
            LOGS.info(f"꧁༺ Gojo Userbot ༻꧂\n⚙️ PyroVersion:{pyrover} [TELAH DIAKTIFKAN]")
        except Exception:
            pass
                  
    
def startpyro():
    if Panda.pyrobot:
        Panda.pyrobot.loop.run_until_complete(ongruppyro())
        LOGS.info(f"꧁༺ Gojo Userbot ༻꧂\n⚙️ PyroVersion:{pyrover} [TELAH DIAKTIFKAN]")
                   
      

if __name__ == "__main__":
    Telethon()
    start()
    Pyrogram()
    startpyro()
    
    
  
if Panda.PandaBot:
    try:
        if len(sys.argv) not in (1, 3, 4):
            Panda.PandaBot.disconnect()
        else:
            Panda.PandaBot.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
