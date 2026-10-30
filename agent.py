tools = [
    {"type": "function", "function" :{
        "name": "query_mysql",
         "description": "执行只读SQL查询。表students字段：id(学号), name(姓名), chinese(语文), math(数学), english(英语)",
         "parameters": {
             "type": "object",
             "properties": {"sql": {"type": "string"}},
             "required": ["sql"]}}},
    {"type": "function", "function": {
        "name": "calculator",
        "description": "计算数字表达式",
        "parameters": {
            "type": "object",
            "properties": {"expression": {"type": "string"}},
            "required": ["expression"]}}},
]

available = {"query_mysql": query_mysql, "calculator": calculator}

def ask_agent(question):
    messages = [
        {"role": "system", "content": "你是数据助手。遇到数据问题先查数据库，需要算数用计算器，最后用中文总结回答。"},
        {"role": "user", "content": question}]
    for _ in range(8):
        resp = client.chat.completions.create(
            model="mimo-v2.6-pro", messages=messages, tools=tools,extra_body={"thinking": {"type": "disabled"}})
        msg = resp.choices[0].message
        if msg.tool_calls:
            messages.append(msg)
            for tc in msg.tool_calls:
                args = json.loads(tc.function.arguments)
                print(f">>> 调用 {tc.function.name}({args})")
                result = available[tc.function.name](**args)
                messages.append({"role": "tool",
                                 "tool_call_id": tc.id, "content": result})
        else:
            return msg.content
    return "步数超限"

print(ask_agent("英语及格分数为80分，谁英语不及格?他三科平均分是多少?"))
