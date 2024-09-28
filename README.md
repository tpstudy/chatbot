# AI 聊天助手

## 项目简介

AI 聊天助手是一个基于 Flask 和 Azure OpenAI 服务的网页应用程序。它提供了一个简单而直观的界面，允许用户与 AI 进行对话。该应用程序支持实时流式输出，markdown 格式化，以及复制 AI 回复到剪贴板的功能。

## 功能特点

- 实时流式 AI 响应
- Markdown 格式支持
- 复制 AI 回复到剪贴板
- 响应式设计，适配各种设备
- 简洁美观的 Material Design 风格界面

## 技术栈

- 后端：Python, Flask
- 前端：HTML, CSS, JavaScript, jQuery
- AI 服务：Azure OpenAI
- 其他库：marked.js (用于 Markdown 渲染)

## 安装指南

1. 克隆仓库：
   ```
   git clone https://github.com/your-username/ai-chat-assistant.git
   cd ai-chat-assistant
   ```

2. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

3. 设置环境变量：
   ```
   export AZURE_OPENAI_KEY=your_azure_openai_key
   export AZURE_OPENAI_VERSION=your_azure_openai_version
   export AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
   ```

4. 运行应用：
   ```
   python app.py
   ```

5. 在浏览器中访问 `http://localhost:5000`

## 使用说明

1. 在输入框中输入您的问题或消息
2. 点击发送按钮或按回车键发送消息
3. 等待 AI 助手的回复
4. 如需复制 AI 的回复，点击回复旁边的"复制"按钮

## 配置

在 `app.py` 文件中，确保将 `model` 参数设置为您的 Azure OpenAI 部署名称：
