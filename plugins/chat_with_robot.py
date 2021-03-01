from nonebot import on_message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Message,MessageEvent
import aiohttp
import urllib.parse
import json
import re



chat_me = on_message(rule=to_me(),priority=8)

@chat_me.handle()
async def _(bot: Bot,event:MessageEvent,state: T_State):
    to_robot = str(event.get_message())
    face_code ,reply = await get_reply(to_robot)
    if len(face_code)==0:
        msg_send = Message(reply)
    else:
        code_list = []
        face_list = []
        for code in face_code:
            code_list.append(code)
            code = re.findall("\d+", code)
            face_list.append("[CQ:face,id={}]".format(code[0]))
        for i in range(len(face_list)):
            reply = reply.replace("{}".format(face_code[i]),"{}".format(face_list[i]))
        msg_send = Message(reply)
    await chat_me.finish(message=msg_send)



async def get_reply(to_robot):
    face_code ,txt = await fetch(to_robot)
    return face_code ,txt



async def fetch(to_robot):
    async with aiohttp.ClientSession() as session:
        url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(urllib.parse.quote(to_robot))
        response = await session.get(url,verify_ssl = False)
        txt = await response.text()
        txt = json.loads(txt)['content']
        txt = txt.replace('菲菲', 'Cina')
        txt = txt.replace('{br}','\n')
        if '{face:'in txt:
            face_code = re.findall(r'{face:.*?}',txt)
            return face_code , txt
        else:
            face_code = []
            return face_code,txt




