# Podstawy teoretyczne

Niniejszy dokument opisuje konceptualne i teoretyczne podstawy BDM. Cała treść stanowi kierunki badawcze i robocze hipotezy, nie ustalone wyniki. Celem jest identyfikacja istotnych koncepcji z kognitywistyki i badań nad AI oraz ich ujęcie jako pojęć przydatnych z perspektywy oprogramowania.

---

## Architektura poznawcza

Architektura poznawcza to framework definiujący stałe struktury i procesy leżące u podstaw inteligentnego zachowania. Klasyczne przykłady to ACT-R, SOAR i CLARION — modele opracowane w kognitywistyce, opisujące funkcjonalną strukturę ludzkiego poznania.

BDM nie próbuje replikować żadnej konkretnej architektury poznawczej. Czerpie z ich ogólnego podejścia: definiowania odrębnych warstw funkcjonalnych (pamięć, uwaga, rozumowanie, uczenie się) i określania, jak te warstwy ze sobą współdziałają.

**Kluczowe pytanie:** Jaki jest minimalny zestaw warstw funkcjonalnych potrzebnych do uzyskania spójnego, refleksyjnego zachowania systemu oprogramowania?

---

## Systemy pamięci

Pamięć w kognitywistyce nie jest jednym systemem. Wyróżnia się między innymi:

- **Pamięć robocza** — aktywna przestrzeń robocza dla bieżącego przetwarzania
- **Pamięć epizodyczna** — zapisy konkretnych zdarzeń z metadanymi czasowymi i kontekstowymi
- **Pamięć semantyczna** — wiedza ogólna i relacje pojęciowe
- **Pamięć proceduralna** — wyuczone umiejętności i procedury

Dla BDM istotne pytanie to nie to, jak replikować te systemy biologiczne, lecz czy programowe odpowiedniki tych rozróżnień są użyteczne. Przechowywanie płaskiej listy poprzednich wiadomości różni się od przechowywania strukturalnych zapisów epizodycznych z sygnaturami czasowymi, wynikami istotności i tagami kontekstowymi. Hipoteza zakłada, że struktura poprawia jakość wyszukiwania i umożliwia bardziej spójne długoterminowe zachowanie.

**Kierunek badań:** Zaprojektowanie i przetestowanie schematu trwałej pamięci odróżniającego zapisy epizodyczne od faktów semantycznych.

---

## Uwaga

W kognitywistyce uwaga oznacza selektywną alokację zasobów przetwarzania do istotnych bodźców. W sieciach neuronowych mechanizmy uwagi obliczają ważone wyniki istotności między elementami zapytania a pamięcią lub wejściem.

Dla BDM uwaga to mechanizm wyszukiwania w pamięci i selekcji kontekstu. Dane wejście — które zapisane wspomnienia są najbardziej istotne? Jak je ważyć i udostępniać?

**Kierunek badań:** Podejścia rozszerzone o wyszukiwanie, gdzie uwaga nad zasobem pamięci służy do konstruowania skoncentrowanego kontekstu dla dalszego rozumowania.

---

## Refleksja

Refleksja w sensie poznawczym oznacza zdolność do myślenia o własnym myśleniu — przeglądania wcześniejszego rozumowania, identyfikowania niespójności i rewizji wniosków.

W kategoriach oprogramowania refleksja to krok post-przetwarzania: po wygenerowaniu wyjścia przez system, moduł refleksji porównuje to wyjście z wcześniejszymi wyjściami lub jawnymi kryteriami spójności.

Hipoteza zakłada, że nawet prosty krok refleksji może redukować niespójności w rozumowaniu w czasie, szczególnie przy długich interakcjach lub kontekstach wielosesyjnych.

**Kierunek badań:** Zaprojektowanie i przetestowanie lekkiego modułu refleksji porównującego nowe wyjścia z zapisanymi poprzednimi i oznaczającego rozbieżności.

---

## Model siebie

Model siebie, jako używany w BDM, oznacza strukturalną reprezentację własnego stanu systemu: co wie, czego nie wie, jakie tematy eksplorował, jakie były jego ostatnie wyjścia, jakie poziomy pewności wiążą się z jego zapisanymi przekonaniami.

To nie jest twierdzenie o samoświadomości ani świadomości. Model siebie to struktura danych. To zapis wewnętrznego stanu, nie subiektywne doświadczenie tego stanu.

**Kierunek badań:** Zaprojektowanie minimalnego schematu modelu siebie i ocena, czy dostęp do niego poprawia zdolność systemu do reprezentowania niepewności.

---

## Ciągłość wewnętrznego kontekstu

Ciągłość oznacza zachowanie istotnego stanu wewnętrznego między sesjami, interakcjami lub w czasie. Bez ciągłości każda interakcja jest niezależna. Z ciągłością wcześniejsze interakcje mogą kształtować bieżące.

Biologiczna pamięć umożliwia ciągłość przez utrzymywanie reprezentacji przeszłych doświadczeń. W systemach oprogramowania ciągłość wymaga świadomego projektowania: co przechowywać, jak kodować, jak długo przechowywać i jak udostępniać.

BDM traktuje ciągłość kontekstu jako podstawowy wymóg projektowy, nie opcjonalną funkcję.

**Kierunek badań:** Zaprojektowanie warstwy ciągłości zachowującej i indeksującej historię interakcji w sposób umożliwiający wyszukiwanie, aktualizację i audyt.

---

## Uczenie się z doświadczenia

Uczenie się w zakresie BDM oznacza strukturalną aktualizację stanu wewnętrznego na podstawie nowych informacji lub informacji zwrotnych. Niekoniecznie oznacza to trenowanie modelu. Może oznaczać aktualizację przechowywanych przekonań, rewizję wyników istotności wspomnień, oznaczanie sprzeczności lub zapisywanie nowych zdarzeń epizodycznych.

Hipoteza zakłada, że lekkie, strukturalne mechanizmy uczenia się — aktualizacja struktury pamięci zamiast wag modelu — mogą być wystarczające do poprawy spójności i zdolności adaptacyjnych.

**Kierunek badań:** Zdefiniowanie znaczenia "uczenia się" dla systemu rozszerzonego o pamięć, który nie trenuje ponownie swojego modelu bazowego.

---

## Związek z AI i LLM

Duże modele językowe to najbardziej praktyczny substrat dla obecnej fazy badań BDM. Zapewniają silne możliwości rozumienia i generowania języka. Czego typowo brakuje im w bazowej formie — to trwałej pamięci, strukturalnego samomodelowania i ciągłości między sesjami.

Hipoteza BDM zakłada, że te właściwości można dodać jako warstwy zewnętrzne — zasoby pamięci, mechanizmy wyszukiwania, moduły refleksji — bez modyfikowania modelu bazowego. To podejście augmentacji, nie trenowania.

**Kierunek badań:** Ocena architektur rozszerzonych o wyszukiwanie i pamięć, zbudowanych wokół istniejących LLM, mierzenie spójności, konsekwencji i retencji kontekstu.

---

*Cała treść tego dokumentu reprezentuje hipotezy i kierunki badań. Nic tu nie stanowi ustalonych wyników naukowych.*
