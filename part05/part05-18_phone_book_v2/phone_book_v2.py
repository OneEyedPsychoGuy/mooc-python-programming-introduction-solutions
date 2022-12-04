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

def search(phone_book: dict[str, list[str]]) -> None:
    name = input("name: ")
    if name in phone_book:
        for number in phone_book[name]:
            print(number)
    else:
        print("no number")

def add(phone_book: dict[str, list[str]]) -> None:
    name = input("name: ")
    number = input("number: ")
    if name not in phone_book:
        phone_book[name] = []
    phone_book[name].append(number)
    print("ok!")

main()