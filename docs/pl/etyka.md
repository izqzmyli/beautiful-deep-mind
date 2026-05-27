# Etyka i odpowiedzialne badania

Niniejszy dokument opisuje zasady etyczne i ograniczenia kierujące BDM jako projektem badawczym. To nie są deklaracje aspiracyjne — to wiążące wytyczne kształtujące to, co projekt twierdzi, jak się komunikuje, co buduje i czego odmawia robienia.

---

## Brak twierdzeń medycznych

BDM nie jest produktem medycznym, narzędziem badań medycznych, instrumentem klinicznym ani zastosowaniem terapeutycznym.

BDM nie twierdzi, że:
- diagnozuje, leczy, zapobiega ani leczy jakiemukolwiek schorzeniu
- poprawia funkcje poznawcze w jakimkolwiek mierzalnym klinicznie sensie
- wspiera podejmowanie decyzji w ochronie zdrowia, psychologii lub neurologii
- jest bezpieczny lub odpowiedni do zastosowań klinicznych lub terapeutycznych

Każda osoba szukająca wsparcia w zakresie zdrowia poznawczego, oceny neurologicznej lub pomocy psychologicznej powinna skonsultować się z wykwalifikowanym specjalistą medycznym lub klinicznym.

---

## Brak twierdzeń o świadomości

BDM nie twierdzi, że:
- tworzy świadomość w systemie oprogramowania
- symuluje świadomość ani przybliża subiektywnego doświadczenia
- udowadnia, że system jest lub nie jest świadomy
- produkuje systemy, które "czują", "doświadczają" lub mają stany wewnętrzne w jakimkolwiek znaczącym sensie

Użycie terminów takich jak "umysł", "głęboki umysł", "model siebie" i "refleksja" w tym projekcie jest metaforyczne i funkcjonalne. Terminy te opisują wzorce projektowe oprogramowania, nie właściwości świadomości, wrażliwości ani subiektywnego doświadczenia.

Projekt bada pytanie o świadomość. Nie twierdzi, że na nie odpowiada. To zasadnicza różnica.

---

## Brak twierdzeń o przesyłaniu umysłu

BDM nie twierdzi, że:
- kopiuje ludzki umysł do oprogramowania
- przesyła, przenosi, zachowuje ani rozszerza ludzką świadomość
- zapewnia jakąkolwiek ścieżkę do cyfrowej nieśmiertelności czy ciągłości umysłu
- replikuje strukturę lub funkcję ludzkiego mózgu

BDM to badania oprogramowania. Czerpie konceptualną inspirację z kognitywistyki, ale nie operuje na danych biologicznych i nie modeluje rzeczywistych procesów mózgowych. Różnica między "zainspirowanym koncepcjami kognitywnymi" a "replikującym mózg" jest kategoryczna — BDM jest zdecydowanie w pierwszej kategorii.

---

## Odpowiedzialny język

BDM zobowiązuje się do używania starannego, precyzyjnego języka we wszelkiej dokumentacji, komentarzach do kodu, publikacjach i komunikacji.

Oznacza to:
- Formułowanie wszystkich niezweryfikowanych idei jako hipotez, nie faktów
- Wyraźne rozróżnianie między modelem, symulacją a rzeczywistym poznaniem
- Nieużywanie języka sugerującego świadomość lub doświadczenie w systemie oprogramowania
- Nieużywanie języka generującego ekscytację kosztem dokładności
- Explicite i wyraźne uznawanie ograniczeń
- Aktualizowanie lub wycofywanie twierdzeń, gdy dowody ich nie wspierają

Język do unikania: "system myśli", "system czuje", "system jest świadomy", "cyfrowa świadomość", "mózg w oprogramowaniu", "kopia umysłu", "cyfryczna dusza".

Język preferowany: "system przechowuje", "system wyszukuje", "system modeluje", "system reprezentuje", "strukturalne przybliżenie", "warstwa konceptualna", "hipoteza badawcza".

---

## Kwestie prywatności

Warstwy pamięci i ciągłości BDM będą przechowywać zapisy interakcji, w tym potencjalnie wrażliwe treści. Projekt traktuje to poważnie:

- Zasoby pamięci nie powinny gromadzić ani przechowywać danych osobowych bez wyraźnej zgody
- Przechowywane zapisy interakcji powinny być chronione przed nieautoryzowanym dostępem
- Użytkownicy powinni mieć możliwość przeglądania, eksportowania i usuwania przechowywanych zapisów
- Każdy eksperyment z danymi użytkowników musi działać w ramach jasnej polityki obsługi danych
- BDM nie będzie udostępniał przechowywanych danych interakcji stronom trzecim bez wyraźnej zgody

