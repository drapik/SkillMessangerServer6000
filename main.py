# Flask  - библиотека веб-сервера
# ctrl + alt + L - форматировать текст под PEP8 формат

from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)
all_messages = []


@app.route("/")
def hello_world():
    return "<p>Hello, <b>Oleg!</b> Welcome to the Chat</p>"


# API для получения списка сообщений
@app.route("/get_messages")
def get_messages():
    return {"messages": all_messages}


def add_message(sender, text):
    # time: подставить автоматически
    new_message = {
        "sender": sender,
        "text": text,
        "time": datetime.now().strftime("%H:%M")
    }
    # append - добавить элемент в список
    all_messages.append(new_message)


# API для отправки сообщений
@app.route("/send_message")
def send_message():
    sender = request.args['sender']
    text = request.args['text']
    if 3 > len(sender) <= 100:
        print('123')
        return '{"result": False, error: "Invalid Name"}'
    if 1 > len(text) <= 3000:
        print('321')
        return '{"result": False, error: "Text should be >1 and <3000 char"}'
    else:
        add_message(sender, text)
        print('message done')
    return {"result": True}


@app.route("/chat")
def chat_page():
    return render_template("form.html")


@app.route("/info")
def chat_info_page():
    body_info = "<p style=\"font-size: 40px;\">в чате <b style='color: green;'>{0}</b> сообщения</p>".format(len(all_messages))
    return body_info


add_message("Oleg", "hello")
add_message("User2", "Yes,hello")

app.run()
#тестирую гит