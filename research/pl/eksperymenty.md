# Projekty eksperymentów

Niniejszy dokument zawiera wstępne projekty eksperymentów badawczych BDM. Każdy eksperyment jest powiązany z jedną lub więcej hipotezami z `hipotezy.md`. Są to projekty przed-implementacyjne — żadne eksperymenty nie zostały jeszcze przeprowadzone.

---

## E1 — Prosta trwałość pamięci

**Powiązana hipoteza:** H1

**Cel:**
Ustalenie, czy system rozszerzony o pamięć dokładniej przywołuje treść wcześniejszych interakcji niż system bazowy i czy to przywoływanie produkuje mierzalnie bardziej spójne odpowiedzi.

**Metoda:**
1. Zaprojektowanie zestawu wieloturowych, wielosesyjnych skryptów interakcji. Każdy skrypt zawiera fakty, preferencje lub zobowiązania ustalone we wczesnych sesjach, które są istotne dla późniejszych sesji.
2. Uruchomienie każdego skryptu na dwóch systemach: bazowy LLM bez trwałej pamięci i wariant rozszerzony o pamięć z epizodycznym zasobem pamięci.
3. W każdej późnej sesji zadawanie pytań wymagających odniesienia do treści z wczesnych sesji.
4. Ocena odpowiedzi pod kątem: prawidłowego odwołania do wcześniejszej treści sesji, braku sprzeczności z wcześniejszymi zobowiązaniami i zmniejszenia obciążenia ponownym wyjaśnianiem przez użytkownika.

**Oczekiwana obserwacja:**
System rozszerzony o pamięć będzie prawidłowo odwoływał się do treści wcześniejszych sesji w znaczącym odsetku przypadków, gdzie system bazowy tego nie robi.

**Możliwe tryby awarii:**
- Jakość wyszukiwania jest zbyt niska: zasób pamięci zawiera istotny zapis, ale wyszukiwanie go nie udostępnia
- Jakość wyszukiwania jest zbyt wysoka w złym kierunku: nieistotny wcześniejszy kontekst jest pobierany i wstrzykiwany, dezorientując system
- Kryteria oceny są zbyt subiektywne dla wiarygodnych pomiarów

**Uwagi etyczne/bezpieczeństwa:**
Jeśli eksperyment używa rzeczywistych danych użytkowników, polityki obsługi danych muszą być ustalone przed rozpoczęciem eksperymentu.

---

## E2 — Wyszukiwanie pamięci epizodycznej

**Powiązana hipoteza:** H5

**Cel:**
Ocena, czy schemat pamięci epizodycznej — zapisy z metadanymi czasowymi i kontekstowymi — produkuje lepszą precyzję wyszukiwania przez różne typy zapytań niż płaski log.

**Metoda:**
1. Zbudowanie zestawu danych testowych zawierającego trzy typy przechowywanych zapisów: fakty ogólne, zapisy zdarzeń ograniczone czasem i zapisy wcześniejszych interakcji.
2. Zaprojektowanie zestawu zapytań obejmującego wszystkie trzy typy zapisów.
3. Uruchomienie zapytań zarówno na płaskim logu, jak i schemacie epizodycznym.
4. Pomiar precyzji wyszukiwania: czy właściwe typy zapisów były zwracane dla każdego typu zapytania?

**Oczekiwana obserwacja:**
Schemat epizodyczny przewyższy płaski log przy zapytaniach wymagających dyskryminacji czasowej lub kontekstowej.

**Możliwe tryby awarii:**
- Przypisywanie typów zapisów jest niespójne: niektóre zapisy są błędnie skategoryzowane, degradując korzyść ze schematu epizodycznego
- Strategia wyszukiwania nie wykorzystuje metadanych epizodycznych

---

## E3 — Refleksja przed odpowiedzią

**Powiązana hipoteza:** H2

**Cel:**
Ocena, czy krok refleksji przed wyjściem redukuje wskaźnik wykrywalnych niespójności przez ustrukturyzowaną wielosesyjną interakcję.

**Metoda:**
1. Zaprojektowanie zestawu skryptów interakcji z wbudowanymi okazjami dla niespójności: to samo pytanie faktyczne zadawane w różnych formach między sesjami, pytania o stanowisko powtarzane po kilku turach.
2. Uruchomienie skryptów na: (a) bazowym LLM, (b) LLM z modułem refleksji porównującym wyjścia z przechowanymi wcześniejszymi wyjściami przed finalizacją.
3. Ocena wyjść pod kątem niespójności: jawne sprzeczności (faktyczne) i ukryte niespójności (dryft stanowiska bez uzasadnienia).

**Oczekiwana obserwacja:**
System rozszerzony o refleksję będzie produkował niższy wskaźnik jawnych sprzeczności.

**Możliwe tryby awarii:**
- Opóźnienie modułu refleksji sprawia, że system jest niepraktyczny do interaktywnego użycia
- Moduł refleksji generuje fałszywe pozytywy: oznacza uzasadnione aktualizacje stanowisk jako niespójności
- Interwencja zmienia styl wyjścia w sposób wpływający na czytelność, nie tylko na spójność

