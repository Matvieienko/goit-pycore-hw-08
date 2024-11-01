from collections import UserDict
from datetime import datetime, timedelta

# Базовий клас для зберігання значення поля
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# Клас для зберігання імені
class Name(Field):
    pass

# Клас для зберігання номеру телефону з валідацією
class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)

# Клас для зберігання дня народження з перевіркою формату
class Birthday(Field):
    def __init__(self, value):
        try:
            self.date = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(value)

# Клас для зберігання інформації про контакт
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = list(filter(lambda ph: ph.value != phone, self.phones))

    def edit_phone(self, old_phone, new_phone):
        self.phones = list(map(lambda ph: Phone(new_phone) if ph.value == old_phone else ph, self.phones))

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def get_birthday(self):
        return self.birthday.value if self.birthday else "Birthday not set."

    def days_to_birthday(self):
        if self.birthday:
            today = datetime.today()
            birthday_this_year = self.birthday.date.replace(year=today.year)
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            return (birthday_this_year - today).days
        return None

    def __str__(self):
        phones = '; '.join(p.value for p in self.phones)
        birthday = self.get_birthday()
        return f"Contact name: {self.name.value}, phones: {phones}, birthday: {birthday}"

# Клас для управління книгою контактів
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        today = datetime.today()
        next_week = today + timedelta(days=7)
        return [
            record for record in self.data.values()
            if record.birthday and today <= record.birthday.date.replace(year=today.year) <= next_week
        ]