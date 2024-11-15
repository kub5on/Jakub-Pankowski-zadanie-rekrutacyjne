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


def ask_openai(f_system_content, f_user_prompt, f_article):

    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f_system_content},
            {"role": "user", "content": f_user_prompt + f_article}
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

    result = result.replace("```", "")

    if result.lower().startswith("html"):
        result = result[4:].strip()  # Usuwamy pierwsze 4 znaki i ewentualne białe znaki

    # Zapisanie wygenerowanego HTML do pliku
    with open("artykul.html", "w", encoding="UTF-8") as output_file:
        output_file.write(result)


# Define variables
execution = True;
system_content = "\nJesteś ekspertem w tworzeniu stron internetowych w HTML.\n" \
                     "Twoje zadanie to stworzenie kodu HTML dla artykułu, który spełnia wymagania przesłane przez użytkownika."

user_prompt = "\n1. Wykorzystaj odpowiednie tagi HTML do strukturyzacji treści, takie jak nagłówki `<h1>`, `<h2>`, akapity `<p>`, listy `<ul>`, `<li>`, oraz tagi formatowania jak `<strong>`, `<em>`. \n" \
                  "2. Wybierz miejsca, w których twoim zdaniem powinny znajdować się ilustracje i wstaw w nie tagi `<img>` z atrybutem `src=image_placeholder.jpg` oraz atrybutem `alt`, \n" \
                  "   który powinien zawierać dokładny opis obrazka. \n"  \
                  "3. Do każdego obrazu dodaj podpis używając tagu `<figcaption>`. \n" \
                  "4. Zwróć tylko kod HTML do umieszczenia pomiędzy tagami `<body>` i `</body>`. Nie dołączaj tagów `<html>`, `<head>`, ani `<body>`, ani żadnych stylów CSS i skryptów JavaScript."

while True:

    if execution == True:
        api_key_request()
        execution = False

    # Wczytanie treści artykułu
    with open('artykul.txt', 'r', encoding='UTF-8') as file:
        article = file.read()

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
