from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Message
import aiohttp




qinghua = on_command('说句话',rule=to_me(),priority=5)

@qinghua.handle()
async def _(bot: Bot,event:Event,state: T_State):
    reply = await get_reply()
    msg_send = Message(reply)
    await qinghua.finish(message=msg_send)



async def get_reply():
    reply_list = await fetch()
    return reply_list



async def fetch():
    async with aiohttp.ClientSession() as session:
        url = 'https://qinghua.haom.ren/api.php'
        response = await session.get(url,verify_ssl = False)
        txt = await response.text()
        return txt