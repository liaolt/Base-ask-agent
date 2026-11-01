# Function Calling + RAG 智能数据助手
## ✨ 项目能干什么
本项目是一个基于 Python 搭建的 AI Agent 智能助手，融合 **Function Calling 工具调用 + RAG检索增强** 能力：
1. 🧮 计算器工具：接收数学表达式，自动完成数值计算
2. 🗄️ MySQL 查询工具：安全地只读查询本地学生成绩数据库（仅支持SELECT语句，防止删改）
3. 📚 RAG知识库检索：使用 BAAI/bge-m3 向量模型，结合 ChromaDB 向量库，对简历文档做切片向量化检索；仅基于给定文档内容回答，文档不存在信息则回复不知道
4. 🤖 智能路由：大模型自动判断问题类型，选择合适工具：数据库问题走MySQL查询、计算问题走计算器、简历/文档类问题走向量检索RAG

> 底层模型使用小米MIMO大模型，向量嵌入调用硅基流动SiliconFlow的BAAI/bge-m3。

## 🛠️ 技术栈
- Python
- Function Calling（工具调用）
- MySQL（pymysql）
- ChromaDB（向量数据库）
- RAG（检索增强生成）
- OpenAI兼容SDK（硅基流动、MIMO模型接口）
- BAAI/bge-m3 向量Embedding模型

## 📷 运行截图
<img width="647" height="313" alt="image" src="https://github.com/user-attachments/assets/84e86b00-2748-43c6-8822-b2e0a9196b23" />

## 📦 依赖安装
pip install openai pymysql chromadb
