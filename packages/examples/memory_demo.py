"""
memory_demo.py — przykład użycia LongTermStore z SQLite persistence.

Uruchom dwa razy. Przy pierwszym uruchomieniu zapiszemy zdarzenia.
Przy drugim uruchomieniu odczytamy je z pliku — bez ponownego dodawania.

    python packages/examples/memory_demo.py
"""

from pathlib import Path

from bdm.memory.event import MemoryEvent, MemoryEventType
from bdm.memory.long_term import LongTermStore

DB_PATH = Path("/tmp/bdm_demo.db")


def main() -> None:
    store = LongTermStore(path=DB_PATH)

    existing = store.query(limit=100)

    if not existing:
        print("Pierwsze uruchomienie — zapisuję zdarzenia...\n")

        store.add(MemoryEvent(
            content="Celem projektu BDM jest badanie świadomości przez budowanie modeli pamięci i refleksji.",
            event_type=MemoryEventType.FACT,
            tags=["bdm", "cel", "research"],
            salience=1.0,
        ))

        store.add(MemoryEvent(
            content="Użytkownik zapytał: czemu komputer nie może być mózgiem?",
            event_type=MemoryEventType.INTERACTION,
            tags=["bdm", "świadomość", "pytanie"],
            salience=0.9,
        ))

        store.add(MemoryEvent(
            content="Ustalono: milestone M1 dotyczy budowy warstwy pamięci z SQLite.",
            event_type=MemoryEventType.FACT,
            tags=["bdm", "m1", "decyzja"],
            salience=0.8,
        ))

        store.add(MemoryEvent(
            content="System nie posiada embodiment — brak doświadczeń zmysłowych.",
            event_type=MemoryEventType.FACT,
            tags=["świadomość", "ograniczenie", "h7"],
            salience=0.75,
        ))

        print(f"Zapisano {len(store.query(limit=100))} zdarzeń do {DB_PATH}\n")
    else:
        print(f"Drugie uruchomienie — odczytuję {len(existing)} zdarzeń z {DB_PATH}\n")

    print("─── Wszystkie zdarzenia (od najnowszego) ───")
    for e in store.query(limit=10):
        print(f"  [{e.event_type.value}] {e.content[:70]}")
        print(f"           tags={e.tags}  salience={e.salience}")
    print()

    print("─── Filtr: tylko FACT ───")
    for e in store.query(event_type=MemoryEventType.FACT, limit=10):
        print(f"  {e.content[:70]}")
    print()

    print("─── Filtr: tag 'świadomość' ───")
    for e in store.query(tags=["świadomość"], limit=10):
        print(f"  {e.content[:70]}")
    print()

    print(f"─── Łącznie w bazie: {len(store)} zdarzeń ───")
    store.close()


if __name__ == "__main__":
    main()
