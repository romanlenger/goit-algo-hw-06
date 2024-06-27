from collections import UserDict
from data import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name, "record not found.")
    
    def delete(self, name: str):
        if name in self.data:
            del self.data[name]
        else:
            return "record not found."
    
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())