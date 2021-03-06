from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["/start", f"/start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
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
                [InlineKeyboardButton("๐๏ธุดุฑูุญูุงุช ุงูุจููุช", callback_data="cbhowtouse")],
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


@Client.on_message(
    command(["/alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("๐ง๏ธุขููุณูููุฑุณ", url=f"https://t.me/SULHB"),
                InlineKeyboardButton(
                    "๐๏ธุงููุฏุนูู", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**ูุฑุญุจุข  {message.from_user.mention()}, ุงูุง {BOT_NAME}**\n\nโจ ุงูุจูุช ูุนูู ุจุดูู ุทุจูุนู\n๐ ุงูุง : [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\nโจ ุงุตุฏุงุฑ Bot : `v{__version__}`\n๐ ุงุตุฏุงุฑ Pyrogram : `{pyrover}`\nโจ ุงุตุฏุงุฑ Python: `{__python_version__}`\n๐ ุงุตุฏุงุฑ PyTgCalls : `{pytover.__version__}`\nโจ ููุช ุงูุชุดุบูู: `{uptime}`\n\n**ุดูุฑูุง ูุฅุถุงูุชู ููุง ุ ูุชุดุบูู ุงูููุฏูู ูุงูููุณููู ุนูู ุฏุฑุฏุดุฉ ุงูููุฏูู ุงูุฎุงุตุฉ ุจูุฌููุนุชู ** โค"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("๐ `PONG!!`\n" f"โก๏ธ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "๐ค bot status:\n"
        f"โข **uptime:** `{uptime}`\n"
        f"โข **start time:** `{START_TIME_ISO}`"
    )