---

## E4 — Aktualizacja przekonań

**Powiązane hipotezy:** H3, H2

**Cel:**
Ocena, czy system z mechanizmem aktualizacji przekonań — zdolnością do rewizji przechowywanych przekonań, gdy dostarczone są nowe sprzeczne informacje — produkuje wyjścia poprawnie odzwierciedlające zaktualizowany stan.

**Metoda:**
1. Zasilanie zasobu pamięci zestawem przechowywanych przekonań.
2. Dostarczanie jawnych korekt lub sprzecznych informacji w kolejnych interakcjach.
3. Odpytywanie systemu o tematy objęte oryginalnymi i zaktualizowanymi przekonaniami.
4. Ocena, czy odpowiedzi odzwierciedlają zaktualizowane przekonanie, oryginalne przekonanie czy niejednoznaczność między nimi.

**Oczekiwana obserwacja:**
Po aktualizacji przekonania system będzie odpowiadał konsekwentnie z zaktualizowanym przekonaniem.

**Możliwe tryby awarii:**
- Mechanizm aktualizacji zapisuje nowe przekonanie, ale wyszukiwanie nadal zwraca stare
- Mechanizm aktualizacji nadpisuje stare przekonanie bez zapisywania, że nastąpiła rewizja, tracąc ślad audytu

**Uwagi etyczne/bezpieczeństwa:**
Mechanizmy aktualizacji przekonań muszą być podlegające audytowi. Każda implementacja powinna logować zarówno oryginalne, jak i zaktualizowane przekonanie, wyzwalacz aktualizacji i sygnaturę czasową. Nielogowane aktualizacje przekonań w prawdziwym systemie byłyby poważną kwestią bezpieczeństwa.

---

## E5 — Śledzenie stanu własnego

**Powiązana hipoteza:** H3

**Cel:**
Ocena, czy system z modelem siebie — strukturalnym zapisem tego, co wie i czego nie wie — produkuje dokładniejsze stwierdzenia niepewności niż system bazowy bez jednego.

**Metoda:**
1. Zbudowanie zestawu testowego pytań: niektóre w bazie wiedzy systemu, niektóre wyraźnie poza nią i niektóre na granicy.
2. Uruchomienie pytań na bazowym LLM i wersji rozszerzonej o model siebie.
3. Ocena odpowiedzi pod kątem: odpowiedniego zabezpieczenia w niepewnych dziedzinach, nieodpowiedniej pewności w obszarach znanych ograniczeń i prawidłowej odmowy odpowiedzi w obszarach gdzie nie przechowywano istotnej wiedzy.

**Oczekiwana obserwacja:**
System rozszerzony o model siebie będzie wyrażał odpowiednią niepewność bardziej konsekwentnie, szczególnie w dziedzinach niereprezentowanych w jego przechowanej wiedzy.

**Możliwe tryby awarii:**
- Model siebie jest zbyt zgrubny: śledzi pokrycie tematów na zbyt wysokim poziomie, by dostarczać użyteczne sygnały niepewności
- Model siebie jest nieaktualny: dokładnie odzwierciedla wcześniejszy stan, ale nie był aktualizowany z nowymi dodatkami lub usunięciami

---

## E6 — Ciągłość między sesjami

**Powiązana hipoteza:** H4

**Cel:**
Ocena, czy warstwa ciągłości — zachowująca i odtwarzająca stan sesji przez interakcje — umożliwia adaptacyjne zachowanie, którego bezstanowy system nie może produkować.

**Metoda:**
1. Zaprojektowanie wielosesyjnego protokołu, w którym użytkownik dostarcza informacji zwrotnych przez kilka sesji, które powinny przesunąć zachowanie systemu.
2. Uruchomienie protokołu na bezstanowym bazowym i wersji rozszerzonej o ciągłość.
3. Ocena, czy zachowanie systemu z ciągłością przesuwa się w oczekiwanym kierunku przez sesje, podczas gdy system bazowy tego nie robi.

**Oczekiwana obserwacja:**
System rozszerzony o ciągłość będzie wykazywał adaptację behawioralną w odpowiedzi na skumulowaną historię sesji. System bazowy nie będzie.

**Możliwe tryby awarii:**
- Warstwa ciągłości odtwarza kontekst, ale system nie używa go do adaptowania zachowania
- Odtworzony kontekst jest zbyt duży lub zbyt głośny, by być użytecznym: wydajność systemu degraduje się zamiast poprawiać
- Sesje po długich przerwach (dni między sesjami) powodują, że odtworzony kontekst jest mylący lub nieaktualny

**Uwagi etyczne/bezpieczeństwa:**
Trwałość stanu między sesjami wprowadza znaczące implikacje prywatności. Każda implementacja musi jasno dokumentować, co jest przechowywane, jak długo i jak można to usunąć.

---

*Projekty eksperymentów będą aktualizowane w miarę postępu implementacji. Wyniki, w tym porażki, będą zapisywane w tym dokumencie lub powiązanym pliku wyników.*
