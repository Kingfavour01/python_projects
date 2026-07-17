import json
import os
from datetime import datetime


class JournalEntry:
    def __init__(self, title: str, body: str, mood: int, timestamp: str | None = None):
        self.title = title
        self.body = body
        self._mood = mood
        self.timestamp = timestamp or datetime.now().strftime("%Y-%m-%d %H:%M")

    @property
    def mood(self):
        return self._mood

    @mood.setter
    def mood(self, value: int):
        if not 1 <= value <= 5:
            raise ValueError("Mood must be between 1 and 5")
        self._mood = value

    def __str__(self):
        stars = "⭐" * self.mood
        return f"[{self.timestamp}] {self.title} {stars}\n{self.body}\n"

    def __eq__(self, other):
        if not isinstance(other, JournalEntry):
            return NotImplemented
        return self.title == other.title and self.timestamp == other.timestamp

    def to_dict(self):
        return {"title": self.title, "body": self.body, "mood": self.mood, "timestamp": self.timestamp}

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["body"], data["mood"], data["timestamp"])


class Journal:
    def __init__(self, filename: str = "journal.json"):
        self.filename = filename
        self.entries: list[JournalEntry] = []
        self.load()

    def add_entry(self, title: str, body: str, mood: int):
        entry = JournalEntry(title, body, mood)
        self.entries.append(entry)
        self.save()

    def view_entries(self, sort_by: str = "date"):
        if sort_by == "date":
            sorted_entries = sorted(self.entries, key=lambda e: e.timestamp, reverse=True)
        elif sort_by == "mood":
            sorted_entries = sorted(self.entries, key=lambda e: e.mood, reverse=True)
        elif sort_by == "title":
            sorted_entries = sorted(self.entries, key=lambda e: e.title.lower())
        else:
            sorted_entries = self.entries

        for i, entry in enumerate(sorted_entries, 1):
            print(f"{i}. {entry}")

    def search(self, keyword: str):
        results = [e for e in self.entries if keyword.lower() in e.title.lower() or keyword.lower() in e.body.lower()]
        if results:
            print(f"\n--- Found {len(results)} match(es) ---")
            for entry in results:
                print(entry)
        else:
            print(f"No entries matching '{keyword}'.")
        return results

    def summary(self):
        if not self.entries:
            print("No entries yet.")
            return
        avg_mood = sum(e.mood for e in self.entries) / len(self.entries)
        print(f"Total entries: {len(self.entries)}")
        print(f"Date range: {self.entries[0].timestamp} to {self.entries[-1].timestamp}")
        print(f"Average mood: {avg_mood:.1f} / 5.0")

    def save(self):
        with open(self.filename, "w") as f:
            json.dump([e.to_dict() for e in self.entries], f, indent=2)

    def load(self):
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
            self.entries = [JournalEntry.from_dict(item) for item in data]
        except (json.JSONDecodeError, KeyError):
            print("Journal file corrupted. Starting fresh.")
            self.entries = []


def validate_int(prompt: str, low: int, high: int) -> int:
    while True:
        try:
            value = int(input(prompt))
            if low <= value <= high:
                return value
            print(f"Enter a number between {low} and {high}.")
        except ValueError:
            print("Invalid input. Enter a number.")


def main():
    journal = Journal()
    while True:
        print("\n=== PERSONAL JOURNAL ===")
        print("1. Write new entry")
        print("2. View all entries")
        print("3. Search entries")
        print("4. Journal summary")
        print("5. Exit")
        choice = validate_int("Choice: ", 1, 5)
        if choice == 1:
            title = input("Title: ").strip()
            if not title: print("Title cannot be empty."); continue
            print("Body (type 'END' on its own line to finish):")
            lines = []
            while True:
                line = input()
                if line == "END": break
                lines.append(line)
            body = "\n".join(lines).strip()
            if not body: print("Body cannot be empty."); continue
            mood = validate_int("Mood (1-5): ", 1, 5)
            journal.add_entry(title, body, mood)
            print("Entry saved!")

        elif choice == 2:
            if not journal.entries:
                print("No entries yet.")
                continue
            print("\nSort by: 1. Date  2. Mood  3. Title")
            sort_choice = validate_int("Sort: ", 1, 3)
            sort_map = {1: "date", 2: "mood", 3: "title"}
            journal.view_entries(sort_map[sort_choice])

        elif choice == 3:
            keyword = input("Search: ").strip()
            journal.search(keyword)

        elif choice == 4:
            journal.summary()

        elif choice == 5:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
