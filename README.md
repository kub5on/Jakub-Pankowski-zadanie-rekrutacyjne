# Aplikacja do generowania kodu HTML na podstawie artykułu

## Opis

Aplikacja łączy się z API OpenAI, co umożliwia generowanie kodu HTML przez AI na podstawie artykułu tekstowego.
Użytkownik ma za zadanie wprowadzić dane wejściowe (prompty), które są przesyłane do OpenAI, a w odpowiedzi aplikacja generuje 
kod HTML z odpowiednimi tagami, strukturą i propozycjami miejsc na grafiki. 
Wygenerowany kod HTML może być użyty do wstawienia artykułu do strony internetowej.

## Instrukcje uruchomienia

### 1. Wymagania wstępne

- Python od wersji 3.8
- Klucz API OpenAI dodany do zmiennych środowiskowych 
  bądź gotowy do wklejenia do aplikacji
- biblioteka openai

### 2. Uruchomienie aplikacji

Należy pobrać folder Jakub-Pankowski-zadanie-rekrutacyjne i otworzyć go za pomocą
dowolnego środowiska umożliwiającego programowanie w języku Python (np. PyCharm). Następnie należy
uruchomić program main.py, w którym znajduję się główny kod stworzonej aplikacji. Program z zadania
dla chętnych znajduje się w pliku additional_task.py i działa analogicznie do programu main.py.

### 4. Działanie aplikacji krok po kroku

Po uruchomieniu pliku main.py aplikacja w pierwszej kolejności sprawdza czy klucz API OpenAI znajduję
się w zmiennych środowiskowych systemu, jeżeli tak to program wykonuję się dalej (nazwa zmiennej
środowiskowej musi mieć nazwę "OPENAI_API_KEY"!!). W przeciwnym wypadku program poprosi użytkownika
o podanie swojego klucza, a następnie sprawdzi jego poprawność. Nie można przejść dalej bez podania poprawnego klucza.

Następnie zostaje wczytany artykuł. Po tej operacji można przystąpić do zaakceptowania bądź
zaktualizowania promptów wysyłanych później do API OpenAI. Zostały ustawione domyśle prompty zgodnie z instrukcją
zadania, jednak istnieje możliwość ich aktualizacji. Po sprawdzeniu prompta należy wpisać jego nową 
wersję bądź zatwierdzić domyślny.

Po zatwierdzeniu promptów, zapytania wraz z artykułem zostają wysłane do API OpenAI. AI generuje odpowiedź która 
zapisuje się w pliku artykul.html. Jeżeli użytkownik nie jest usatysfakcjnowany odpowiedzią może przejść ponowie 
do wpisywania promptów wpisując dowolny znak na klawiaturze (za wyjątkiem enter!)

### 5. Działanie aplikacji (zadanie dla chętnych)

Zadanie dla chętnych działa analogicznie jak program główny. Znajduje się ono w pliku additional_task.py.
Różni się ono promptami oraz tym, że na wyjściu otrzymujemy pliki szablon.html oraz podglad.html.
Program składa się z dwóch zapytań wysyłanych do OpenAI - pierwsze tworzy plik szablon.html, a drugie plik
podglad.html z plikow artykul.html i szablon.html.

### Uwagi

- Aby przechodzić do kolejnych etapów w aplikacji należy wciskać enter.
- W plikach artykul.html, szablon.html oraz podglad.html znajdują się ostatnie wygenerowane przez aplikacje pliki.
Uruchomienie aplikacji i przejście przez wszytstkie jej etapy spowoduje nadpisanie odpowiednich plików.


