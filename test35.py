import openai

client = openai.OpenAI(api_key="Write your Api Key ")
response = client.chat.completions.create(
    model = "gpt-3.5-turbo", 
    messages=[{"role": "user", "content": "Hello, how are you? I'm your AI assistant."}]
)
print(response.choices[0].message.content)
