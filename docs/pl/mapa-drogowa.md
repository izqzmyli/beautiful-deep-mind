# Mapa drogowa

## Wizja

Beautiful Deep Mind bada pytanie o świadomość i przepaść między obliczeniami a poznaniem — budując modele oprogramowania pamięci, refleksji, samomodelowania i ciągłości, i badając, gdzie te modele działają, gdzie zawodzą, i co te porażki ujawniają.

BDM nie twierdzi, że tworzy świadomość. Nie próbuje kopiować, przesyłać ani zachowywać ludzkiego umysłu. To eksperymentalny projekt programistyczny i badawczy. Każda faza przynosi działające oprogramowanie, opublikowane wyniki badań, lub obie.

---

## Milestone 0 — Fundament projektu

**Status: Zakończony**

**Cel:** Ustanowienie konceptualnego, prawnego i dokumentacyjnego fundamentu. Projekt musi istnieć jako poważne repozytorium z jasnym zakresem, zasadami i ograniczeniami zanim zostanie napisany jakikolwiek kod.

**Moduły:**
- M0.1 — Struktura repozytorium
- M0.2 — Manifest
- M0.3 — Koncepcja architektury
- M0.4 — Etyka i ograniczenia
- M0.5 — Licencja i zasady wkładu
- M0.6 — Mapa drogowa

**Wyniki:** `README.md`, `LICENSE.md`, `CONTRIBUTING.md`, `docs/`, `research/`, `concepts/`, `.ai/`, `.github/`

**Ograniczenia:** Brak działającego oprogramowania. Wszystkie opisy architektoniczne są konceptualne.

---

## Milestone 1 — Rdzeń pamięci

**Status: W toku**

**Cel:** Zbudowanie pierwszej trwałej warstwy pamięci. To fundament, od którego zależy wszystko inne. Bez działającej pamięci przeżywającej sesje pytania badawcze o ciągłość, tożsamość i luki świadomości nie mogą być testowane.

**Moduły:**
- M1.1 — `MemoryEvent` z typem, tagami, istotnością, pewnością
- M1.2 — Abstrakcyjna klasa bazowa `MemoryStore`
- M1.3 — `ShortTermBuffer` — ograniczony bufor FIFO w pamięci
- M1.4 — `LongTermStore` — teraz SQLite, wcześniej dict w pamięci
- M1.5 — `EpisodicRecord` — strukturalny epizod z kontekstem sesji
- M1.6 — Wyszukiwanie w pamięci: po tagu, typie, treści
- M1.7 — Ocenianie ważności i pewności

**Oczekiwane wyniki:**
- Działający pakiet pamięci z testami
- `LongTermStore` oparty na SQLite
- `examples/memory_demo.py`

**Ograniczenia:** Brak integracji refleksji ani modelu siebie. Brak wyszukiwania semantycznego/embeddingowego. Schemat SQLite jest wstępny.

---

## Milestone 2 — Pętla refleksji

**Status: Planowany**

**Cel:** Zbudowanie pętli, gdzie system pobiera istotną pamięć, reflektuje nad kontekstem, przygotowuje strukturalny kontekst odpowiedzi i zapisuje wynik po interakcji.

**Przepływ:**
```
wejście → pobranie pamięci → refleksja → budowanie kontekstu → wyjście → zapis wyniku
```

**Moduły:**
- M2.1 — Analizator wejścia
- M2.2 — Pobieranie pamięci (warstwa uwagi)
- M2.3 — Silnik refleksji (najpierw oparty na regułach, potem wspomagany LLM)
- M2.4 — Konstruktor kontekstu odpowiedzi
- M2.5 — Aktualizator pamięci po interakcji

**Oczekiwane wyniki:**
- Działająca pętla refleksji bez zależności od LLM
- `examples/reflection_demo.py`
- Testy dla każdego modułu

**Ograniczenia:** Jakość refleksji jest ograniczona bez pomocy LLM. Detekcja spójności oparta na regułach przeoczy subtelne niespójności. Opóźnienie nie jest jeszcze zoptymalizowane.

**Zależy od:** Ukończenia Milestone 1

---

## Milestone 3 — Model siebie

**Status: Planowany**

**Cel:** Stworzenie strukturalnej reprezentacji stanu wiedzy systemu: aktywnych celów, znanych ograniczeń, pokrycia tematycznego i bieżącego fokusa. Model siebie może być odpytywany i wstrzykiwany do promptów LLM.

**Moduły:**
- M3.1 — Stan projektu
- M3.2 — Aktywne cele
- M3.3 — Znane ograniczenia
- M3.4 — Bieżący fokus
- M3.5 — Opis tożsamości

**Oczekiwane wyniki:**
- `SelfModelState` z celami, ograniczeniami i inwentarzem tematów
- Integracja z pętlą refleksji
- Testy

