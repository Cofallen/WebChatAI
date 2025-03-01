from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import openai
import requests
import key
import os


app = Flask(__name__)

if key.api_key == "sk-xxx":
    key.api_key = os.getenv("API_KEY")

client = OpenAI(
    api_key=key.api_key,
    base_url='https://api.deepseek.com',
    default_headers={"Content-Type": "application/json"}  # 添加默认请求头
)

def getmessage(msg, user_id):
    print("调用API, 用户id:{user_id}，消息：{msg}".format(user_id=user_id, msg=msg))
    
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是一个可爱猫娘\n" + msg},
            ],
            max_tokens= 512,
            temperature= 0.7,
            stream= False
            
        )
    except Exception as api_error:
        print(api_error)
        return jsonify({"error": "API调用失败"})
    
    reply = response.choices[0].message.content
    # print("API返回：", reply)
    return reply

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get("message")
    # 此处可以从 session 中获取 user_id，示例中直接使用 "123456"
    reply = getmessage(message, "123456")
    return jsonify({"reply": reply})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    # with app.app_context():
    #     getmessage("中国大模型行业2025年将会迎来哪些机遇和挑战？", "123456")