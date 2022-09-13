while True:
    # your code
    cont = input("Encrypt? yes/no > ")

    while cont.lower() not in ("yes", "no", "y", "n"):
        cont = input("Encrypt? yes/no > ")

    if cont == "no":
        print("Break")
        break