from openai import OpenAI

client = OpenAI()
prompt = "Przywitaj się"
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": ""},
        {"role": "user", "content": prompt}
    ]
)

print(completion.choices[0].message)
