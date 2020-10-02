

#we can loop

def add(*numbers):
    total = 0
    for number in numbers:
            total = total + number
    return(total)

#example

print(add(1,2,3,4,5,6,7,8,9))
