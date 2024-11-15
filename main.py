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
            print(input("Klucz działa! Połączono się z API OpenAI."))
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


def processing_result(result, name):

    result = result.replace("```", "")

    if result.lower().startswith("html"):
        result = result[4:].strip()  # Usuwamy pierwsze 4 znaki i ewentualne białe znaki

    start_index = result.find("<!DOCTYPE html>")
    if start_index != -1:
        result = result[start_index:]

    stop_index = result.find("</html>")
    if stop_index != -1:
        result = result[:stop_index + len("</html>")]

    # Zapisanie wygenerowanego HTML do pliku
    with open(f"{name}.html", "w", encoding="UTF-8") as output_file:
        output_file.write(result)


if __name__ == "__main__":

    # Zdefiniowanie domyślnych zmiennych
    execution_1 = True;
    system_content = "\nJesteś ekspertem w tworzeniu stron internetowych w HTML.\n" \
                         "Twoje zadanie to wygenerowanie kodu HTML na podstawie przesłanego artykułu, \n" \
                         "który spełnia wymagania przesłane przez użytkownika."

    user_prompt = "\nAby wygenerować kod HTML wykorzystaj odpowiednie tagi HTML do strukturyzacji treści, \n" \
                    "takie jak nagłówki, akapity, listy oraz tagi formatowania. \n" \
                    "Na podstawie tekstu wybierz miejsca, w których twoim zdaniem powinny znajdować się ilustracje i wstaw w nie tagi `<img>` \n" \
                    "z atrybutem `src=image_placeholder.jpg` oraz atrybutem `alt`, który powinien zawierać dokładny opis obrazka. \n"  \
                    "Do każdego obrazu dodaj podpis używając tagu `<figcaption>`. \n" \
                    "Zwróć tylko kod HTML do umieszczenia pomiędzy tagami `<body>` i `</body>`. \n" \
                    "Nie dołączaj tagów `<html>`, `<head>`, ani `<body>`, ani żadnych stylów CSS i skryptów JavaScript.\n" \
                    "Podziel kod na kontenery, sekcje, dodaj klasy i identyfikatory. Kod ma być gotowy do dodania stylów CSS." \


    while True:

        if execution_1:
            api_key_request()
            execution_1 = False

        # Wczytanie treści artykułu
        with open('artykul.txt', 'r', encoding='UTF-8') as file:
            article = file.read()
            print(input("Poprawnie wczytano artykuł, przejdź dalej."))

        print(input("Dane które zostaną przesłane do OpenAi:\n"
              "1. Treść artykułu (article),\n"
              "2. Wiadomość użytkownika (user_prompt),\n"
              "3. Instrukcja dla systemu (system_content)\n"
              "\nW kolejnym etapie zaakceptuj je bądź ustaw nowe."))

        while True:

            # akceptacja danych gotowych do przekazania do OpenAI
            system_content = accept_arguments("Instrukcja dla systemu (system_content): ", system_content)
            user_prompt = accept_arguments("\nWiadomość użytkownika (user_prompt): ", user_prompt)


            print("\nGenerowanie odpowiedzi...")
            answer = ask_openai(system_content, user_prompt, article)
            processing_result(answer, "artykul")
            print("\nAI wygenerowało kod artykułu, sprawdź go w pliku artykul.html.\n"
                      "Wciśnij enter jeśli go akceptujesz, w przeciwnym wypadku będziesz mógł zaktualiować prompty i wygenerować nową odpowiedź.")
            accept = input()
            if accept == "":
                break

        if accept == "":
            break
