import asyncio

from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from AnonXMusic import app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.utils import get_readable_time
from AnonXMusic.utils.database import (
    add_banned_user,
    get_banned_count,
    get_banned_users,
    get_served_chats,
    is_banned_user,
    remove_banned_user,
)
from AnonXMusic.utils.decorators.language import language
from AnonXMusic.utils.extraction import extract_user
from config import BANNED_USERS, OWNER_ID
import config 


@app.on_message(filters.command(["gban", "globalban"]) & SUDOERS)
@language
async def global_ban(client, message: Message, _):
    if not message.reply_to_message and len(message.command) < 3:
        return await message.reply_text("Usage: /gban <user> <reason>")
    
    user = await extract_user(message)
    reason = " ".join(message.command[2:]) if len(message.command) > 2 else None
    
    if not reason:
        return await message.reply_text("You must provide a reason for the global ban!")

    if user.id == message.from_user.id:
        return await message.reply_text(_["gban_1"])
    elif user.id == app.id:
        return await message.reply_text(_["gban_2"])
    elif user.id in SUDOERS:
        return await message.reply_text(_["gban_3"])
    
    is_gbanned = await is_banned_user(user.id)
    if is_gbanned:
        return await message.reply_text(_["gban_4"].format(user.mention))

    if user.id not in BANNED_USERS:
        BANNED_USERS.add(user.id)

    served_chats = await get_served_chats()
    time_expected = get_readable_time(len(served_chats))
    
    mystic = await message.reply_text(f"Banning {user.mention} globally...\nExpected time: {time_expected}")
    
    number_of_chats = 0
    for chat in served_chats:
        try:
            await app.ban_chat_member(chat["chat_id"], user.id)
            number_of_chats += 1
        except FloodWait as fw:
            await asyncio.sleep(int(fw.value))
        except:
            continue

    await add_banned_user(user.id)
    
    await message.reply_text(
        f"✅ {user.mention} has been globally banned in {number_of_chats} chats.\n\nReason: {reason}"
    )
    await mystic.delete()

    owner_id = config.OWNER_ID
    await app.send_message(
        owner_id,
        f"**Global Ban Alert**\n\n"
        f"Admin: {message.from_user.mention} (`{message.from_user.id}`)\n"
        f"Banned User: {user.mention} (`{user.id}`)\n"
        f"Reason: {reason}\n"
        f"Affected Chats: {number_of_chats}"
    )


@app.on_message(filters.command(["ungban"]) & SUDOERS)
@language
async def global_un(client, message: Message, _):
    if not message.reply_to_message and len(message.command) < 3:
        return await message.reply_text("Usage: /ungban <user> <reason>")
    
    user = await extract_user(message)
    reason = " ".join(message.command[2:]) if len(message.command) > 2 else None
    
    if not reason:
        return await message.reply_text("You must provide a reason for the unban!")

    is_gbanned = await is_banned_user(user.id)
    if not is_gbanned:
        return await message.reply_text(_["gban_7"].format(user.mention))

    owner_id = config.OWNER_ID
    confirm_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("Confirm", callback_data=f"confirm_unban_{user.id}_{message.from_user.id}_{reason}")],
        [InlineKeyboardButton("Cancel", callback_data="cancel_unban")]
    ])

    await app.send_message(
        owner_id,
        f"**Unban Request**\n\n"
        f"Admin: {message.from_user.mention} (`{message.from_user.id}`)\n"
        f"User: {user.mention} (`{user.id}`)\n"
        f"Reason: {reason}\n\n"
        f"Do you want to approve this unban?",
        reply_markup=confirm_markup
    )
    await message.reply_text("Unban request sent to the owner for approval.")


@app.on_callback_query(filters.regex(r"confirm_unban_(\d+)_(\d+)_(.+)"))
async def confirm_unban(client, query: CallbackQuery):
    _, user_id, admin_id, reason = query.data.split("_")
    user_id = int(user_id)
    admin_id = int(admin_id)

    is_gbanned = await is_banned_user(user_id)
    if not is_gbanned:
        return await query.answer("User is not globally banned!", show_alert=True)

    if user_id in BANNED_USERS:
        BANNED_USERS.remove(user_id)

    served_chats = await get_served_chats()
    number_of_chats = 0
    for chat in served_chats:
        try:
            await app.unban_chat_member(chat["chat_id"], user_id)
            number_of_chats += 1
        except FloodWait as fw:
            await asyncio.sleep(int(fw.value))
        except:
            continue

    await remove_banned_user(user_id)

    await query.message.edit_text(
        f"✅ Unban approved!\n\nUser: `{user_id}`\nReason: {reason}\nAffected Chats: {number_of_chats}"
    )

    await app.send_message(
        admin_id,
        f"✅ Your unban request for `{user_id}` has been approved!\n\nReason: {reason}"
    )


@app.on_callback_query(filters.regex("cancel_unban"))
async def cancel_unban(client, query: CallbackQuery):
    await query.message.edit_text("❌ Unban request has been cancelled.")

@app.on_message(filters.command(["gbannedusers", "gbanlist"]) & SUDOERS)
@language
async def gbanned_list(client, message: Message, _):
    counts = await get_banned_count()
    if counts == 0:
        return await message.reply_text(_["gban_10"])
    mystic = await message.reply_text(_["gban_11"])
    msg = _["gban_12"]
    count = 0
    users = await get_banned_users()
    for user_id in users:
        count += 1
        try:
            user = await app.get_users(user_id)
            user = user.first_name if not user.mention else user.mention
            msg += f"{count}➤ {user}\n"
        except Exception:
            msg += f"{count}➤ {user_id}\n"
            continue
    if count == 0:
        return await mystic.edit_text(_["gban_10"])
    else:
        return await mystic.edit_text(msg)