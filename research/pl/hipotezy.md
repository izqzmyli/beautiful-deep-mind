# Hipotezy badawcze

Niniejszy dokument rejestruje wstępne hipotezy badawcze BDM. Każda hipoteza jest sformułowana precyzyjnie, wraz z uzasadnieniem, możliwym eksperymentem i uznanymi ograniczeniami.

Są to robocze hipotezy. Żadna z nich nie jest ustalonym wynikiem. Celem ich zapisania jest uczynienie założeń projektu jawnymi, sprawdzalnymi i otwartymi na rewizję.

---

## H1 — Trwała pamięć poprawia ciągłość interakcji

**Hipoteza:**
System z trwałą, strukturalną pamięcią wcześniejszych interakcji będzie produkował bardziej kontekstualnie spójne odpowiedzi przez wielosesyjne interakcje niż system bez trwałej pamięci.

**Uzasadnienie:**
Bez trwałej pamięci każda sesja zaczyna od stanu pustego. System nie może odwoływać się do wcześniejszych zobowiązań, korygować wcześniejszych błędów ani budować na wcześniejszych wymianach. Jeśli ciągłość kontekstu ma znaczenie dla spójnej interakcji — a jest powód, by wierzyć, że tak jest — to brak trwałej pamięci jest strukturalnym ograniczeniem.

**Możliwy eksperyment:**
Zaprojektowanie wielosesyjnego protokołu interakcji, w którym użytkownik zadaje pytania uzupełniające w wielu sesjach. Porównanie bazowego systemu (bez trwałej pamięci) z systemem rozszerzonym o pamięć. Ocena, czy system z pamięcią poprawnie odwołuje się do wcześniejszych interakcji, unika sprzeczania się z wcześniejszymi stwierdzeniami i wymaga mniej ponownych wyjaśnień od użytkownika.

**Ograniczenie:**
Spójność jest trudna do obiektywnego zmierzenia. Automatyczne metryki mogą nie wychwytywać znaczącej konsekwencji. Ocena ludzka jest bardziej wiarygodna, ale trudniejsza do skalowania. Ponadto jakość wyszukiwania pamięci wpływa na wynik: słabe wyszukiwanie nieistotnego wcześniejszego kontekstu mogłoby pogorszyć, a nie poprawić spójność.

---

## H2 — Pętle refleksji poprawiają konsekwencję rozumowania

**Hipoteza:**
System stosujący krok refleksji — przeglądający nowe wyjścia względem przechowywanych wcześniejszych wyjść przed finalizacją odpowiedzi — będzie produkował mniej wykrywalnych niespójności przez rozszerzone interakcje niż system bez refleksji.

**Uzasadnienie:**
LLM generują wyjścia bez dostępu do strukturalnego zapisu tego, co wcześniej mówiły. Krok refleksji jawnie porównujący nowe wyjścia z wcześniejszymi tworzy okazję do wykrywania i korygowania niespójności zanim trafią do użytkownika.

**Możliwy eksperyment:**
Seria interakcji zaprojektowanych do stworzenia okazji dla niespójności — pytania faktyczne zadawane w różnych formach między sesjami, pytania o stanowisko zadawane ponownie po kilku wymianach. Porównanie wyjść z i bez modułu refleksji. Pomiar wskaźnika wykrywalnych sprzeczności.

**Ograniczenie:**
Refleksja dodaje opóźnienie. Krok refleksji, który jest zbyt wolny, może być niepraktyczny. Ponadto sam moduł refleksji może produkować błędy: może oznaczać uzasadnione aktualizacje wcześniejszych stanowisk jako niespójności lub nie wykrywać subtelnych.

---

## H3 — Model siebie poprawia reprezentację niepewności

**Hipoteza:**
System z dostępem do strukturalnego modelu siebie — reprezentacji tego, co wie, czego nie wie i jakie poziomy pewności wiążą się z przechowywanymi przekonaniami — będzie produkował dokładniejsze stwierdzenia niepewności niż system bez jednego.

**Uzasadnienie:**
LLM są znane z produkowania pewnie brzmiących wyjść nawet w obszarach, gdzie ich wiedza jest ograniczona lub niepewna. Model siebie śledzący znane luki wiedzy i poziomy pewności mógłby dostarczać jawnych sygnałów ograniczających wyjścia systemu w niepewnych dziedzinach.

**Możliwy eksperyment:**
Ocena odpowiedzi na pytania w dziedzinach poza przechowaną wiedzą systemu, porównanie bazowego LLM z wersją rozszerzoną o model siebie. Pomiar wskaźnika nieodpowiedniej pewności (fałszywa pewność) i odpowiedniego zabezpieczenia (prawidłowe uznanie niepewności).

