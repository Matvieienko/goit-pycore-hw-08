from colorama import Fore
from decorators import input_error
from address_book import Record, Phone

@input_error
def add_contact(args, book):
    if len(args) < 2:
        return Fore.RED + "⚠️  Give me name and phone, please."
    
    name, phone, *_ = args
    validated_phone = Phone(phone)  # Валідація телефону
    record = book.find(name)

    if record is None:
        record = Record(name)
        record.add_phone(validated_phone.value)
        book.add_record(record)
        message = Fore.GREEN + f"✅ Contact '{name}' added."
    else:
        record.add_phone(validated_phone.value)
        message = Fore.GREEN + f"✅ Contact '{name}' updated."
    
    return message

@input_error
def change_contact(args, book):
    if len(args) != 3:
        return Fore.RED + "⚠️  Give me name, old phone, and new phone, please."
    
    name, old_phone, new_phone = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return Fore.GREEN + f"🔄 Contact '{name}' updated."
    else:
        raise KeyError

@input_error
def show_phone(args, book):
    if not args:
        return Fore.RED + "⚠️  Enter the argument for the command."
    name = args[0]
    record = book.find(name)
    if record:
        phones = ", ".join(p.value for p in record.phones)
        return Fore.GREEN + f"👨 {name}  ☎️  {phones}"
    else:
        raise KeyError

def show_all(book):
    if book.data:
        return Fore.GREEN + "\n".join(str(record) for record in book.data.values())
    else:
        return Fore.RED + "🔍 No contacts available."

@input_error
def add_birthday(args, book):
    if len(args) != 2:
        return Fore.RED + "⚠️  Give me the name and birthday in the format DD.MM.YYYY, please."
    
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return Fore.GREEN + f"🎉 Birthday added for {name}."
    else:
        raise KeyError

@input_error
def show_birthday(args, book):
    if not args:
        return Fore.RED + "⚠️  Give me the name of the contact to show the birthday."
    name = args[0]
    record = book.find(name)
    if record:
        return Fore.GREEN + f"🎂 {name}'s birthday is {record.get_birthday()}"
    else:
        raise KeyError

@input_error
def birthdays(args, book):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return Fore.RED + "🔍 No upcoming birthdays in the next week."
    return Fore.GREEN + "\n".join(f"🎂 {record}" for record in upcoming)