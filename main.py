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
            print("Klucz działa! Połączono się z API OpenAI.")
            break
        except openai.OpenAIError:
            OPENAI_API_KEY = input(str("Twój klucz API nie działa bądź nie istnieje, podaj swój klucz API OpenAI: "))
            os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

        except openai.AuthenticationError:
            OPENAI_API_KEY = input(str("Twój klucz API nie działa bądź nie istnieje, podaj swój klucz API OpenAI: "))
            os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

def ask_openai(system_content, user_prompt, article):

    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_prompt + article}
        ]
    )
    answer = completion.choices[0].message
    # print(completion.choices[0].message)
    return answer


# api_key_request()

# Wczytanie treści artykułu
with open('artykul.txt', 'r', encoding='UTF-8') as file:
    article = file.read()




#
# ask_openai(system_content, user_prompt, article)
