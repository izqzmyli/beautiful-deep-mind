# Model siebie

## Definicja

Model siebie, tak jak jest używany w BDM, to strukturalna reprezentacja danych własnego stanu systemu: jakie tematy ma przechowywane informacje, jakie poziomy pewności wiążą się z przechowywanymi przekonaniami, jakie ograniczenia zostały odnotowane i jak wygląda historia ostatnich interakcji z perspektywy systemu.

Model siebie to struktura danych. Nie jest samoświadomością. Nie jest świadomością. Nie jest subiektywnym poczuciem istnienia. To zapis — utrzymywany i odpytywalny — własnego stanu wiedzy systemu.

---

## Dlaczego ma znaczenie

Systemy pozbawione jakiejkolwiek reprezentacji własnego stanu nie mogą dokładnie rozumować o tym, co wiedzą i czego nie wiedzą. LLM w szczególności są znane z produkowania pewnie brzmiących wyjść nawet w dziedzinach, gdzie ich wiedza jest nieobecna lub słaba. Model siebie śledzący znane luki wiedzy, poziomy pewności i uznane ograniczenia mógłby dostarczać jawnych sygnałów ograniczających wyjścia w niepewnych dziedzinach, prowadząc do bardziej odpowiednio ostrożnych i dokładnych odpowiedzi.

Poza reprezentacją niepewności model siebie umożliwia pewien rodzaj spójności: system może skonsultować swój model siebie przed zaangażowaniem się w twierdzenie i zidentyfikować, czy to twierdzenie jest sprzeczne z zapisanymi wcześniejszymi stanowiskami.

---

## Możliwa reprezentacja w oprogramowaniu

Minimalny model siebie w BDM mógłby zawierać:

- **Inwentarz tematów:** lista tematów, o których system ma przechowywane zapisy, ze wskaźnikami pokrycia (wysoki, średni, niski, brak)
- **Rejestr pewności:** dla kluczowych przechowywanych przekonań, wynik pewności odzwierciedlający jak dobrze przekonanie jest poparte przechowywanym dowodem
- **Dziennik ograniczeń:** zapis jawnie uznanych luk, otrzymanych korekt i obszarów, gdzie system produkował niespójne wyjścia w przeszłości
- **Podsumowanie interakcji:** zwarte podsumowanie ostatnich wzorców interakcji — jakie tematy były omawiane, jakie korekty otrzymano, jakie otwarte pytania pozostają

Model siebie byłby wstrzykiwany do kontekstu LLM jako strukturalne podsumowanie, dając modelowi dostęp do reprezentacji własnego stanu bez konieczności każdorazowego wnioskowania tego stanu od zera.

---

## Otwarte pytania

- Jaki jest minimalny schemat czyniący model siebie użytecznym bez jego nadmiernego rozrastania?
- Jak powinny być przypisywane i aktualizowane wyniki pewności? Oparte na regułach, wspomagane LLM, czy obie?
- Jak zapobiegamy dryfowi modelu siebie — gdzie staje się niedokładny w czasie, bo aktualizacje są pominięte lub nieprawidłowe?
- Czy model siebie jest eksponowany LLM bezpośrednio (wstrzykiwany do promptu), używany jako filtr przed promptowaniem, czy obie?
- Jakie jest ryzyko nadmiernego polegania LLM na modelu siebie i odmawiania angażowania się w tematy niereprezentowane w nim?

---

## Związek z BDM

Warstwa modelu siebie zależy od warstwy pamięci (jest z niej wyprowadzona), pętli uczenia się (jest aktualizowana przez zdarzenia uczenia) i refleksji (zdarzenia refleksji zasilają dziennik ograniczeń). Zasila warstwę interfejsu, dostarczając strukturalnego kontekstu o bieżącym stanie systemu do wstrzyknięcia do promptów LLM.

Model siebie jest jednym z bardziej nowatorskich komponentów BDM — ma analogi w kognitywistyce (metapoznanie, samomonitorowanie), ale mniej wyraźny precedens w obecnym projektowaniu systemów AI jako pierwszoklasowej warstwy architektonicznej.

**Przypomnienie:** posiadanie modelu siebie nie czyni systemu samoświadomym. Model siebie to zapis stanu, nie jego doświadczenie.
