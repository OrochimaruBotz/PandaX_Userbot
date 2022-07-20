from datetime import datetime

from Panda._func.decorators import Panda_cmd as ilhammansiz_on_cmd
from Panda._func._func._helpers import edit_or_reply


@ilhammansiz_on_cmd(
    ["stats", "stat"],
    cmd_help={
        "help": "Shows user account stats!",
        "example": "{ch}stats",
    },
)
async def stats(client, message):
    pablo = await edit_or_reply(message, f"`Processing...`")
    start = datetime.now()
    u = 0
    g = 0
    sg = 0
    c = 0
    b = 0
    a_chat = 0
    async for dialog in client.iter_dialogs():
        if dialog.chat.type == "private":
            u += 1
        elif dialog.chat.type == "bot":
            b += 1
        elif dialog.chat.type == "group":
            g += 1
        elif dialog.chat.type == "supergroup":
            sg += 1
            user_s = await dialog.chat.get_member(int(client.me.id))
            if user_s.status in ("creator", "administrator"):
                a_chat += 1
        elif dialog.chat.type == "channel":
            c += 1

    end = datetime.now()
    ms = (end - start).seconds
    await pablo.edit(
        """`Your Stats Obtained in {} seconds`
`You have {} Private Messages.`
`You are in {} Groups.`
`You are in {} Super Groups.`
`You Are in {} Channels.`
`You Are Admin in {} Chats.`
`Bots = {}`""".format(
            ms, u, g, sg, c, a_chat, b
        )
    )