W miarę przejścia projektu z fazy konceptualnej do prototypu, konkretne protokoły obsługi danych będą dokumentowane i publikowane.

---

## Kwestie bezpieczeństwa

BDM to projekt badawczy we wczesnej fazie. Kwestie bezpieczeństwa obejmują:

- **Dryft behawioralny:** Pętla uczenia się aktualizująca przechowywane przekonania bez odpowiednich zabezpieczeń mogłaby wzmacniać nieprawidłowe lub szkodliwe przekonania w czasie. Wszystkie mechanizmy uczenia muszą zawierać logowanie, możliwość audytu i możliwość cofnięcia.
- **Nadmierne poleganie:** Użytkownicy nie powinni być zachęcani do polegania na wynikach BDM przy podejmowaniu ważkich decyzji, szczególnie w dziedzinach takich jak zdrowie, prawo czy finanse.
- **Błędy refleksji:** Moduł refleksji, który nieprawidłowo oznacza spójne wyjścia jako niespójne lub nie wykrywa prawdziwych niespójności, może degradować jakość wyjścia w nieoczywisty sposób.
- **Ograniczenia modelu:** Poleganie BDM na LLM jako substracie oznacza, że dziedziczy wszystkie znane ograniczenia tych modeli, w tym halucynacje, uprzedzenia i ograniczenia okna kontekstowego.

---

## Badania skoncentrowane na człowieku

BDM jest projektowany dla ludzi i przez ludzi, z myślą o potrzebach ludzkich i ludzkiej kontroli.

Oznacza to:
- Projekt nie dąży do autonomii kosztem przejrzystości
- Użytkownicy powinni rozumieć, co system przechowuje, wyszukuje i nad czym rozumuje
- Żaden komponent BDM nie powinien działać w sposób celowo nieprzejrzysty dla użytkowników i deweloperów
- Celem jest budowanie użytecznego, uczciwego, podlegającego audytowi oprogramowania — nie maksymalizowanie możliwości bez względu na konsekwencje

---

## Przejrzystość i ograniczenia

BDM zobowiązuje się do przejrzystości w kwestii tego, czym jest i czym nie jest:

- Wszystkie opublikowane wyniki będą zawierać jasne stwierdzenie ograniczeń
- Negatywne wyniki będą publikowane obok pozytywnych
- Projekt nie będzie selekcjonować wyników, by przedstawić bardziej korzystny obraz
- Opisy architektoniczne będą wyraźnie rozróżniać między zaimplementowanymi komponentami a konceptualnymi
- Historia wersji i dzienniki zmian będą utrzymywane otwarcie

---

## Unikanie zwodniczego antropomorfizmu

Antropomorfizm — przypisywanie ludzkich cech nieludzkim systemom — to znane ryzyko w badaniach i komunikacji AI. BDM zwraca uwagę na unikanie zwodniczego antropomorfizmu:

- Warstwy oprogramowania nie będą opisywane tak, jakby miały doświadczenia, intencje ani uczucia
- Interfejsy użytkownika nie będą projektowane tak, by tworzyć fałszywe wrażenie wrażliwości lub emocjonalnej reaktywności
- Dokumentacja nie będzie używać języka zachęcającego użytkowników do tworzenia nieodpowiednich więzi lub poziomów zaufania do systemu

Metafory funkcjonalne (np. "system reflektuje nad swoim wcześniejszym wyjściem") są akceptowalne, gdy są wyraźnie ujęte jako opisy procesów obliczeniowych, nie jako twierdzenia o wewnętrznych doświadczeniach.

---

## Symulacja, modelowanie i rzeczywiste poznanie

Te trzy koncepcje są kategorycznie różne i BDM będzie utrzymywał to rozróżnienie przez cały czas:

- **Symulacja** — proces oprogramowania naśladujący pewne obserwowalne zachowania systemu, niekoniecznie implementujący te same mechanizmy
- **Modelowanie** — strukturalna reprezentacja wybranych właściwości systemu, wyabstrahowana z pełnej złożoności
- **Rzeczywiste poznanie** — procesy zachodzące w biologicznych mózgach, obejmujące mechanizmy, które nie są jeszcze w pełni rozumiane

BDM buduje modele. Może produkować symulacje pewnych zachowań poznawczych. Nie replikuje, nie uzyskuje dostępu ani nie odtwarza rzeczywistego poznania.

---

*Ten dokument będzie aktualizowany w miarę rozwoju projektu. Etyka nie jest jednorazową deklaracją — wymaga ciągłej uwagi, rewizji i odpowiedzialności.*
