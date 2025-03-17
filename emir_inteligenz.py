import emir_inteligenz

emir_inteligenz.api_key = "API_KEY"

response = emir_inteligenz.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Sen bir yardımcı AI asistansın."},
        {"role": "user", "content": "Bana en iyi yapay zeka modellerini söyle!"}
    ],
    temperature=0.7
)

print(response["choices"][0]["message"]["content"])
