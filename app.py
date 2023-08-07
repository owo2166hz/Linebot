'''
Author: owo2166hz owo2166hz@gmail.com
Date: 2023-08-07 09:38:44
LastEditors: owo2166hz owo2166hz@gmail.com
LastEditTime: 2023-08-07 16:30:21
FilePath: \OWO\LINEBOT\app.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from line_bot_api import *
from events.basic import *
from events.oil import *

app = Flask (__name__)

#監聽所有來自/callback的Post Request
@app.route("/callback", methods=["POST"])
def callback():
    #get X-Line-Signature header value
    signature = request.headers["X-Line_Signature"]

    #get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    #header webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"



#處理訊息(這邊是歡迎訊息)
@handler.add(FollowEvent)
def handle_follow(event):
    welcome_msg = """ Hello 您好 歡迎你成為OWO的好友 我是OWO 財經小幫手 這裡有股票 匯率資訊喔 期待您的光臨"""

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message_text = str(event.message.text).lower()
    if message_text == '使用說明':
        about_us_event(event)
        Usage(event)
    
        
    if event.message.text == '小幫手':
        line_bot_api.reply_message(event.reply_token , buttons_template)

    ############################

    if event.message.text == '想知道油價':
        content = oil_price()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
    
@handler.add(UnfollowEvent)
def handle_follow(event):
    print(event)


if __name__=="__main__":
    app.run() 