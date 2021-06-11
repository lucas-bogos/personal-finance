import json
import os
from tabulate import tabulate
from time import sleep, localtime
from random import randint
from colored import stylize, fg

list_finances = {
    "Light":100,
    "Water":100,
    "Bus or Train":100,
    "Driving":200
}

def save_changes(data):
    with open("all_data.json", "w", encoding="UTF-8") as Save:
        json.dump(data, Save, indent=4)

def read_data():
    finances = []
    values = []

    with open("all_data.json", "r", encoding="UTF-8") as Extract:
        datas = json.load(Extract)

        for key, item in datas.items():
            finances.append(key)
            values.append(item)
    print(tabulate(
        [finances, values], headers="firstrow", tablefmt="github")
        )

def add_on_all_data(name_finance, value_finance):
    list_finances[name_finance] = value_finance
    save_changes(list_finances)

def updating():
    with open("all_data.json", "r", encoding="UTF-8") as Extract:
        extracted = json.load(Extract)
        print(
            str(extracted)
            .replace(",","\n")
            .replace("{","")
            .replace("}","")
            .replace("'","")
            .replace(" ", "")
            )
        name = str(input("Choose a name for your finance: "))
        value = int(input("Typing a value here: "))
        extracted.update({name:value})
        print("updating the system...")
        print(extracted)
        save_changes(extracted)

def removing():
        with open("all_data.json", "r", encoding="UTF-8") as Extract:
            extracted = json.load(Extract)
            print(
                str(extracted)
                .replace(",","\n")
                .replace("{","")
                .replace("}","")
                .replace("'","")
                .replace(" ", "")
                )
            name = str(input("Delete a finance with the name: "))
            extracted.pop(name)
            print("deleting of the system...")
            sleep(randint(0, 5))
            print(extracted)
            save_changes(extracted)

def perfil_of_user(user_name, password_user):
    perfil = {
        "user": user_name,
        "password": password_user
    }

    with open("user_perfil.json", "w", encoding="UTF-8") as User:
        json.dump(perfil, User, indent=4)

def options_for_user():
    services = {
        1:"All list",
        2:"Add data",
        3:"Do update",
        4:"Delete",
        5:"Perfil myself",
        6:"Quit"
        }

    for key, item in services.items():
        print(f"{key}- {item}")

def validation_of_user():
    user = str(input("Write your user: "))
    password = str(input("typing your password here: "))

    with open("user_perfil.json", "r", encoding="UTF-8") as ExtractPerfil:
        datas = json.load(ExtractPerfil)

def file_exists():
    test = False
    dir = os.listdir("../personal-finance")
    
    if "user_perfil.json" in dir:
        print("Validating...")
        sleep(randint(0, 5))
        test = True
        print(stylize("Ok", fg("green")))
    return test

if __name__=="__main__":
    print("Welcome to personal finance!")
    res = file_exists()
    print(stylize("Accessing...", fg("yellow")))
    sleep(randint(0, 10))

    with open("user_perfil.json", "r", encoding="UTF-8") as Extract:
            print("Insert your datas bellow here: ")
            username = input(str("Username: "))
            passwd = input(str("Password: "))
            extracted = json.load(Extract)

            if extracted["user"] == username and extracted["password"] == passwd:

                if not res == False:
                    while True:
                        options_for_user()
                        option = int(input("Select just one option: "))
                        if option == 1:
                            read_data()

                        if option == 2:
                            name = str(input("Choose a name for the finance: "))
                            value = int(input("Insert just one value: "))
                            add_on_all_data(name, value)
                        
                        if option == 3:
                            updating()
                        if option == 4:
                            removing()
                        if option == 5:
                            user = str(input("Typing a name for your user: "))
                            password = str(input("Now, choose your password: "))

                            perfil_of_user(user, password)
                        if option == 6:
                            ask = str(input(
                                "Do you want to continue?[y/n] ")
                                .lower())

                            if not ask == "n":
                                break
            else:
                print(stylize("Not available!", fg("red")))