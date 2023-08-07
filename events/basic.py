from line_bot_api import *


def about_us_event(event):
    emoji = [
            {"index":0,
             "productId":"5ac21b4f031a6752fb806d59",
             "emojiId":"041"
                },

            {"index":1,
             "productId":"5ac21b4f031a6752fb806d59",
             "emojiId":"049"
                },
            {"index":2,
             "productId":"5ac21b4f031a6752fb806d59",
             "emojiId":"041"
                },
            ]
    #歡迎訊息
    text_message = TextSendMessage(text="""$$$
告知 歡迎成為OWO好友
此處提供一些功能以及歡迎訊息
""",emojis=emoji)
    
    #貼圖訊息
    sticker_message = StickerMessage(
        package_id = "11537",
        sticker_id = "52002769")
    
    #將歡迎訊息、貼圖訊息放到機器人裡面回復
    line_bot_api.reply_message(
        event.reply_token,
        [text_message, sticker_message])