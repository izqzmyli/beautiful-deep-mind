# Refleksja

## Definicja

Refleksja to zdolność do przeglądania i rozumowania o własnych wcześniejszych wyjściach, procesach rozumowania lub stanie wiedzy. W kognitywistyce metapoznanie — myślenie o myśleniu — to szerszy framework, w którym mieści się refleksja. W BDM refleksja jest zdefiniowana węziej jako proces obliczeniowy: dane kandydujące wyjście, porównaj je z wcześniejszymi wyjściami i oznacz lub popraw niespójności.

---

## Dlaczego ma znaczenie

Systemy generujące wyjścia bez przeglądania ich pod kątem spójności mogą dryfować w czasie. Pojedyncza sesja z dobrze skalibrowanym systemem może wyglądać spójnie. Ale przez wiele sesji i wielu tematów, bez żadnego mechanizmu sprawdzania spójności, sprzeczności się kumulują. System może stwierdzać X w jednym kontekście i nie-X w innym, bez mechanizmu wykrywania ani rozwiązywania konfliktu.

Refleksja to mechanizm adresujący ten problem. Nie chodzi o osiągnięcie filozoficznej samoświadomości — chodzi o implementację strukturalnego przeglądu, który wychwytuje wykrywalne niespójności zanim trafią do użytkowników.

---

## Możliwa reprezentacja w oprogramowaniu

Moduł refleksji w BDM byłby implementowany jako krok post-przetwarzania w pipeline wyjść:

1. Kandydujące wyjście jest generowane przez LLM
2. Moduł refleksji pobiera wcześniejsze wyjścia na ten sam lub powiązane tematy z zasobu pamięci
3. Moduł refleksji porównuje kandydujące wyjście z wcześniejszymi wyjściami
4. W przypadku wykrycia potencjalnej niespójności moduł produkuje raport refleksji:
   - `consistent` — nie wykryto sprzeczności, wyjście zatwierdzone
   - `inconsistent` — wykryto sprzeczność, oznacz do rewizji
   - `uncertain` — porównanie niejednoznaczne, oznacz do przeglądu
5. W przypadku niespójności moduł opcjonalnie generuje zrewidowane wyjście lub przekazuje flagę dalej

Krok porównania mógłby być:
- **Oparty na regułach:** jawna detekcja sprzeczności (np. "A" vs. "nie A" dla tego samego faktu)
- **Wspomagany LLM:** wtórny prompt prosi LLM o porównanie kandydata z wcześniejszymi wyjściami i ocenę spójności
- **Hybrydowy:** detekcja oparta na regułach dla rażących sprzeczności, wspomagana LLM dla subtelnych

---

## Otwarte pytania

- Czy refleksja powinna być blokująca (wstrzymuje wyjście do zakończenia przeglądu) czy asynchroniczna (oznacza niespójności po fakcie)?
- Jak odróżnić uzasadnioną aktualizację wcześniejszego stanowiska od niespójności?
- Jaki jest koszt obliczeniowy refleksji i w jakiej skali staje się niepraktyczna?
- Czy refleksja może być rzetelnie ewaluowana? Jakie metryki mogą odróżnić dobrą refleksję od złej?
- Czy istnieje ryzyko, że refleksja spowoduje, że wyjście stanie się nadmiernie ostrożne — konsekwentnie ostrożne zamiast angażowania się w stanowiska?

---

## Związek z BDM

Refleksja to trzecia warstwa w architekturze BDM. Zależy od warstwy pamięci (do pobierania wcześniejszych wyjść do porównania) i warstwy uwagi (do efektywnego udostępniania istotnych wcześniejszych wyjść). Zasila pętlę uczenia się: gdy refleksja wykryje niespójność i zostanie dokonana rewizja, ta rewizja może wywołać aktualizację zasobu pamięci.

Refleksja jest również ściśle związana z warstwą modelu siebie: model siebie może reprezentować znany rekord spójności systemu, a zdarzenia refleksji mogą go aktualizować.
