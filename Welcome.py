from nonebot import on_notice
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Message, GroupDecreaseNoticeEvent,GroupIncreaseNoticeEvent

welcom = on_notice()

#进群欢迎
@welcom.handle()
async def _(bot: Bot,event:GroupDecreaseNoticeEvent , state: T_State):
    user = event.get_user_id()
    at_ = "[CQ:at,qq={}]".format(user)
    msg = at_ + '欢迎新进群的小伙伴：\n来了就别想走了哦'
    msg = Message(msg)
    await welcom.finish(message=msg)

#退群提醒
@welcom.handle()
async def _(bot: Bot, event:GroupIncreaseNoticeEvent, state: T_State):
    user = event.get_user_id()
    at_ = "[CQ:at,qq={}]".format(user)
    msg = at_ + '\n' +'/(ㄒoㄒ)/~~又一位群友离我们而去'
    msg = Message(msg)
    await welcom.finish(message=msg)