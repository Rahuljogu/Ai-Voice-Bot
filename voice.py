from Openai import OpenAI
from apikey import api_data

model='gpt-4o'
client=OpenAI(api_key=api_data)

def Reply(question):
    completion=client.chat.completions.create(
    model=model,
    messages=[
        {'role':"system",'content':"you are a helpful assist"},
        {'role':"user",'content':question}
    ],
    max_tokens=200
    )
    answer=completion.choice[0].messages.content
    return answer
question='explain me about ai in 50 words'
ans=Reply(question)
print(ans)
#text to speech

