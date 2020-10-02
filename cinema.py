films = {
    "Finding Dory": [3,5],
    "Bourne": [18,5],
    "Tarzan": [15,5],
    "Moana": [10,5]
    }

while True:
    choice = input("What do you want to watch?:").strip().title()
    if choice in films:
        age = int(input("How old are you?").strip())
        #check user age
        if age >= films[choice][0]:
            #check enough seats
            num_seats = films[choice][1]
            if num_seats>0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1]- 1
            else: print("sorry we are sold out")
        else:
            print("You are too young")
            
        pass
    else:
        print("We don't have that film...")
    
                   
