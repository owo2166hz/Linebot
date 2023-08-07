from flask import Flask, request, abort
from linebot.exceptions import (InvalidSignatureError)
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.models import *

app = Flask (__name__)

line_bot_api = LineBotApi('/5O5W/lf2xUg2O4/x/whu8JrKyoN4LzoExue5u+JTJmrOOZlkYq+KDSiW/lDhAInEIAr1tiNT8r4IC71DYNf7cEB95E7kB63JAh/Q+jyMFE3IaMy4hc9FgKjPUx6GrWrbSmgPbXHYbO2VLkt3vJQ5wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9110abd2b90e95aa80c4cb30023507d7')




# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    emoji = [
            {
                "imdex":0,
                "productId":"5ac21184040ab15980c9b43a",
                "emojiId":"001"
            },
            {
                "imdex":18,
                "productId":"5ac21184040ab15980c9b43a",
                "emojiId":"001"
            }
    ]


    text_message = TextSendMessage(text='''$ Master Finance $
Hello! 您好 歡迎您成為OWO的好友
                                   
我是OWO財經小幫手
                                   
-這裡有股票 匯率資訊
-直接點選下方的選單功能
-期待您的光臨''',emojis=emoji)
    
    sticker_message = StickerMessage(
        package_id = "11537",
        sticker_id = "52002769")
    line_bot_api.reply_message(
        event.reply_token,
        [text_message, sticker_message])
    


if __name__ == "__main__":
    app.run()