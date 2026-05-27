# Pętla uczenia się

## Definicja

Pętla uczenia się to mechanizm, przez który system aktualizuje swój stan wewnętrzny na podstawie nowych informacji, informacji zwrotnych lub wyników z interakcji. W BDM uczenie się nie odnosi się do gradientu ani aktualizacji wag modelu. Odnosi się do strukturalnych modyfikacji przechowywanych danych: aktualizowania przekonań, rewizji wyników istotności, zapisywania nowych zdarzeń epizodycznych, propagowania korekt z decyzji refleksji.

---

## Dlaczego ma znaczenie

System, który nie może aktualizować swojego stanu wewnętrznego, jest statyczny. Może działać dobrze w jednej sesji, ale nie może się poprawiać na podstawie informacji zwrotnych, adaptować do nowych informacji ani korygować wcześniejszych błędów w czasie. Uczenie się — nawet w ograniczonym sensie aktualizowania przechowywanych zapisów — to mechanizm, przez który system staje się dokładniejszy i bardziej użyteczny w kolejnych interakcjach.

Pętla uczenia się to również mechanizm, przez który inne warstwy BDM wzajemnie na siebie wpływają: decyzje refleksji zasialją aktualizacje pamięci, informacje zwrotne użytkownika aktualizują wyniki istotności, a nowe zdarzenia epizodyczne rozszerzają zasób pamięci.

---

## Możliwa reprezentacja w oprogramowaniu

Pętla uczenia się w BDM działałaby jako mechanizm aktualizacji sterowany zdarzeniami:

**Wyzwalacze uczenia:**
- Jawna informacja zwrotna użytkownika (korekta, potwierdzenie lub oznaczenie)
- Wyjście modułu refleksji (wykryta niespójność, wygenerowana rewizja)
- Nowe zdarzenie epizodyczne na końcu sesji
- Zaplanowany przegląd (np. zanikanie istotności)

**Typy aktualizacji:**
- **Aktualizacja przekonania:** modyfikacja lub zastąpienie przechowanego zapisu semantycznego, gdy potwierdzone są nowe sprzeczne informacje
- **Aktualizacja istotności:** zwiększenie lub zmniejszenie wyniku istotności zapisu pamięci na podstawie częstości wyszukiwania lub informacji zwrotnych użytkownika
- **Dołączanie epizodyczne:** zapisanie nowego zapisu epizodycznego podsumowującego zakończoną interakcję
- **Rozwiązywanie niespójności:** oznaczanie sprzecznych zapisów, archiwizowanie zastąpionej wersji i promowanie zrewidowanej

**Logowanie:**
Każda aktualizacja powinna być logowana: co się zmieniło, co wywołało zmianę, kiedy i jaki był poprzedni stan. Jest to warunek konieczny dla możliwości audytu i cofnięcia.

---

## Otwarte pytania

- Co liczy się jako "informacja zwrotna" do wywołania aktualizacji uczenia? Tylko jawne korekty, czy też sygnały niejawne?
- Jak zapobiegamy temu, by pętla uczenia się wprowadzała systematyczny dryft — gdzie wczesne nieprawidłowe przekonania propagują się i się kumulują?
- Jaki jest mechanizm wycofywania, gdy aktualizacja uczenia okazuje się nieprawidłowa?
- Jak wykrywamy, gdy pętla uczenia się degraduje, a nie poprawia wydajność?
- Czy istnieje punkt, w którym skumulowane aktualizacje wymagają pełnego przeglądu spójności, a nie aktualizacji przyrostowych?

---

## Związek z BDM

Pętla uczenia się siedzi w centrum architektury BDM jako mechanizm utrzymujący aktualne wszystkie inne warstwy. Konsumuje wyjście z refleksji i z warstwy interfejsu, i zapisuje z powrotem do warstwy pamięci i warstwy modelu siebie. Bez pętli uczenia się BDM byłby systemem tylko do odczytu: zdolnym do pobierania i używania przechowywanych wiedzy, ale niezdolnym do jej aktualizowania na podstawie doświadczenia.

Pętla uczenia się to to, co sprawia, że system jest adaptacyjny, a nie tylko trwały.
