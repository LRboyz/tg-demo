import telebot
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def hello_world():
    return {
        "message": "Hello World"
    }


@app.get("/test")
def hello_world():
    return {
        "message": "这是测试用的接口"
    }


# 在 BotFather 那里获得你自己的 Telegram Bot API Token，并将其粘贴在此处
TOKEN = '6102219812:AAFQGk0KiEIObTjmAjTISGqODsGBEy5qs9g'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True)
def calculate(message):
    # 获取用户发送的消息文本
    query = message.text
    print("用户说的消息", query)
    try:
        # 使用 eval() 函数来执行字符串形式的数学运算表达式
        result = eval(query)

        response = "结果为：" + str(result)

    except (SyntaxError, NameError):
        response = "无法识别您输入的问题，请重新输入"

    bot.reply_to(message, response)


if __name__ == '__main__':
    bot.polling()