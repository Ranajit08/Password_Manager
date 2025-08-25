import json
import sys
from strtobin import string_to_binary


def main():
    if len(sys.argv) < 2:
        print("Error: no commands")
    elif len(sys.argv) < 3:
        if sys.argv[1] == "-reg":
            registration()
        else:
            print("Error: no commands")
    elif len(sys.argv) < 5:
        if sys.argv[1] == "-u" and sys.argv[3] == "-p":
            try:
                with open("users_data.json", "r") as file:
                    users = json.load(file)
                    if (
                        sys.argv[2] in users
                        and users[sys.argv[2]]["password"] == sys.argv[4]
                    ):
                        mainloop(sys.argv[2], sys.argv[4])
                    else:
                        print("Incorrect data :(")
            except (FileNotFoundError, json.JSONDecodeError):
                print("Error: FILE NOT FOUND.")
        else:
            print("Error: no commands")
    else:
        print("Error: no commands")


def mainloop(username: str, password: str) -> None:
    while True:
        arg = input(f"{username}> ")
        if arg == ".exit":
            break
        elif arg == ".insert":
            ...
        elif arg == ".get":
            ...
        elif arg == ".alter":
            ...
        elif arg == ".delete":
            ...


def registration():

    USER_INPUT_1 = input("Set User Name: ")

    try:
        with open("users_data.json", "r") as file:
            users = json.load(file)
    except:
        users = {}

    if USER_INPUT_1 in users:
        sys.exit("username already exist.")

    USER_INPUT_2 = string_to_binary(input("Set Password: "))

    if USER_INPUT_1 not in users:
        users[USER_INPUT_1] = {"password": USER_INPUT_2, "data": []}

        with open("users_data.json", "w") as file:
            json.dump(users, file, indent=4)
            print(f"✔️  Account created succuessfully!")
    else:
        print(f"({USER_INPUT_1}) username is already exist")


if __name__ == "__main__":
    main()
