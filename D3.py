# score = 85

# if score >= 90:
#     grade = 'A'
# elif score >=80:
#     grade = 'B'
# elif score >=70:
#     grade = 'C'
# elif score >=60:
#     grade = 'D'
# else:
#     grade = 'F'

# print(f'成绩{score}分-->等级为{grade}')
# 

# students = {
#     '小明':88,
#     '小红':76,
#     '小王':98
# }
# for name,value in students.items():
#     print(f"{name}:{value}")

# 这是 DeepSeek 接口真实返回的样子（简化版）
response = {
    "id": "chatcmpl-123",
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "你好！"
            }
        }
    ],
    "usage": {"total_tokens": 42}
}

# 要拿到 AI 的回复，你就得一层层取：
tokens = response["usage"]['total_tokens']

if tokens > 100:
    print('这次回复比较长')
else:
    print('这次回复很短')

print(f"本次使用tokens={tokens}")  # → 你好