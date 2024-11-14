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
    # answer = completion.choices[0].message['content']
    # print(completion.choices[0].message)
    # return answer
    result = completion.choices[0].message.content  # Pobiera tekst odpowiedzi
    return result


def accept_arguments(name, value):
    new_value = input(f"{name}{value} --> ")
    return new_value if new_value else value


def processing_result(result):

    start_index = result.find("<!DOCTYPE html>")
    if start_index != -1:
        result = result[start_index:]

    stop_index = result.find("</html>")
    if stop_index != -1:
        result = result[:stop_index + len("</html>")]

    # Zapisanie wygenerowanego HTML do pliku
    with open("artykul.html", "w", encoding="UTF-8") as output_file:
        output_file.write(result)


api_key_request()

# Wczytanie treści artykułu
with open('artykul.txt', 'r', encoding='UTF-8') as file:
    article = file.read()

system_content = "\nJesteś programistą HTML, twoją pracą jest odpowiednie obrabianie tekstu do wstawienia na stronę internetową."

user_prompt = "\nStwórz kod HTML z artykułem z odpowiednimi tagami HTML do strukturyzacji treści, który zawiera miejsca na obrazy. \n" \
              "Wstaw tagi <img src='image_placeholder.jpg' alt='...' /> tam, gdzie artykuł może wymagać obrazu, \n" \
              "wypełnij atrybut 'alt' odpowiednim opisem dla grafiki, który można wykorzystać do jej wygenerowania.\n" \
              "Dodaj podpisy pod grafikami z użyciem tagu <figcaption>."
                # "Nie generuj kodu CSS ani JavaScript. Kod HTML ma być tylko między tagami <body> i </body>."


print("Dane które zostaną przesłane do OpenAi:\n"
      "1. Treść artykułu (article),\n"
      "2. Wiadomość użytkownika (user_prompt),\n"
      "3. Instrukcja dla systemu (system_content)\n"
      "\nZaakceptuj klikając enter bądź ustaw nowe wartości dla: \n ")

# akceptacja danych gotowych do przekazania do OpenAI
user_prompt = accept_arguments("Wiadomość użytkownika (user_prompt): ", user_prompt)
system_content = accept_arguments("\nInstrukcja dla systemu (system_content): ", system_content)

answer = ask_openai(system_content, user_prompt, article)

processing_result(answer)
