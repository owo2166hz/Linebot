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
                        quickReplyButton(
                                action=MessageAction(
                                    label="K線圖",
                                    text="@K"+stockNumber
                                )
                            ),
                            ]
                        ))
    return text_massage