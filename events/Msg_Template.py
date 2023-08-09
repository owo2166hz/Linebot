'''
Author: owo2166hz owo2166hz@gmail.com
Date: 2023-08-09 09:28:38
LastEditors: owo2166hz owo2166hz@gmail.com
LastEditTime: 2023-08-09 10:19:27
FilePath: \Linebot-1\events\Msg_Template.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from line_bot_api import *


def stock_reply_other(stockNumber):
    contest_text = "即時股價和K線圖"
    text_massage = TextSendMessage(
                                text = contest_text,
                                quick_reply=QuickReply(
                                items=[
                                QuickReplyButton(
                                        action=MessageAction(
                                            label="及時股價",
                                            text="#"+stockNumber,
                                )
                        ),
                        QuickReplyButton(
                                action=MessageAction(
                                    label="K線圖",
                                    text="@K"+stockNumber
                                )
                            ),
                            ]
                        ))
    return text_massage