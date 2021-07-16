from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('6Eq5q/wPR7FtllZgmo8LXleo8XsZixdm+gQXaqnggAdT0C7M2yopVRHoc3WgcwUOeHgQrNjHuGtGczyIh6rB0n27zGL2XYx8HNHeMIJVDjOXyPYq5cLxO8957uCyOcRztJ5GvludNXgz2MdDq9edGQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('cdb51a1a3e5e5e31fb864f7652e45099')

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

# 學你說話
@handler.add(MessageEvent, message=TextMessage)
def echo(event):
    
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="哈哈翔宇很幽默欸")
        )

if __name__ == "__main__":
    app.run()