**Ograniczenia:** Model siebie to struktura danych, nie samoświadomość. Ocena pewności jest przybliżona. Model siebie odzwierciedla przechowywaną wiedzę, nie wywnioskowaną.

**Zależy od:** Ukończenia Milestone 1

---

## Milestone 4 — Ciągłość kontekstu

**Status: Planowany**

**Cel:** Utrzymanie spójnego kontekstu między sesjami przez serializację sesji, podsumowania, śledzenie stanu i rekonstrukcję długoterminowego kontekstu.

**Moduły:**
- M4.1 — Model sesji
- M4.2 — Generator podsumowania kontekstu
- M4.3 — Tracker ciągłości
- M4.4 — Most sesja-pamięć
- M4.5 — Rekonstrukcja długoterminowego kontekstu

**Oczekiwane wyniki:**
- Sesje z cyklem życia otwarcia/zamknięcia
- Podsumowania sesji zapisywane w pamięci długoterminowej
- Rekonstrukcja kontekstu z wcześniejszych podsumowań
- `examples/continuity_demo.py`

**Ograniczenia:** Sesje po długich przerwach mogą dawać nieakualny kontekst. Jakość podsumowań zależy od jakości przechowywanych zdarzeń. Implikacje prywatności przechowywania między sesjami muszą być explicite omówione.

**Zależy od:** Milestones 1, 2, 3

---

## Milestone 5 — Integracja LLM

**Status: Planowany**

**Cel:** Połączenie BDM Core z modelem językowym przez interfejs dostawcy, z kontekstem promptów świadomym pamięci.

**Moduły:**
- M5.1 — Abstrakcyjny interfejs `LLMProvider`
- M5.2 — Konstruktor kontekstu promptów
- M5.3 — Chat świadomy pamięci
- M5.4 — Chat świadomy refleksji
- M5.5 — Granice bezpieczeństwa

**Oczekiwane wyniki:**
- Wtykowy interfejs dostawcy LLM (mock + prawdziwy)
- Chat świadomy pamięci z wstrzykiwaniem kontekstu
- Pętla refleksji zintegrowana w pipeline odpowiedzi
- Warstwa bezpieczeństwa zapobiegająca twierdzeniom o świadomości i medycznym w wyjściu

**Ograniczenia:** Ocena jakości jest częściowo subiektywna. Wyniki są specyficzne dla użytego LLM. Integracja dodaje opóźnienie. Koszty API ograniczają skalę eksperymentów.

**Zależy od:** Milestones 1, 2, 3, 4

---

## Milestone 6 — CLI / Demo lokalne

**Status: Planowany**

**Cel:** Lokalny interfejs wiersza poleceń demonstrujący możliwości BDM Core w użytecznej formie.

**Komendy:**
```bash
bdm memory add "..."
bdm memory list
bdm memory search "..."
bdm reflect "..."
bdm chat
bdm session summary
```

**Oczekiwane wyniki:**
- Pakiet `packages/bdm-cli/`
- Wszystkie wymienione komendy działające end-to-end
- `README.md` dla `bdm-cli`

**Ograniczenia:** Nie jest narzędziem produkcyjnym. CLI to demo i pomoc deweloperska, nie produkt dla użytkownika.

**Zależy od:** Milestones 1–5

---

## Milestone 7 — Eksperymenty i ewaluacja

**Status: Planowany**

**Cel:** Przeprowadzenie strukturalnych eksperymentów w celu oceny, czy warstwy BDM przynoszą mierzalne ulepszenia w spójności, konsekwencji i retencji kontekstu. Otwarte publikowanie wyników, w tym negatywnych.

**Eksperymenty:**
- M7.1 — Test trwałości pamięci (H1)
- M7.2 — Test spójności refleksji (H2)
- M7.3 — Test aktualizacji przekonań (H3)
- M7.4 — Test ciągłości między sesjami (H4)
- M7.5 — Test stabilności modelu siebie (H3)
- M7.6 — Test różnic strukturalnych pamięci (H6)
- M7.7 — Test granic ucieleśnienia (H7)

**Oczekiwane wyniki:**
- Skrypty eksperymentów w `research/scripts/`
- Wyniki w `research/results/`
- `research/findings.md` — podsumowanie wniosków
- Zrewidowane lub wycofane hipotezy na podstawie wyników

**Ograniczenia:** Wyniki będą specyficzne dla testowanych systemów i LLM. Zautomatyzowane metryki spójności są niedoskonałe. Uogólnialność jest niepewna. Niektóre hipotezy prawdopodobnie zostaną sfalsyfikowane.

**Zależy od:** Milestones 1–6

---

*Ta mapa drogowa jest dokumentem roboczym. Będzie aktualizowana w miarę postępu projektu. Statusy milestones są śledzone w `.ai/milestones.md`.*
