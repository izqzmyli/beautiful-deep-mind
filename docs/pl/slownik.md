# Słownik pojęć

Słownik definiuje terminy używane w dokumentacji BDM. Definicje są napisane tak, by być precyzyjne, ale dostępne. Tam, gdzie termin ma różne znaczenia w różnych dyscyplinach, definicja odzwierciedla użycie specyficzne dla BDM.

---

## Uwaga

W kognitywistyce uwaga to selektywna alokacja zasobów poznawczych do określonych bodźców przy jednoczesnym odfiltrowywaniu innych. W uczeniu maszynowym mechanizmy uwagi obliczają ważone wyniki istotności między elementami zapytania a pamięcią lub wejściem. W BDM uwaga odnosi się do procesu wyboru, które przechowywane wspomnienia lub elementy kontekstowe powinny być udostępnione w odpowiedzi na dane wejście.

---

## BCI (Interfejs mózg-komputer)

Technologia ustanawiająca bezpośredni kanał komunikacji między mózgiem a zewnętrznym urządzeniem — zazwyczaj odczytująca sygnały neuronalne (BCI wejściowe), dostarczająca stymulację do mózgu (BCI wyjściowe) lub obie (BCI dwukierunkowe). BDM nie jest projektem BCI. Termin pojawia się w liście lektur i dokumencie etycznym dla kontekstu, nie jako część zakresu BDM.

---

## Architektura poznawcza

Framework definiujący bazowe stałe struktury i procesy kognitywnego lub inteligentnego systemu. Przykłady w kognitywistyce to ACT-R i SOAR. Architektura poznawcza definiuje, jakie typy pamięci istnieją, jak wzajemnie oddziałują, jak działa uwaga i jak przebiega uczenie się. BDM używa tej koncepcji do ramowania własnego warstwowego projektu — nie do replikowania żadnej istniejącej architektury poznawczej, lecz do przyjęcia podejścia definiowania warstw funkcjonalnych z jasnymi odpowiedzialnościami.

---

## Konektom

Kompleksowa mapa połączeń neuronowych w mózgu lub jego części. Ludzki konektom to aktywny obszar badań neuronauki. BDM nie pracuje z konektomami i nie próbuje symulować ani replikować połączeń neuronalnych. Termin pojawia się tu dla kontekstu i rozróżnienia.

---

## Świadomość

Świadomość to subiektywne doświadczenie bycia świadomym — jakościowa właściwość doświadczenia. Jest jednym z najbardziej dyskutowanych i najmniej rozumianych tematów w filozofii, neuronauce i kognitywistyce. BDM nie twierdzi, że tworzy, symuluje ani wyjaśnia świadomość. Termin pojawia się w dokumentach etyki i słowniku, by explicite zdefiniować, czego BDM nie realizuje.

---

## Ciągłość

W BDM ciągłość oznacza zachowanie istotnego stanu wewnętrznego między sesjami, interakcjami lub w czasie. System ma ciągłość, jeśli informacje z wcześniejszych interakcji wpływają na bieżące zachowanie w sposób strukturalny, możliwy do wyszukania i audytowania. Biologiczna pamięć wspiera ciągłość przez utrzymywanie reprezentacji przeszłych doświadczeń. Warstwa ciągłości BDM to decyzja projektowa oprogramowania, nie twierdzenie filozoficzne o tożsamości czy jaźni.

---

## Pamięć epizodyczna

Typ pamięci przechowujący zapisy konkretnych zdarzeń w kontekście — co się wydarzyło, kiedy i w jakich okolicznościach. Pamięć epizodyczna różni się od semantycznej (ogólna wiedza i koncepcje) tym, że zawiera metadane czasowe i kontekstowe. W BDM struktury pamięci epizodycznej mają poprawić trafność wyszukiwania, pozwalając systemowi odróżniać typy wcześniejszych interakcji.

---

## Wewnętrzny kontekst

