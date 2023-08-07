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
def push_msg(event,msg):
    try:
        user_id = event.source.user_id
        line_bot_api.push_message(user_id,TextSendMessage(text=msg))
    except:
        room_id = event.source.room_id
        line_bot_api.push_message(room_id,TextSendMessage(text=msg))

def Usage(event):
    push_msg(event," 🥹查詢方法🥹  \
             \n\
             \n 🌎小幫手可以查詢油價 匯率🥹 \
             \n\
             \n 🌎匯率通知 輸入查詢由下\
             \n 🌎匯率兌換 換匯USD/TWD\
             \n 🌎股價查詢 輸入#股票代碼")

