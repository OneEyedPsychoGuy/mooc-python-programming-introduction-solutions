def main() -> None:
    phone_book = {}
    while True:
        command = input("command (1 search, 2 add, 3 quit): ")
        if command == "1":
            search(phone_book)
        elif command == "2":
            add(phone_book)
        elif command == "3":
            break
    print("quitting...")

def search(phone_book: dict[str, str]) -> None:
    name = input("name: ")
    if name in phone_book:
        print(phone_book[name])
    else:
        print("no number")

def add(phone_book: dict[str, str]) -> None:
    name = input("name: ")
    number = input("number: ")
    phone_book[name] = number
    print("ok!")

main()