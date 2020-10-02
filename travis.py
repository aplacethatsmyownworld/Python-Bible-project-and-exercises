known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]



while True:
    print("Hi! My name is Travis")
    name = input("What is your name?:").strip().capitalize()

    if name in known_users:
        print("Hello {}! How are you today?".format(name))
        remove = input("Would you like to be removed from the system? (y/n)?").lower()
        if remove == "y":
            known_users.remove(name)
            print(known_users)
        elif remove == "n":
            print("No worries, I like you to stay anyway!")
            
    else:
        print("I dont think I met you yet {}".format(name))
        add_me = input("Would you like to be added to our list? y/n?:").strip().lower()
        if add_me == "y":
            known_users.append(name)
            print(known_users)
        elif add_me == "n":
            print("Alright. See you around!")
