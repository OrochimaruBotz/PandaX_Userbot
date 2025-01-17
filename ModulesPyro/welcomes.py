from pyrogram import filters

from Panda.database.welcomedb import add_welcome, del_welcome, welcome_info
from Panda import Config
from Panda._func.decorators import Panda_cmd as ilhammansiz_on_cmd, listen
from Panda._func._helpers import edit_or_reply
from . import HELP

HELP(
    "welcomes",
)


@ilhammansiz_on_cmd(
    ["setwelcome"],
    cmd_help={
        "help": "Save Welcome Message!",
        "example": "{ch}setwelcome (text/reply to welcome message)",
    },
)
async def save_welcome(client, message):
    note_ = await edit_or_reply(message, "`Processing..`")
    msg = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        msg = message.reply_to_message
    if not msg:
        return await edit_or_reply(message, "**Berikan Sebuah Pesan atau Reply**")
    cool = await client.copy_message(Config.LOG_GRP, message.chat.id, msg.message_id)
    add_welcome(str(message.chat.id), cool.message_id)
    await note_.edit(f"`Done! Welcome Message Saved!`")


@listen(filters.new_chat_members & filters.group)
async def welcomenibba(client, message):
    if not message:
        
        return
    if not welcome_info(str(message.chat.id)):
        
        return
    if not message.chat:
        
        return
    is_m = False
    sed = welcome_info(str(message.chat.id))
    m_s = await client.get_messages(Config.LOG_GRP, sed["msg_id"])
    if await is_media(m_s):
        text_ = m_s.caption or ""
        is_m = True
    else:
        text_ = m_s.text or ""
    if text_ != "":
        mention = message.new_chat_members[0].mention
        user_id = message.new_chat_members[0].id
        user_name = message.new_chat_members[0].username or "No Username"
        first_name = message.new_chat_members[0].first_name
        last_name = message.new_chat_members[0].last_name or "No Last Name"
        text_ = text_.format(mention=mention, user_id=user_id, user_name=user_name, first_name=first_name, last_name=last_name)
    if not is_m:
        await client.send_message(
            message.chat.id,
            text_,
            reply_to_message_id=message.message_id)
    else:
        await m_s.copy(
            chat_id=str(message.chat.id),
            caption=text_,
            reply_to_message_id=message.message_id,
        )
    
    
    
async def is_media(message):
    if not (message.photo or message.video or message.document or message.audio or message.sticker or message.animation or message.voice or message.video_note):
        return False
    return True


@ilhammansiz_on_cmd(
    ["delwelcome"],
    cmd_help={"help": "Delete welcome Message!", "example": "{ch}delwelcome"},
)
async def del_welcomez(client, message):
    note_ = await edit_or_reply(message, "`Processing..`")
    if not welcome_info(str(message.chat.id)):
        await note_.edit("`Welcome Message Not Found In This Chat!`")
        return
    del_welcome(str(message.chat.id))
    await note_.edit(f"`Welcome Message Deleted Successfully!`")


@ilhammansiz_on_cmd(
    ["welcome"],
    cmd_help={"help": "Current Welcome Message!", "example": "{ch}welcome"},
)
async def show_welcome(client, message):
    pablo = await edit_or_reply(message, "`Processing..`")
    sed = welcome_info(str(message.chat.id))
    if sed is False:
        await pablo.edit("`No Welcome Found In This Chat...`")
        return
    mag = f""" Welcome Message In Correct Chat Is :"""
    await client.copy_message(
        from_chat_id=Config.LOG_GRP,
        chat_id=str(message.chat.id),
        message_id=sed["msg_id"],
        reply_to_message_id=message.message_id,
    )
    await pablo.edit(mag)
