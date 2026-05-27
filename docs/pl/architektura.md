# Architektura konceptualna

Niniejszy dokument opisuje konceptualną architekturę systemu BDM. To nie jest implementacja. Dla tej architektury nie istnieje jeszcze żaden kod (poza warstwą pamięci). Celem tego dokumentu jest zdefiniowanie warstw funkcjonalnych, wyjaśnienie ich odpowiedzialności i interfejsów oraz identyfikacja otwartych pytań projektowych dla każdej warstwy.

Wszystkie opisy tu reprezentują intencje projektowe i hipotezy, nie zaimplementowane zachowanie.

---

## Przegląd

Architektura BDM jest zorganizowana jako zestaw kompozytowalnych warstw funkcjonalnych. Każda warstwa ma odrębne przeznaczenie i komunikuje się z sąsiednimi przez zdefiniowane interfejsy.

```
┌─────────────────────────────────┐
│         Warstwa interfejsu      │  ← wejście/wyjście użytkownika i LLM
├─────────────────────────────────┤
│       Ciągłość kontekstu        │  ← trwałość sesji
├─────────────────────────────────┤
│        Warstwa modelu siebie    │  ← reprezentacja stanu wewnętrznego
├─────────────────────────────────┤
│          Pętla uczenia się      │  ← aktualizacja przekonań, przetwarzanie informacji zwrotnych
├─────────────────────────────────┤
│         Warstwa refleksji       │  ← sprawdzanie spójności, przegląd
├─────────────────────────────────┤
│          Warstwa uwagi          │  ← pobieranie pamięci, selekcja kontekstu
├─────────────────────────────────┤
│           Warstwa pamięci       │  ← przechowywanie, indeksowanie, wyszukiwanie
└─────────────────────────────────┘
```

---

## Warstwa pamięci

**Przeznaczenie:** Przechowywanie i wyszukiwanie strukturalnych zapisów doświadczeń, wiedzy i historii interakcji.

**Możliwe odpowiedzialności:**
- Utrzymywanie odrębnych typów zapisów: zapisy epizodyczne (zdarzenia interakcji z sygnaturą czasową), zapisy semantyczne (ogólna wiedza i koncepcje), bufor pamięci roboczej (aktywny kontekst sesji)
- Zapewnianie interfejsu zapytań do wyszukiwania według aktualności, tematu, wyniku istotności lub typu zapisu
- Zarządzanie wygasaniem zapisów, zanikaniem istotności i limitami przechowywania
- Obsługa aktualizacji i rewizji przechowywanych zapisów, gdy nowe informacje zaprzeczają wcześniejszym
- Prowadzenie dziennika audytu operacji pamięci

**Otwarte pytania:**
- Jaki schemat najlepiej oddaje zapisy epizodyczne bez nadmiernego narzutu?
- Jak powinny być obliczane i aktualizowane wyniki istotności — oparte na regułach, embeddingach czy hybrydowo?
- Jaka jest właściwa polityka retencji: zanikanie czasowe, jawne usuwanie czy przycinanie ważone pewnością?
- Jak powinny być obsługiwane sprzeczności między przechowywanymi zapisami — oznaczane, scalane czy zastępowane?

---

## Warstwa uwagi

**Przeznaczenie:** Wybór, które przechowywane wspomnienia i elementy kontekstowe są najbardziej istotne dla bieżącego wejścia, i udostępnianie ich do dalszego przetwarzania.

**Możliwe odpowiedzialności:**
- Odbieranie zapytania (bieżące wejście, zadanie lub pytanie) i zwracanie rankingowego zestawu istotnych zapisów pamięci
- Stosowanie strategii wyszukiwania: ważonej aktualnością, opartej na podobieństwie semantycznym lub filtrowanej tematycznie
- Ograniczanie pobranego kontekstu do tego, co mieści się w oknie kontekstowym systemu downstream
- Prowadzenie dziennika wyszukiwania dla możliwości audytu

**Otwarte pytania:**
- Czy uwaga powinna używać jednej strategii wyszukiwania czy dynamicznie wybierać między strategiami w zależności od typu zapytania?
- Jak oceniać jakość wyszukiwania bez etykiet istotności ground truth?
- Co się dzieje, gdy pobrany kontekst jest sprzeczny?

---

## Warstwa refleksji

**Przeznaczenie:** Przeglądanie wcześniejszych wyjść pod kątem spójności, oznaczanie rozbieżności i opcjonalne stosowanie korekt przed produkcją końcowego wyjścia.

**Możliwe odpowiedzialności:**
- Porównywanie kandydującego wyjścia z przechowywanymi wcześniejszymi wyjściami na ten sam lub powiązany temat
- Wykrywanie jawnych sprzeczności (niespójności faktyczne) i ukrytych niespójności (zmiana stanowiska bez uzasadnienia)
- Produkowanie raportu refleksji: spójny, niespójny lub niepewny
- Opcjonalne rewizja wyjścia w celu rozwiązania wykrytych niespójności
- Logowanie wszystkich zdarzeń refleksji dla audytu

**Otwarte pytania:**
- Czy refleksja powinna być krokiem blokującym (wyjście jest wstrzymane do zakończenia przeglądu) czy asynchronicznym?
- Jak odróżnić uzasadnione aktualizacje wcześniejszych stanowisk od niespójności?
- Jaka jest optymalna częstotliwość refleksji — przy każdym wyjściu, okresowo czy na żądanie?

