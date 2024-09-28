from flask import Flask, request, jsonify, render_template, Response, stream_with_context
from flask_cors import CORS
from openai import AzureOpenAI
import os
import json
import markdown

# 初始化 Flask 应用
app = Flask(__name__)
# 启用跨域资源共享
CORS(app)

# 初始化 Azure OpenAI 客户端
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),  
    api_version=os.getenv("AZURE_OPENAI_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

print(f"AZURE_OPENAI_ENDPOINT: {os.getenv('AZURE_OPENAI_ENDPOINT')}")
print(f"AZURE_OPENAI_VERSION: {os.getenv('AZURE_OPENAI_VERSION')}")
print(f"AZURE_OPENAI_KEY: {'Set' if os.getenv('AZURE_OPENAI_KEY') else 'Not Set'}")

# 定义主页路由
@app.route('/')
def home():
    return render_template('index.html')

# 定义聊天接口
@app.route('/chat', methods=['POST'])
def chat():
    # 获取用户发送的消息
    user_message = request.json['message']
    
    # 定义生成器函数，用于流式传输响应
    def generate():
        try:
            full_response = ""
            # 调用 Azure OpenAI API
            response = client.chat.completions.create(
                model="your-deployment-name",  # 替换为您的部署名称
                messages=[
                    {"role": "system", "content": "你是一个有帮助的助手。请使用Markdown格式输出。"},
                    {"role": "user", "content": user_message}
                ],
                stream=True
            )
            
            # 逐块处理 API 响应
            for chunk in response:
                if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    full_response += content
                    # 发送每个内容块
                    yield f"data: {json.dumps({'content': content})}\n\n"
            
            # 发送完整的响应
            yield f"data: {json.dumps({'full_response': full_response})}\n\n"
            # 发送结束信号
            yield f"data: {json.dumps({'end': True})}\n\n"
            
        except Exception as e:
            print(f"Error in /chat route: {str(e)}")
            # 发送错误信息
            yield f"data: {json.dumps({'error': str(e)})}\n\n"

    # 返回流式响应
    return Response(stream_with_context(generate()), content_type='text/event-stream')

# 运行 Flask 应用
if __name__ == '__main__':
    app.run(debug=True)