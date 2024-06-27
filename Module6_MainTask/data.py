class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    ...


class Phone(Field):
    @staticmethod
    def validate_phone(phone):
        return phone.isdigit() and len(phone) == 10
    
    def __init__(self, value):
        if not self.validate_phone(value):
            raise ValueError("Телефон повинен містити 10 цифр!")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str) -> None:
            self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        for ph in self.phones:
            if ph.value == phone:
                self.phones.remove(ph)
                return
        raise ValueError("Номер не знайдено.")

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        for ph in self.phones:
            if ph.value == old_phone:
                self.phones.remove(ph)
                self.phones.append(Phone(new_phone))
                return
        raise ValueError("Номер, який ви хочете змінити, не знайдено.")

    def find_phone(self, phone: str):
        for ph in self.phones:
            if ph.value == phone:
                return ph
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"