---

## Pętla uczenia się

**Przeznaczenie:** Aktualizacja przechowywanych stanów wewnętrznych na podstawie nowych informacji, informacji zwrotnych lub wyników z interakcji.

**Możliwe odpowiedzialności:**
- Przetwarzanie jawnych sygnałów informacji zwrotnych (korekty użytkownika, oznaczone błędy) i aktualizowanie istotnych zapisów pamięci
- Dostosowywanie wyników istotności zapisów pamięci na podstawie częstości pobierania lub potwierdzenia
- Zapisywanie nowych zdarzeń epizodycznych generowanych podczas interakcji
- Propagowanie aktualizacji z decyzji refleksji z powrotem do warstwy pamięci
- Prowadzenie dziennika zmian wszystkich zastosowanych aktualizacji

**Otwarte pytania:**
- Co liczy się jako informacja zwrotna? Tylko jawne korekty, czy też sygnały niejawne?
- Jak powinny być rozwiązywane sprzeczne aktualizacje — wygrywa najnowsza, ważona pewnością czy ręcznie?
- Jak zapobiegamy temu, by pętla uczenia się wprowadzała systematyczny dryft w czasie?

---

## Warstwa modelu siebie

**Przeznaczenie:** Utrzymywanie strukturalnej reprezentacji własnego stanu systemu: co wie, czego nie wie, jakie tematy eksplorował i jakie poziomy pewności wiążą się z jego przechowywanymi przekonaniami.

**Możliwe odpowiedzialności:**
- Utrzymywanie inwentarza tematów: tematy, o których system ma przechowywane informacje
- Śledzenie poziomów pewności dla przechowywanych przekonań, aktualizowanych przez pętlę uczenia się
- Zapisywanie uznanych ograniczeń i znanych luk
- Dostarczanie podsumowania stanu modelu siebie do użytku downstream (np. LLM może odwoływać się do niego przy formułowaniu odpowiedzi)

**Otwarte pytania:**
- Jaki jest minimalny schemat przydatnego modelu siebie? Co musi zawierać, co jest narzutem?
- Jak poziomy pewności są przypisywane i aktualizowane w zasadniczy sposób?
- Jak zapobiegamy temu, by model siebie stawał się niedokładny przez dryft?

**Ważna uwaga:** Model siebie to struktura danych. Nie stanowi samoświadomości. Nie implikuje świadomości. To zapis stanu wewnętrznego, nie subiektywne doświadczenie tego stanu.

---

## Warstwa ciągłości kontekstu

**Przeznaczenie:** Zachowanie istotnego stanu wewnętrznego między sesjami, tak aby nowa sesja zaczynała się z dostępem do wcześniejszego kontekstu, a nie od stanu pustego.

**Możliwe odpowiedzialności:**
- Serializacja i przechowywanie stanu sesji na końcu każdej interakcji
- Odtwarzanie istotnego wcześniejszego stanu na początku nowej sesji, filtrowanego według aktualności i istotności
- Stosowanie "protokołu zimnego startu": streszczanie wcześniejszego kontekstu do zwartej reprezentacji
- Zarządzanie granicami sesji i przejściami
- Obsługa wycofywania: przywracanie stanu do wcześniejszego punktu kontrolnego w przypadku wykrycia uszkodzenia lub błędu

**Otwarte pytania:**
- Ile wcześniejszego kontekstu powinno być przywracane? Pełna historia vs. filtrowane pod względem istotności streszczenie?
- Co definiuje granicę sesji? Czasowa, tematyczna czy jawna akcja użytkownika?
- Jak obsługujemy ciągłość po długich przerwach (dni, tygodnie), gdzie wiele wcześniejszego kontekstu może być nieaktualnych?
- Implikacje prywatności: przechowywany stan sesji może zawierać wrażliwe treści — jak jest chroniony?

---

## Warstwa interfejsu

**Przeznaczenie:** Łączenie wszystkich wewnętrznych warstw z zewnętrznymi wejściami (wiadomości użytkownika, wywołania API) i wyjściami (generowane odpowiedzi) oraz z LLM tam, gdzie ma to zastosowanie.

**Możliwe odpowiedzialności:**
- Odbieranie przychodzącego wejścia i kierowanie go przez pipeline przetwarzania
- Wstrzykiwanie pobranego kontekstu pamięci i stanu modelu siebie do promptów LLM
- Odbieranie wyjść LLM i przekazywanie ich do warstwy refleksji
- Zwracanie końcowych wyjść do użytkownika lub systemu wywołującego
- Udostępnianie interfejsu konfiguracji do włączania lub wyłączania warstw
- Zapewnianie hooków logowania i obserwowalności do debugowania i ewaluacji

**Otwarte pytania:**
- Czy warstwa interfejsu powinna być od początku niezależna od LLM (zdolna do wymiany modelu)?
- Jak powinno być strukturowane wstrzykiwanie kontekstu promptu — systemowy prompt, wiadomość użytkownika czy dedykowany format?
- Jak zapobiegamy temu, by warstwa interfejsu stała się wąskim gardłem lub pojedynczym punktem awarii?

---

*Ta architektura jest konceptualna. Wszystkie opisy warstw reprezentują intencje projektowe. Na tym etapie implementacja nie istnieje dla większości warstw.*
