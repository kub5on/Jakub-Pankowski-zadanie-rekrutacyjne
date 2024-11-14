from openai import OpenAI


def ask_openai(system_content, prompt):
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": prompt}
        ]
    )
    print(completion.choices[0].message)


ask_openai("", "Przywitaj się.")
