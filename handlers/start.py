from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hello🤠 {message.from_user.first_name}!
I am TN57 Music Player Bot, created by @TN57_BotZ

For Help, Support or Error Report contact my Master @BluVDs!

List of Supported Streaming Platforms Given Below:
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🤓Contact My Dev🤓", url="t.me/Bluvds",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "YouTube", url="Youtube.com"
                    ),
                    InlineKeyboardButton(
                        "Jio Saavn", url="https://www.jiosaavn.com/"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Deezer", url="https://www.deezer.com"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "🤡 Do you want to search for a YouTube video?😺",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
