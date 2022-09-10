from JE313P import JE313P, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
•═════•| [𝙀ٍ𝙇ٓ𝙍َٰ𝘼َٰ𝙎َٰ𝘼ِّّ𝙈](https://t.me/EL_RASA) |•═════•

↯ مِـرحًبّـآفــي سًــــــــوُرسُ ★𝙀ٍ𝙇ٓ𝙍َٰ𝘼َٰ𝙎َٰ𝘼ِّّ𝙈 ★.

↯ اختصاصي تشغيل الاغاني والفديوهات في المكالمات  .

↯ البوت يعمل بسرعه عاليه ولا يوجد تقطيع .

↯ ضيف البوت الي مجموعتك واستمتع .

⌁ [𝐸𝐿𝑅𝐴𝑆𝐴𝑀 ’⚡](t.me/Mahmod777777)

•═════•| [𝙀ٍ𝙇ٓ𝙍َٰ𝘼َٰ𝙎َٰ𝘼ِّّ𝙈](https://t.me/ELRSAM11) |•═════•
"""

@JE313P.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("➕ اضغط هنا لأضافتي", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("السورس", "https://t.me/EL_RASA")],
        [Button.url("الدعم", f"https://t.me/{Config.SUPPORT}"), Button.url("القناة", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("الاوامر", data="help")]])
       return

    if event.is_group:
       await event.reply("**- اهلا بك انا اعمل بنجاح**")
       return



@JE313P.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ اضغط هنا لاضافتي", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("السورس", "https://t.me/EL_RASA")],
        [Button.url("الدعم", f"https://t.me/{Config.SUPPORT}"), Button.url("القناة", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("الاوامر", data="help")]])
       return
