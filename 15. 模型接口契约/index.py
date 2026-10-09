from utils import config
from openai import OpenAI, AsyncOpenAI
import sys

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
# 获取模型列表
# list = client.models.list()
# print(list.to_json())
response = client.chat.completions.create(
    model=config.OPENAI_MODEL,
    messages=[{"role": "user", "content": "你是谁"}],
    extra_body={"thinking": {"type": "disabled"}},  # qwen3-vl无法直接关闭思考模式
    stream=True,
)
for chunk in response:
    print(chunk)
    sys.stdout.flush()
