<img width="647" height="293" alt="image" src="https://github.com/user-attachments/assets/79ca9c09-3558-450b-9e17-7e90b86e6c2a" /># Function Calling + RAG 智能数据助手
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
<img width="648" height="290" alt="image" src="https://github.com/user-attachments/assets/51e3e39c-84c8-4e9b-a19c-888deee24572" />

## 📦 依赖安装
pip install openai pymysql chromadb

## 📊 Agent 基准评测

使用独立脚本'eval_agent.py'自动化批量评测，覆盖纯SQL查询、SQL+计算器串联、RAG检索、多工具链式调用、域外幻觉抑制、危险SQL拦截6类典型场景，自动采集响应延迟、Token 消耗，人工校验工具调用链路与回答正确性。

- 评测用例总数：8
- 任务完成率：100.0%（8/8）
- 平均响应延迟：8.89 s
- 平均 Token 消耗：881.1

<img width="709" height="403" alt="image" src="https://github.com/user-attachments/assets/1fee3b4f-fa18-4c6e-b922-38301485d3eb" />
<img width="419" height="275" alt="image" src="https://github.com/user-attachments/assets/e1dbfe93-36e2-4648-aeae-d557e2b9b130" />
<img width="568" height="275" alt="image" src="https://github.com/user-attachments/assets/f26d75c9-5ce6-4961-ac3e-2625b2e98fe2" />
<img width="863" height="533" alt="image" src="https://github.com/user-attachments/assets/c1a74711-fa25-4dd6-acc8-12d9a5889df7" />
<img width="791" height="371" alt="image" src="https://github.com/user-attachments/assets/419a3db6-0d79-429c-bf17-3ba7875c9d9c" />
<img width="966" height="191" alt="image" src="https://github.com/user-attachments/assets/7b2a795c-0c07-4cef-804c-5f85053a1a2a" />
<img width="971" height="448" alt="image" src="https://github.com/user-attachments/assets/ede0d9ad-e592-4a74-ae78-2c7e99b903c3" />
