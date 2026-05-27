# Uwaga

## Definicja

Uwaga to mechanizm, przez który system wybiera, które informacje są najbardziej istotne dla bieżącego zadania i alokuje odpowiednio zasoby przetwarzania. W kognitywistyce uwaga to selektywne filtrowanie bodźców z większej puli dostępnych wejść. W uczeniu maszynowym mechanizmy uwagi obliczają ważoną istotność między zapytaniem a zestawem elementów kandydujących, produkując skoncentrowany wybór istotnej treści.

---

## Dlaczego ma znaczenie

Pamięć bez uwagi jest prawie bezużyteczna. System może przechowywać dużą liczbę zapisów, ale jeśli nie może wybrać właściwych zapisów we właściwym czasie, przechowywanie nie przynosi żadnej korzyści. Uwaga to strategia wyszukiwania — mechanizm łączący to, co jest przechowywane z tym, co jest aktualnie potrzebne.

W systemach opartych na LLM uwaga działa wewnątrz okna kontekstowego na tokenach wejściowych. Warstwa uwagi BDM działa na innym poziomie: nad trwałym zasobem pamięci, wybierając które przechowywane zapisy powinny być udostępnione i wstrzyknięte do bieżącego kontekstu interakcji.

---

## Możliwa reprezentacja w oprogramowaniu

W BDM warstwa uwagi działałaby jako procesor zapytań nad zasobem pamięci:

1. Odbieranie bieżącego wejścia lub zadania jako zapytania
2. Obliczanie wyników istotności dla przechowywanych zapisów pamięci względem zapytania
3. Rankingowanie i filtrowanie zapisów według istotności, aktualności lub innych konfigurowalnych kryteriów
4. Zwracanie ograniczonego zestawu wysokoisotnych zapisów do wstrzyknięcia do kontekstu downstream
5. Logowanie decyzji wyszukiwania dla możliwości audytu

Obliczanie istotności mogłoby używać:
- **Nakładania słów kluczowych:** proste dopasowanie terminów między zapytaniem a treścią zapisu
- **Podobieństwa embeddingowego:** kosinusowe podobieństwo między embeddingami zapytania i zapisu
- **Ważenia aktualnością:** nowsze zapisy otrzymują wzmocnienie istotności
- **Oceniania istotnością:** zapisy oznaczone jako wysokoisotne przez pętlę uczenia są priorytetowane

---

## Otwarte pytania

- Czy warstwa uwagi powinna używać jednej strategii wyszukiwania czy dynamicznie wybierać między strategiami na podstawie typu zapytania?
- Jak oceniamy jakość wyszukiwania bez etykiet istotności ground truth?
- Jaki jest właściwy górny limit pobranego kontekstu do wstrzyknięcia — zbyt dużo dodaje szum, zbyt mało traci ważny kontekst?
- Czy uwaga powinna dalej filtrować pobrane zapisy (np. streszczać lub kompresować) przed wstrzyknięciem?
- Jak powinny być obsługiwane sprzeczne pobrane zapisy — wstrzykiwane razem, oznaczane czy filtrowane?

---

## Związek z BDM

Uwaga siedzi między warstwą pamięci a wszystkimi wyższymi warstwami. Jest odpowiedzialna za zapewnienie, że właściwe przechowywane informacje trafiają do właściwej części pipeline'u we właściwym czasie. Bez efektywnej uwagi pamięć staje się obciążeniem, a nie zasobem: duże, wolne i głośne.

Dobry projekt warstwy uwagi jest prawdopodobnie jedną z najważniejszych decyzji inżynierskich w architekturze BDM.
