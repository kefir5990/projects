import json

def print_with_indent(value, indent = 0):
    indentation = " " * indent
    print(f"{indentation}{str(value)}")

class Entry:
    def __init__(self, title, entries = None, parent = None):
        if entries is None:
            entries = []
        self.title = title
        self.entries = entries
        self.parent = parent

    def __str__(self):
        return self.title
    
    def print_entries(self, indent = 0):
        print_with_indent(self, indent)
        for entry in self.entries:
            entry.print_entries(indent + 1)
    
    def json(self):
        res = {
            "title": self.title,
            "entries": [x.json() for x in self.entries]
        }
        return res
    
    @classmethod
    def entry_from_json(cls,value: dict):
        new_entry = cls(value["title"])
        for item in value.get("entries", []):
            new_entry.add_entry(cls.entry_from_json(item))
        return new_entry

    def add_entry(self, entry):
        self.entries.append(entry)
        entry.parent = self


if __name__ == "__main__":
    entry = Entry("Products")
    meat = Entry("Meat")
    kolbasa = Entry("Kolbasa")
    chicken = Entry("Chicken")
    beef = Entry("Beef")


    entry.add_entry(meat)
    meat.add_entry(kolbasa)
    meat.add_entry(chicken)
    meat.add_entry(beef)

    new_entry = Entry.entry_from_json(entry.json())
    new_entry.print_entries()


                      

