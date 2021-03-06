# Copyright (C) 2021 By AmortMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐**ูุฑุญุจุข ุนุฒูุฒูโคใ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) ใ!**\n
๐ฏยฆ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) **
๐นยฆ ** ูุชูุญ ูู ุชุดุบูู ุงูููุณููู ูุงูููุฏูู ูู ูุฌููุนุงุช ูู ุฎูุงู ุงูููุงููุงุช ุงูุฌุฏูุฏุฉ ูู Telegram! **
๐ยฆ ** ุงูุชุดู ุฌููุน ุฃูุงูุฑ ุงูุจูุช ูููููุฉ ุนูููุง ูู ุฎูุงู ุงูููุฑ ุนูู ุฒุฑ ยป๐ ุงูุฃูุงูุฑ! **
๐ยฆ ** ููุนุฑูุฉ ููููุฉ ุงุณุชุฎุฏุงู ูุฐุง ุงูุจูุช ุ ูุฑุฌู ุงูููุฑ ููู ยป ุฒุฑ ุดุฑูุญูุงุช ุงูุจููุช **
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โ๏ธ๏ธุงุถูููู ุฅูููู ูุฌูููุนูุชู..",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton(" ๐๏ธุดุฑูุญูุงุช ุงูุจููุช", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("๐ผ๏ธุงููุฃูุงูููุฑ", callback_data="cbbasic"),
                    InlineKeyboardButton("๐ธ๏ธุงููููููุทูุฑ", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "๐ฏ๏ธููุงุฉ ุงูุจูุช", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "๐๏ธุงููุฏุนูู", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "๐ง๏ธุขููุณูููุฑุณ", url="https://t.me/D_racon"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" ุงูุฏููู ุงูุฃุณุงุณู ูุงุณุชุฎุฏุงู ูุฐุง ุงูุจูุช:

 1 โค ุฃููุงู ุ ุฃุถููู ุฅูู ูุฌููุนุชู
 2 โค ุจุนุฏ ุฐูู ุ ูู ุจุชุฑููุชู ููุดุฑู ูููุญ ุฌููุน ุงูุตูุงุญูุงุช ุจุงุณุชุซูุงุก ุงููุถุน ุงูุฎูู
 3 โค ุจุนุฏ ุชุฑููุชู ุ ุงูุชุจ /reload ูุฌููุนุฉ ูุชุญุฏูุซ ุจูุงูุงุช ุงููุดุฑููู
 3 โค ุฃุถู @{ASSISTANT_NAME} ุฅูู ูุฌููุนุชู ุฃู ุงูุชุจ /userbotjoin ูุฏุนูุฉ ุญุณุงุจ ุงููุณุงุนุฏ
 4 โค ูู ุจุชุดุบูู ุงูููุงููุฉ  ุฃููุงู ูุจู ุงูุจุฏุก ูู ุชุดุบูู ุงูููุฏูู / ุงูููุณููู
 5 โค ูู ุจุนุถ ุงูุฃุญูุงู ุ ูููู ุฃู ุชุณุงุนุฏู ุฅุนุงุฏุฉ ุชุญููู ุงูุจูุช ุจุงุณุชุฎุฏุงู ุงูุฃูุฑ /reload ูู ุฅุตูุงุญ ุจุนุถ ุงููุดููุงุช
 ๐ ุฅุฐุง ูู ููุถู ุงูุจูุช ุฅูู ุงูููุงููุฉ ุ ูุชุฃูุฏ ูู ุชุดุบูู ุงูููุงููุฉ  ุจุงููุนู ุ ุฃู ุงูุชุจ /userbotleave ุซู ุงูุชุจ /userbotjoin ูุฑุฉ ุฃุฎุฑู
โ โ โ โ โ โ โ โ โโ โ โ โ โ โ โ
 ๐ก ุฅุฐุง ูุงูุช ูุฏูู ุฃุณุฆูุฉ  ุญูู ูุฐุง ุงูุจูุช ุ ูููููู ุฅุฎุจุงุฑูุง ููู ุฎูุงู ูุฑูุจ ุงูุฏุนู ุงูุฎุงุตุฉ ุจู ููุง โค @{GROUP_SUPPORT}

-ยป [ุฃูุงููุฑ ุงูุจูุช](https://t.me/M_TYU_62/6)
-ยป [ุชุญุฏูุซุงุช ุงูุจูุช](https://t.me/M_TYU_62)
-ยป [ูุจุฑูุฌ ุงูุณูุฑุณ](https://t.me/a_bd80)
__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ ุฑุฌูุน", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โจ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

ยป **press the button below to read the explanation and see the list of available commands !**

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("๐ท๐ป Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("๐ง๐ป Sudo Cmd", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("๐ Basic Cmd", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("๐ Go Back", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ ูุง ูู ุงูุฃูุงูุฑ ุงูุฃุณุงุณูุฉ:
-ยป /mplay ใุงุณู ุงูุฃุบููุฉ / ุฑุงุจุทใุชุดุบูู ุงูุตูุช mp3
-ยป /vplay ใุงุณู / ุฑุงุจุท ุงูููุฏููใ ุชุดุบูู ุงูููุฏูู ุฏุงุฎู ุงูููุงููุฉ 
-ยป /stream ใุฑุงุจุท ใุชุดุบูู ุตูุช
-ยป /vstream ใุฑุงุจุทใ ุชุดุบูู ููุฏูู ูุจุงุดุฑ ูู ุงูููุชููุจ
-ยป /stop ูุงููุงู ุงูุชุดุบูู
-ยป /resume ุงุณุชุฆูุงู ุงูุชุดุบูู
-ยป /skip ุชุฎุทู ุงูุฆ ุงูุชุงูู
-ยป /pause ุงููุงู ุงูุชุดุบูู ูููุชุข
-ยป /vmute ููุชู ุงูุจูุช
-ยป /vunmute ูุฑูุน ุงููุชู ุนู ุงูุจูุช
โ โ โ โ โ โ โ โ โโ โ โ โ โ โ โ
-ยป [ุฃูุงููุฑ ุงูุจูุช](https://t.me/M_TYU_62/6)
-ยป [ุชุญุฏูุซุงุช ุงูุจูุช](https://t.me/M_TYU_62)
-ยป [ูุจุฑูุฌ ุงูุณูุฑุณ](https://t.me/a_bd80)
__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ ุงููุชูุงููู", callback_data="cbadmin")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""  -ยป /playlist โค ุชุธูุฑ ูู ูุงุฆูุฉ ุงูุชุดุบูู
-ยป /video + ุงูุงุณู  ุชูุฒูู ููุฏูู ูู youtube
-ยป /song + ุงูุงุณู ุชูุฒูู ุตูุช ูู youtube
-ยป /volume + ุงูุฑูู ูุถุจุท ูุณุชูุฆ ุงูุตูุช
-ยป /reload ูุชุญุฏูุซ ุงูุจูุช ู ูุงุฆูุฉ ุงููุดุฑููู
-ยป /userbotjoin ูุงุณุชุฏุนุงุก ุญุณุงุจ ุงููุณุงุนุฏ
-ยป /userbotleave ูุทุฑุฏ ุญุณุงุจ ุงููุณุงุนุฏ 
-ยป /ping - ุฅุธูุงุฑ ุญุงูุฉ ุงูุจูุช ุจููุบ
-ยป /alive  ุฅุธูุงุฑ ูุนูููุงุช ุงูุจูุช  (ูู ุงููุฌููุนุฉ)
โ โ โ โ โ โ โ โ โโ โ โ โ โ โ โ
-ยป [ุฃูุงููุฑ ุงูุจูุช](https://t.me/M_TYU_62/6)
-ยป [ุชุญุฏูุซุงุช ุงูุจูุช](https://t.me/M_TYU_62)
-ยป [ูุจุฑูุฌ ุงูุณูุฑุณ](https://t.me/a_bd80)
__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ ุฑุฌูุน", callback_data="cbstart")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ here is the sudo commands:

ยป /rmw - clean all raw files
ยป /rmd - clean all downloaded files
ยป /sysinfo - show the system information
ยป /update - update your bot to latest version
ยป /restart - restart your bot
ยป /leaveall - order userbot to leave from all group

โก __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\nยป revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐ก ุงููุณุคูู ุงููุญูุฏ ุงูุฐู ูุฏูู ุฅุฐู ุฅุฏุงุฑุฉ ุงูุฏุฑุฏุดุงุช ุงูุตูุชูุฉ ููููู ุงูููุฑ ุนูู ูุฐุง ุงูุฒุฑ !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"โ๏ธ **ุงูุฅุนุฏุงุฏุงุช** {query.message.chat.title}\n\nโธ : ุงููุงู ุงูุชุดุบูู ูููุชุข\nโถ๏ธ : ุงุณุชุฆูุงู ุงูุชุดุบูู\n๐ : ูุชู ุงูุตูุช\n๐ : ุงูุบุงุก ูุชู ุงูุตูุช\nโน : ุงููุงู ุงูุชุดุบูู",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("โน", callback_data="cbstop"),
                      InlineKeyboardButton("โธ", callback_data="cbpause"),
                      InlineKeyboardButton("โถ๏ธ", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("๐", callback_data="cbmute"),
                      InlineKeyboardButton("๐", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("๐ ุงุบูุงู", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("โ ูุงุฆูุฉ ุงูุชุดุบูู ูุงุฑุบู", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐ก ุงููุณุคูู ุงููุญูุฏ ุงูุฐู ูุฏูู ุฅุฐู ุฅุฏุงุฑุฉ ุงูุฏุฑุฏุดุงุช ุงูุตูุชูุฉ ููููู ุงูููุฑ ุนูู ูุฐุง ุงูุฒุฑ !", show_alert=True)
    await query.message.delete()