Skumulowany stan wewnętrzny, który system utrzymuje w trakcie interakcji lub sesji: co zostało powiedziane, nad czym rozumowano, jakie zobowiązania zostały podjęte i jakie niepewności odnotowano. Większość obecnych systemów AI utrzymuje wewnętrzny kontekst tylko w obrębie jednego okna kontekstowego. BDM traktuje trwały wewnętrzny kontekst jako podstawowy wymóg projektowy.

---

## Pętla uczenia się

Proces, przez który system aktualizuje swój stan wewnętrzny na podstawie nowych informacji, informacji zwrotnych lub wyników. W BDM pętle uczenia się nie odnoszą się do gradientu ani trenowania modelu. Odnoszą się do strukturalnych mechanizmów aktualizacji przechowywanych przekonań, rewizji wyników istotności, oznaczania sprzeczności lub zapisywania nowych zdarzeń epizodycznych. Pętla uczenia się to wzorzec projektowy, nie twierdzenie o autonomicznej zdolności uczenia się.

---

## LLM (Duży model językowy)

Model sieci neuronowej trenowany na dużych korpusach tekstów, zdolny do generowania, streszczania, klasyfikowania i rozumowania o tekście. Przykłady to GPT-4, Claude i Llama. LLM to główny substrat badawczy BDM. BDM nie trenuje LLM; bada architektury rozszerzające LLM o warstwy pamięci, refleksji i ciągłości.

---

## Pamięć długoterminowa

Pamięć trwająca przez długi czas, potencjalnie w nieskończoność. W kognitywistyce pamięć długoterminowa obejmuje pamięć epizodyczną, semantyczną i proceduralną. W BDM pamięć długoterminowa oznacza przechowywane zapisy trwające między sesjami i indeksowane do wyszukiwania w czasie.

---

## Pamięć

Zdolność do kodowania, przechowywania i odtwarzania informacji. W BDM pamięć jest pierwszoplanową troską architektoniczną. Pamięć to nie płaski log. To strukturalny zasób z odrębnymi typami zapisów, strategiami indeksowania i mechanizmami wyszukiwania. Jakość i struktura pamięci jest hipotezowana jako kluczowy wyznacznik spójności systemu w czasie.

---

## Neuroplastyczność

Zdolność mózgu do reorganizowania się przez tworzenie nowych połączeń neuronalnych przez całe życie. Neuroplastyczność leży u podstaw uczenia się, formowania pamięci i regeneracji po uszkodzeniu. BDM czerpie konceptualną inspirację z idei, że stan wewnętrzny systemu może być modyfikowany przez doświadczenie, ale nie modeluje neuroplastyczności na poziomie biologicznym.

---

## Refleksja

W BDM refleksja to strukturalny proces, przez który system przegląda własne wcześniejsze wyjścia, sprawdza spójność i stosuje korekty lub rewizje w razie potrzeby. Refleksja jest implementowana jako moduł oprogramowania, nie jako filozoficzna introspekcja. Hipoteza zakłada, że nawet prosty krok refleksji może poprawić spójność w długich interakcjach.

---

## Model siebie

Reprezentacja, którą system utrzymuje swojego własnego stanu: co wie, czego nie wie, jakie tematy eksplorował, jakie były jego ostatnie wyjścia i jaka pewność wiąże się z jego przechowywanymi przekonaniami. Model siebie to struktura danych. To nie twierdzenie o samoświadomości, subiektywnym doświadczeniu ani świadomości. W BDM warstwa modelu siebie jest hipotezowana jako poprawiająca zdolność systemu do dokładnego reprezentowania niepewności i uznawania wcześniejszych zobowiązań.

---

## Pamięć krótkoterminowa

Pamięć przechowująca ograniczoną ilość informacji przez krótki czas, zazwyczaj od sekund do minut. W kognitywistyce pamięć robocza to ściśle związana koncepcja obejmująca aktywną manipulację informacjami. W BDM pamięć krótkoterminowa odpowiada mniej więcej aktywnemu oknu kontekstowemu LLM w trakcie sesji.

---

*Terminy będą dodawane w miarę rozwoju projektu. Definicje odzwierciedlają użycie w BDM i mogą różnić się od użycia w innych kontekstach.*
