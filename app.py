'''
Author: owo2166hz owo2166hz@gmail.com
Date: 2023-08-07 09:38:44
LastEditors: owo2166hz owo2166hz@gmail.com
LastEditTime: 2023-08-07 15:14:13
FilePath: \OWO\LINEBOT\app.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from line_bot_api import *
from events.basic import *

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
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message_text = str(event.message.text).lower()
    if message_text == '@使用說明':
        about_us_event(event)
    if message_text == '@查詢方法':
        Usage(event)
    if event.message.text == '@小幫手':
        buttons_template = TemplateSendMessage(
            alt_text='小幫手 template',
            template=ButtonsTemplate(
                title = '選擇服務',
                text='請選擇',
                thumbnail_image_url = 'https://i.imgur.com/zGN9PFZ.png',
                actions=[
                    MessageTemplateAction(
                        label='油價查詢',
                        text='油價查詢'
                    ),
                    MessageTemplateAction(
                        label='匯率查詢',
                        text='匯率查詢'
                    ),
                    MessageTemplateAction(
                        label='股價查詢',
                        text='股價查詢'
                    )
                ]
            )

        )
        line_bot_api.reply_message(event.reply_token , buttons_template)
    

if __name__=="__main__":
    app.run() 