**Ograniczenie:**
Model siebie jest tylko tak dokładny, jak mechanizm aktualizacji go utrzymujący. Nieaktualny lub niedokładny model siebie mógłby produkować gorszą reprezentację niepewności niż żaden model siebie.

---

## H4 — Ciągłość kontekstu jest konieczna dla długoterminowego zachowania adaptacyjnego

**Hipoteza:**
System pozbawiony ciągłości wewnętrznego kontekstu między sesjami nie będzie wykazywał zachowania adaptacyjnego — dostosowywania odpowiedzi na podstawie skumulowanego doświadczenia — poza czasem trwania jednej sesji.

**Uzasadnienie:**
Adaptacja wymaga, by wcześniejsze doświadczenie informowało bieżące zachowanie. Bez ciągłości kontekstu nie ma mechanizmu, przez który wcześniejsze doświadczenie mogłoby wpływać na nową sesję. To twierdzenie strukturalne: ciągłość jest koniecznym (choć nie wystarczającym) warunkiem długoterminowej adaptacji.

**Możliwy eksperyment:**
Zaprojektowanie scenariusza, w którym adaptacja powinna zachodzić przez wiele sesji: użytkownik wielokrotnie dostarcza informacji zwrotnych o typie odpowiedzi. Ocena, czy system z ciągłością adaptuje swoje zachowanie między sesjami, podczas gdy bazowy bez ciągłości tego nie robi.

**Ograniczenie:**
Ta hipoteza testuje twierdzenie strukturalne, nie twierdzenie optymalizacyjne. Nawet system z ciągłością może nie adaptować się, jeśli jego pętla uczenia się jest źle zaprojektowana. Eksperyment testuje, czy ciągłość jest konieczna, ale nie mówi nam, czy jest wystarczająca.

---

## H5 — Pamięć epizodyczna poprawia rozróżnienie między faktami, zdarzeniami i wcześniejszymi interakcjami

**Hipoteza:**
System ze strukturą pamięci epizodycznej — zapisy zawierające metadane czasowe i kontekstowe — będzie lepiej odróżniał fakty ogólne, zdarzenia ograniczone czasem i historię wcześniejszych interakcji niż system przechowujący wszystkie informacje w płaskim, niezróżnicowanym logu.

**Uzasadnienie:**
Nie wszystkie przechowywane informacje są takie same. Fakt ogólny różni się od zdarzenia wcześniejszej interakcji i od twierdzenia ograniczonego czasem. Mieszanie tych bez rozróżnienia degraduje jakość wyszukiwania. Zapisy epizodyczne z odpowiednimi metadanymi pozwalają systemowi stosować różne rozumowanie do różnych typów zapisów.

**Możliwy eksperyment:**
Porównanie jakości wyszukiwania między systemem płaskiego logu a systemem pamięci epizodycznej przez typy zapytań: zapytania o wiedzę ogólną, zapytania o przypomnienie zdarzeń i zapytania o historię interakcji. Ocena, czy struktura epizodyczna poprawia precyzję dla każdego typu zapytania.

**Ograniczenie:**
Prawidłowe przypisywanie i utrzymywanie metadanych epizodycznych jest nietrywilalne. Jeśli metadane są niedokładne lub niespójne, struktura epizodyczna może nie poprawiać wyszukiwania.

---

## H6 — Obliczeniowa pamięć jest strukturalnie różna od biologicznej pamięci

**Hipoteza:**
Nawet dobrze zaprojektowany system trwałej pamięci w oprogramowaniu będzie wykazywał fundamentalne różnice od biologicznej pamięci, których nie można rozwiązać przez lepszą inżynierię — szczególnie w sposobie kodowania, zanikania, rekonstrukcji i integracji pamięci z doświadczeniem.

**Uzasadnienie:**
Biologiczna pamięć to nie przechowywanie. To rekonstrukcja. Za każdym razem gdy człowiek przywołuje zdarzenie, pamięć jest częściowo przebudowywana ze składowanych śladów, pod wpływem bieżącego kontekstu, emocji i kolejnych doświadczeń. Jest też stratna z założenia — zapominanie to nie awaria, to cecha utrzymująca istotność. Obliczeniowa pamięć, dla kontrastu, jest zazwyczaj dokładna, trwała i pozbawiona kontekstu. To nie tylko różnice implementacyjne. Mogą one odzwierciedlać coś głębszego w tym, do czego służy pamięć w świadomym systemie.

