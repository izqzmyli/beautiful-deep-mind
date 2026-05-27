# Ciągłość

## Definicja

Ciągłość, w kontekście BDM, oznacza zachowanie istotnego stanu wewnętrznego między sesjami, interakcjami lub w czasie. System ma ciągłość, jeśli informacje z wcześniejszych interakcji mogą wpływać na bieżące zachowanie w sposób strukturalny, możliwy do wyszukania i audytowania.

Ciągłość nie oznacza doskonałej pamięci wszystkiego. Oznacza, że istotny wcześniejszy stan jest dostępny, a nie utracony, gdy zaczyna się nowa sesja.

---

## Dlaczego ma znaczenie

Bez ciągłości każda sesja zaczyna od zera. System nie może odwoływać się do wcześniejszych zobowiązań, budować na wcześniejszych wymianach, korygować błędów z poprzednich interakcji ani akumulować wiedzy w czasie. To fundamentalne ograniczenie dla każdego systemu mającego być użytecznym przez wiele sesji lub przez dłuższy czas.

Ciągłość to również właściwość, która najściślej łączy projekt BDM z pytaniem poznawczym, które pierwotnie go zainspirowało: jak umysł utrzymuje spójne poczucie kontekstu i tożsamości w czasie? W systemach biologicznych jest to wspierane przez konsolidację pamięci, długoterminowe wzmacnianie synaptyczne i trwałość zapisów epizodycznych. W BDM ciągłość to decyzja projektowa oprogramowania.

Co ważne, ciągłość to nie to samo co niezmienność. System z dobrą ciągłością może aktualizować, rewidować i zapominać — ale robi to w sposób strukturalny i zasadniczy, nie przez arbitralne tracenie stanu.

---

## Możliwa reprezentacja w oprogramowaniu

Warstwa ciągłości kontekstu BDM byłaby odpowiedzialna za:

1. **Serializację sesji:** Na końcu każdej sesji serializacja aktywnego stanu zasobu pamięci, modelu siebie i podsumowania interakcji do trwałego przechowywania
2. **Odtwarzanie sesji:** Na początku nowej sesji ładowanie utrwalonego stanu i wstrzykiwanie skompresowanego podsumowania wcześniejszego kontekstu do bieżącej sesji
3. **Protokół zimnego startu:** Przy uruchamianiu po długiej przerwie produkowanie "briefu wznowienia" — zwartego podsumowania najbardziej istotnego wcześniejszego stanu — zamiast próby wstrzyknięcia pełnej historii
4. **Zarządzanie przestarzałością:** Oznaczanie zapisów jako przestarzałych po konfigurowalnych progach czasowych, tak by stare informacje nie były prezentowane jako aktualne
5. **Obsługa wycofywania:** Utrzymywanie punktów kontrolnych, aby uszkodzony lub zdegradowany stan mógł być przywrócony do poprzedniego dobrze-działającego punktu

---

## Otwarte pytania

- Ile wcześniejszego kontekstu powinno być odtwarzane przy starcie sesji? Pełna historia jest niepraktyczna; zbyt mało niweczy cel
- Jak system powinien obsługiwać długie przerwy (dni, tygodnie) między sesjami, gdzie wiele wcześniejszego kontekstu może być przestarzałych lub nieistotnych?
- Co definiuje granicę sesji? Oparta na czasie, tematyczna, jawna akcja użytkownika, czy kombinacja?
- Jak warstwa ciągłości powinna wchodzić w interakcję z wymogiem prywatności, że użytkownicy mogą przeglądać i usuwać przechowywany stan?
- Co się dzieje, gdy zasób pamięci rośnie bardzo przez wiele sesji — jak powinien być kompresowany lub przycinany bez utraty krytycznego kontekstu?

---

## Związek z BDM

Ciągłość to warstwa, która sprawia, że pamięć, model siebie i pętla uczenia się BDM są użyteczne w czasie, a nie tylko w obrębie jednej sesji. Bez ciągłości wszystkie inne warstwy resetują się na końcu sesji. Z ciągłością system akumuluje doświadczenie, utrzymuje spójność w czasie i wykazuje adaptacyjne zachowanie, którego bezstanowy system nie może.

Ciągłość to również miejsce, gdzie obawy o prywatność i bezpieczeństwo są najbardziej aktualne: co jest przechowywane, jak jest chronione i jak może być usunięte — to pytania projektowe, które muszą być rozwiązane równolegle z techniczną implementacją.
