# Pamięć

## Definicja

Pamięć to zdolność do kodowania, przechowywania i odtwarzania informacji. W kognitywistyce pamięć nie jest jednym systemem, lecz zbiorem funkcjonalnie odrębnych procesów i struktur o różnych cechach: czasie trwania, pojemności, mechanizmach kodowania i trybach wyszukiwania.

---

## Dlaczego ma znaczenie

Pamięć to fundament ciągłości. Bez zdolności do zachowania informacji z wcześniejszych doświadczeń system nie może się adaptować, utrzymywać spójności ani budować na wcześniejszej wiedzy. W systemach biologicznych pamięć umożliwia tożsamość, uczenie się i zachowanie zorientowane na cel w czasie. W systemach oprogramowania pamięć jest zazwyczaj albo nieobecna (obliczenia bezstanowe), albo niezróżnicowana (płaskie logi lub proste magazyny klucz-wartość).

Główna hipoteza BDM: struktura pamięci ma znaczenie, nie tylko jej obecność. Rozróżnianie zapisów epizodycznych od faktów semantycznych, indeksowanie według istotności i aktualności, zarządzanie politykami retencji — to hipoteza zakłada, że produkuje jakościowo lepsze zachowanie wyszukiwania niż płaskie przechowywanie.

---

## Możliwa reprezentacja w oprogramowaniu

Zasób pamięci BDM zawierałby prawdopodobnie:

- **Zapisy epizodyczne:** Strukturalne wpisy rejestrujące konkretne zdarzenia interakcji z polami na sygnaturę czasową, tagi tematyczne, wynik istotności i podsumowanie tego, co miało miejsce
- **Zapisy semantyczne:** Ogólna wiedza i koncepcje, przechowywane z atrybucją źródła, poziomem pewności i sygnaturą czasową ostatniej weryfikacji
- **Bufor pamięci roboczej:** Krótkotrwałe, wysokopriorytetowe okno kontekstowe zawierające najnowszy stan interakcji, opróżniane do zapisów epizodycznych na końcu sesji

Wyszukiwanie obsługiwałoby wiele trybów zapytań:
- Ważone aktualnością: zwracanie najnowszych zapisów
- Ważone istotnością: zwracanie zapisów najbardziej podobnych do bieżącego zapytania
- Filtrowane typem: zwracanie tylko epizodycznych, tylko semantycznych lub tylko zapisów pamięci roboczej

---

## Otwarte pytania

- Jaki jest minimalny schemat dla zapisu epizodycznego, który jest zarówno informatywny, jak i obliczeniowo wykonalny?
- Jak powinny być przypisywane i aktualizowane w czasie wyniki istotności?
- Jaka jest właściwa polityka retencji zapobiegająca nieograniczonemu wzrostowi bez utraty ważnych zapisów?
- Jak powinny być rozwiązywane sprzeczności między przechowywanymi zapisami?
- Czy wyszukiwanie oparte na embeddingach jest konieczne od początku, czy prostsze indeksowanie słów kluczowych wystarczy dla wstępnych prototypów?

---

## Związek z BDM

Pamięć to pierwsza warstwa architektury BDM i warunek wstępny dla wszystkich innych warstw. Uwaga wyszukuje z pamięci. Refleksja porównuje z pamięcią. Pętla uczenia się aktualizuje pamięć. Model siebie podsumowuje stan pamięci. Ciągłość kontekstu zachowuje pamięć między sesjami.

Wszystko w BDM zależy od jakości warstwy pamięci. To komponent o najwyższym priorytecie w fazie 1 developmentu.
