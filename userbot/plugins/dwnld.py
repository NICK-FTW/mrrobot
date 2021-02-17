from pyrogram import filters

from userbot import UserBot

@UserBot.on_message(filters.command('sample', ['.']))
async def module_name(client, message):
    await message.edit(
        "This is a sample module"
    )
