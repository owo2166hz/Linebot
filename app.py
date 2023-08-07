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
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    app.run()

