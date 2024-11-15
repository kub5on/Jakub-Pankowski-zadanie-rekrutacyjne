from openai import OpenAI
import openai
import os
from main import api_key_request, ask_openai, accept_arguments, processing_result

execution_1 = True;
system_content = "\nJesteś ekspertem w tworzeniu stron internetowych w HTML.\n" \
                 "Twoje zadanie to stworzenie pliku z kodem HTML na podstawie kodu artykułu, \n" \
                 "który spełnia wymagania przesłane przez użytkownika."

user_prompt = "\nWygeneruj szablon HTML gotowy do wklejenia artykułu. Sekcja '<body>' musi pozostać całkowicie pusta! Nic tam nie dodawaj!\n" \
              "Opracuj dodatkowo style CSS na podstawie nazw sekcji, kontenerów, nazw klas i identyfikatorów zawartych w kodzie artykułu.\n" \
              "Wszystkie nazwy styli CSS mają się zgadzać, z nazwami w kodzie artykułu."

final_system_content = "\nJesteś ekspertem w tworzeniu stron internetowych w HTML.\n" \
                       "Otrzymujesz dwa pliki tekstowe z kodem html, scal je w jeden plik."


while True:

    if execution_1:
        api_key_request()
        execution_1 = False

    # Wczytanie treści artykułu
    with open('artykul.html', 'r', encoding='UTF-8') as file:
        article = file.read()
        print(input("Poprawnie wczytano artykuł, przejdź dalej."))

    while True:

        # akceptacja danych gotowych do przekazania do OpenAI
        user_prompt = accept_arguments("Wiadomość użytkownika (user_prompt): ", user_prompt)
        system_content = accept_arguments("\nInstrukcja dla systemu (system_content): ", system_content)


        print("\nGenerowanie odpowiedzi...")
        answer = ask_openai(system_content, user_prompt, article)
        processing_result(answer, "szablon")
        print("\nAI wygenerowało szablon, sprawdź go w pliku szablon.html.\n"
                  "Wciśnij enter jeśli go akceptujesz, w przeciwnym wypadku będziesz mógł zaktualiować prompty i wygenerować nową odpowiedź.")
        accept = input()
        if accept == "":
            break

    while True:

        # akceptacja danych gotowych do przekazania do OpenAI
        final_system_content = accept_arguments("\nInstrukcja dla systemu (system_content): ", final_system_content)


        print("\nGenerowanie odpowiedzi...")
        answer = ask_openai(system_content, answer, article)
        processing_result(answer, "podglad")
        print("\nAI wygenerowało szablon, sprawdź go w pliku szablon.html.\n"
                  "Wciśnij enter jeśli go akceptujesz, w przeciwnym wypadku będziesz mógł zaktualiować prompty i wygenerować nową odpowiedź.")
        accept = input()
        if accept == "":
            break


    if accept == "":
        break
