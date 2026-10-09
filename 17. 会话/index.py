from agent.model import Model
from agent.printer import print_response, print_stream, PrinterConfig
from agent.prompt import render_prompt

model = Model()
# # 第1次调用
# resp = model.invoke_stream(
#     [
#         {"role": "system", "content": render_prompt("system")},
#         {"role": "user", "content": "uv是什么？"},
#     ]
# )

# print_stream(resp)
# # 第2次调用
# resp = model.invoke_stream(
#     [
#         {"role": "system", "content": render_prompt("system")},
#         {"role": "user", "content": "如何安装？"},
#     ]
# )

# print_stream(resp)
from agent.session import Session

session = Session()
session.add_message({"role": "system", "content": render_prompt("system")})
session.add_message({"role": "user", "content": "uv是什么？"})
# # 第一次调用
# resp = model.invoke_stream(session)

# print_stream(resp)
# 查看会话内容
import json

print(session.id)
print(json.dumps(session.messages, ensure_ascii=False, indent=2))
session.save()
