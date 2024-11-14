from openai import OpenAI
import openai
import os

def api_key_request():

    while True:
        try:
            client = OpenAI()
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": "Hello world"}
                ]
            )
            print("Klucz działa!")
            break
        except openai.OpenAIError:
            OPENAI_API_KEY = input(str("Twój klucz API nie działa bądź nie istnieje, podaj swój klucz API OpenAI: "))
            os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

        except openai.AuthenticationError:
            OPENAI_API_KEY = input(str("Twój klucz API nie działa bądź nie istnieje, podaj swój klucz API OpenAI: "))
            os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


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


api_key_request()
ask_openai("", "Przywitaj się.")
