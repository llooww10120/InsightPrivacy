from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, messages
import configparser
from cra import cra as ca
app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')
# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))
def getedata(url):
    ca.cra(url)

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 
@handler.add(MessageEvent, message=TextMessage)
def echo(event):
    # message=ImageSendMessage(original_content_url="https://i.imgur.com/ae1ImwP.jpg",preview_image_url="https://i.imgur.com/ae1ImwP.jpg")
    message=TextMessage(text=getedata(event.message.text))
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        line_bot_api.reply_message(event.reply_token,message)

if __name__ == "__main__":
    app.run()