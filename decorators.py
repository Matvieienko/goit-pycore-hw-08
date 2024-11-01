from colorama import Fore

# Декоратор для обробки помилок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return Fore.RED + "🛑 This contact does not exist."
        except ValueError as e:
            return Fore.RED + f"⚠️  {e}"
        except IndexError:
            return Fore.RED + "⚠️  Incorrect number of arguments."
    return inner