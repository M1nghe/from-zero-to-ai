from config import DEEPSEEK_API_KEY
from openai import OpenAI

client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com"
)

# response = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {'role':'system','content':'You are a helpful assistant'},
#         {'role':'user','content':'Introduce yourself in one sentence'}
#     ]
# )

# print(response.choices[0].message.content)


while True:
    user_input = input("User: ")
    if user_input.lower() in ("quit",'exit','q','退出'):
        break
    response = client.chat.completions.create(
        model = 'deepseek-chat',
        messages=[
            {'role':'system','content':'你是一个有帮助的助手'},
            {'role':'user','content':user_input}
        ]
    )
    print("AI: ",response.choices[0].message.content)