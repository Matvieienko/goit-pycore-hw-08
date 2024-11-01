from colorama import Fore, init
from commands import add_contact, change_contact, show_phone, show_all, add_birthday, show_birthday, birthdays
from address_book import AddressBook
import sys
import pickle  # Імпортуємо pickle для серіалізації

sys.stdout.reconfigure(encoding='utf-8')

init(autoreset=True)

# Функція для збереження адресної книги
def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

# Функція для завантаження адресної книги
def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Якщо файл не знайдено, повертаємо нову AddressBook

def parse_input(user_input):
    cmd, *args = user_input.split()
    return cmd.lower(), args

def main():
    book = load_data()  # Завантажуємо адресну книгу при запуску
    print(Fore.BLUE + "Welcome to the assistant bot! 🤖")

    while True:
        user_input = input(Fore.BLUE + "Enter a command: ").strip()
        
        # Якщо введено порожній рядок, пропускаємо ітерацію
        if not user_input:
            continue
        
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(Fore.BLUE + "Good bye! 👋")
            save_data(book)  # Зберігаємо адресну книгу перед виходом
            break
        elif command == "hello":
            print(Fore.BLUE + "How can I help you? 😊")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(args, book))
        else:
            print(Fore.RED + "❌ Invalid command. Use 'add', 'change', 'phone', 'all', 'add-birthday', 'show-birthday', 'birthdays', 'hello', 'exit', or 'close'.")

if __name__ == "__main__":
    main()