# Biblioteka_Mikroserwisy

Ogólne informacje o projekcie


	Przedmiotem niniejszego zamówienia jest zaprojektowanie i zaprogramowanie prototypu
aplikacji opartej na technologii Flask z wykorzystaniem usług do obsługi procesów zachodzących
w bibliotece.

System informatyczny (SI) powinien zapewnić;

Kontrolę i monitoring nad procesami zachodzącymi przy wypożyczaniu książki z wirtualnej biblioteki
przez użytkownika po ówczesnym zapewnieniu możliwości przeglądania książek dostępnych
do wypożyczenia po zalogowaniu (w przypadku gdy użytkownik posiada konto) lub zarejestrowaniu
się do systemu poprzez utworzenie konta.


Opis procesu wypożyczenia książki

Książka może być wypożyczona przez użytkownika w przypadku gdy spełnione są konkretne warunki.
Wedle tych warunków oraz sposobu wypożyczenia książki w zachodzących procesach można wyróżnić następujące kroki:

1)	W przypadku posiadania konta przez użytkownika następuje proces logowania – w przeciwnym wypadku jest to rejestracja
po czym następuje logowanie
2)	Wyświetlenie książek dostępnych do wypożyczenia
3)	Wybór książki, która interesuje użytkownika
4)	Dodanie książki do listy
5)	Wyświetlenie listy na której znajdują się książki wybrane przez użytkownika
6)	Użytkownik ma możliwość usunięcia książki z listy przed zatwierdzeniem wypożyczenia
7)	Zatwierdzenie książek znajdujących się na liście i zakończenie procesu wypożyczenia
8)	Gdy użytkownik posiada wypożyczone książki może je w każdej chwili zwrócić
9)	Po zakończeniu procesu wypożyczenia lub zwrócenia książki użytkownik może się wylogować.

Wymagania funkcjonalne SI

Opis ogólny
	System informatyczny składa się z 4 głównych modułów, które są opisane szczegółowo
w dalszej części dokumentu.
	Do pierwszego modułu należy moduł rejestracji, który pozwala nowemu użytkownikowi założyć konto aby mieć dostęp do funkcjonalności, które oferuje system informatyczny. Kolejnym modułem jest moduł logowania, która po weryfikacji czy login i hasło są prawidłowe pozwala użytkownikowi na przejście do kluczowych funkcji systemu. Trzecim modułem jest moduł wypożyczenia książki polegający na wyświetleniu bazy dostępnych książek co daje opcję wyboru książek, które interesują użytkownika. Do ostatniego modułu należy moduł zwrócenia książki z listy wypożyczonych książek przez aktualnie zalogowanego użytkownika.

Użytkownicy systemu

Wyszczególnieni użytkownicy systemu:

- Admin, konto główne – AKG
- Regularny użytkownik – RU


Opis uprawnień

1)	Moduł Admin
AKG musi posiadać dostęp do rejestracji w SI oraz do logowania do modułu wyznaczonego konkretnie dla niego.
Po zalogowaniu – AKG powinien mieć dostęp do wyświetlenia listy użytkowników posiadających konto, wyświetlania i edycji
bazy danych książek (dodawanie i usuwanie pozycji), weryfikacja użytkowników a także ich usuwanie jak i możliwość edycji na żądanie.
Może także podejrzeć który użytkownik wypożyczył konkretną pozycję i czy, np. zalega z jej zwrotem.

2)	Moduł regularny użytkownik
RU posiada dostęp do rejestracji w przypadku gdy nie posiada konta.
Po zarejestrowaniu w systemie zostaje przekierowany do modułu logowania do systemu co pozwoli na dostęp do funkcjonalności
ferowanych przez system takich jak, np. przejrzenie i wypożyczenie konkretnej książki lub wielu książek bądź także w przypadku
wypożyczonej książki – możliwość jej zwrotu.