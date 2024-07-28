from my_class import AddressBook, Record, Phone, Name

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please. Number should have 10 digits"
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command"

    return inner


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_username_phone(args, book: AddressBook):
    name, old_number, new_number = args
    record = book.find(name)
    if record:
        record.edit_phone(old_number, new_number)
        return "Contact updated."
    else:
        return "Name not found"

@input_error
def add_birthday(args, book: AddressBook):
    if len(args) < 2:
        return "Provide name and birthday."

    name, birthday_day = args
    record = book.find(name)

    if record:
        record.add_birthday(birthday_day)
        return "Contact updated."
    else:
        return "Name not found"

@input_error
def show_phone(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record:
        return book[name]
    else:
        return "Name not found"

@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record is None:
        return f"Contact with name {name} not found."
    if record.birthday is None:
        return f"No birthday set for {name}."
    return f"{name}'s birthday is on {record.birthday}"

@input_error
def birthdays(book: AddressBook):
    return (book.get_upcoming_birthdays())

@input_error
def show_all(book):
    pass

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_username_phone(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(book)

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "sb":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()