from functools import wraps

import heroku3

from Panda import Config
from Panda._func.decorators import Panda_cmd as ilhammansiz_on_cmd
from Panda._func._helpers import (
    edit_or_reply,
    edit_or_send_as_file,
    get_text,
)

from . import HELP


HELP(
    "heroku",
)

heroku_client = None
if Config.HEROKU_API_KEY:
    heroku_client = heroku3.from_key(Config.HEROKU_API_KEY)


def _check_heroku(func):
    @wraps(func)
    async def heroku_cli(client, message):
        heroku_app = None
        if not heroku_client:
            await edit_or_reply(
                message, "`Please Add Heroku API Key For This To Function To Work!`"
            )
        elif not Config.HEROKU_APP_NAME:
            await edit_or_reply(
                message, "`Please Add Heroku APP Name For This To Function To Work!`"
            )
        if Config.HEROKU_APP_NAME and heroku_client:
            try:
                heroku_app = heroku_client.app(Config.HEROKU_APP_NAME)
            except:
                await edit_or_reply(
                    message, "`Heroku Api Key And App Name Doesn't Match!`"
                )
            if heroku_app:
                await func(client, message, heroku_app)

    return heroku_cli


@ilhammansiz_on_cmd(
    ["reboot"],
    cmd_help={"help": "Restart Your Userbot On HEROKU!", "example": "{ch}restart"},
)
@_check_heroku
async def gib_restart(client, message, hap):
    await edit_or_reply(message, "`[HEROKU] - 🔁 Restarting 🔁`")
    hap.restart()


@ilhammansiz_on_cmd(
    ["logs"], cmd_help={"help": "Get Logs From HEROKU!", "example": "{ch}logs"}
)
@_check_heroku
async def gib_logs(client, message, happ):
    msg_ = await edit_or_reply(message, "`Please Wait!`")
    logs = happ.get_log()
    capt = f"Heroku Logs Of {Config.HEROKU_APP_NAME}"
    await edit_or_send_as_file(logs, msg_, client, capt, "logs")


@ilhammansiz_on_cmd(
    ["setvar"],
    cmd_help={
        "help": "Set Var From telegram Itself, Please Seperate Var And Value With '|'",
        "example": "{ch}setvar LOAD_UNOFFICIAL_PLUGINS False",
    },
)
@_check_heroku
async def set_varr(client, message, app_):
    msg_ = await edit_or_reply(message, "`Please Wait!`")
    heroku_var = app_.config()
    _var = get_text(message)
    if not _var:
        await msg_.edit("`Here is Usage Syntax : .setvar KEY VALUE`")
        return
    if not " " in _var:
        await msg_.edit("`Here is Usage Syntax : .setvar KEY VALUE`")
        return
    var_ = _var.split(" ", 1)
    if len(var_) > 2:
        await msg_.edit("`Here is Usage Syntax : .setvar KEY VALUE`")
        return
    _varname, _varvalue = var_
    await msg_.edit(f"`Variable {_varname} Added With Value {_varvalue}!`")
    heroku_var[_varname] = _varvalue


@ilhammansiz_on_cmd(
    ["delvar"],
    cmd_help={
        "help": "Delete Var From telegram Itself",
        "example": "{ch}delvar LOAD_UNOFFICIAL_PLUGINS",
    },
)
@_check_heroku
async def del_varr(client, message, app_):
    msg_ = await edit_or_reply(message, "`Please Wait!`")
    heroku_var = app_.config()
    _var = get_text(message)
    if not _var:
        await msg_.edit("`Give Var Name As Input!`")
        return
    if not _var in heroku_var:
        await msg_.edit("`This Var Doesn't Exists!`")
        return
    await msg_.edit(f"`Sucessfully Deleted {_var} Var!`")
    del heroku_var[_var]