**Możliwy eksperyment:**
Zaprojektowanie serii zadań przywoływania wykorzystujących rekonstrukcyjną naturę biologicznej pamięci. Uruchomienie równoważnych zadań na systemie pamięci oprogramowania. Systematyczne dokumentowanie gdzie analogia się załamuje i dlaczego.

**Ograniczenie:**
Ta hipoteza jest częściowo filozoficzna. "Fundamentalna różnica" jest trudna do operacjonalizacji. Eksperyment prawdopodobnie przyniesie obserwacje, a nie czysty falsyfikowalny wynik. To jest akceptowalne — celem jest scharakteryzowanie przepaści, nie jej zamknięcie.

---

## H7 — System bez ucieleśnienia nie może rozwinąć ugruntowanego znaczenia

**Hipoteza:**
System oprogramowania pozbawiony ucieleśnienia — doświadczeń zmysłowych, fizycznych potrzeb, czasowego istnienia w świecie — nie może rozwijać znaczenia w sposób, w jaki robi to ludzki mózg, bez względu na to, jak zaawansowane stają się jego struktury pamięci lub rozumowania.

**Uzasadnienie:**
Znaczenie w ludzkim poznaniu jest ugruntowane w doświadczeniu: słowo "ból" znaczy coś, bo je czułeś; "głód" bo byłeś głodny; "jutro" bo żyłeś przez czas. LLM przetwarza statystyczne relacje między tokenami. Nie ma żadnego odnośnika poza językiem. To może być fundamentalne ograniczenie tego, co takie systemy mogą rozumieć, w przeciwieństwie do tego, co mogą przetwarzać.

**Możliwy eksperyment:**
Ta hipoteza jest trudna do bezpośredniego przetestowania. Pośrednie podejście: zaprojektowanie zadań wymagających ugruntowanego rozumowania — zadania, gdzie prawidłowa odpowiedź zależy od rozumienia, jak coś czuje, nie tylko jak jest opisane. Porównanie wydajności systemów z i bez rozszerzenia o pamięć. Ocena, czy dodanie pamięci cokolwiek zmienia dla tych zadań, czy ograniczenie jest strukturalne.

**Ograniczenie:**
Koncepcja "ugruntowanego znaczenia" jest kwestionowana w filozofii umysłu. Ta hipoteza może nie być falsyfikowalna w żadnym ścisłym sensie. Jest tu zapisana jako kierunek badań i urządzenie ramujące, nie jako twierdzenie, które można rozwiązać przez eksperymenty oprogramowania samodzielnie.

---

## H8 — Przepaść między obliczeniami a świadomością to nie kwestia skali ani architektury

**Hipoteza:**
Obecne systemy AI nie są nieświadome po prostu dlatego, że nie są wystarczająco duże, złożone ani architektonicznie zaawansowane. Istnieje coś kategorycznie innego w biologicznej świadomości, czego nie adresuje samo skalowanie ani doskonalenie architektury.

**Uzasadnienie:**
Powszechne niejawne założenie w badaniach AI jest takie, że świadomość pojawi się z wystarczającą złożonością lub możliwościami. BDM traktuje to jako otwartą hipotezę, nie ustalony fakt. Alternatywa — że świadomość wymaga czegoś nieobecnego w obecnych paradygmatach obliczeniowych, takiego jak ucieleśnienie, przyczynowa ciągłość czy specyficzny rodzaj fizycznego substratu — jest równie warta badania. Framework BDM jest zaprojektowany, by sondować tę granicę.

**Możliwy eksperyment:**
Po ukończeniu podstawowego frameworka (pamięć, refleksja, model siebie, ciągłość), zaprojektowanie strukturalnej oceny tego, co system rozszerzony może i czego nie może robić w porównaniu z bazowym. Specyficznie szukanie możliwości, które oczekuje się pojawić, jeśli świadomość jest kwestią architektury, i dokumentowanie tych, które się nie pojawiają. Używanie tego jako dowodu za lub przeciw hipotezie skalowania.

**Ograniczenie:**
Ta hipoteza jest bardzo szeroka i nie zostanie rozwiązana przez ten projekt samodzielnie. BDM może wnosić obserwacje i strukturalne argumenty, nie dowód. Wartość leży w rygorze badania, nie w ostateczności wniosku.

---

*Wszystkie hipotezy podlegają rewizji w miarę rozwoju projektu. Hipotezy, które zostaną sfalsyfikowane, będą odnotowane wraz z wnioskami.*
