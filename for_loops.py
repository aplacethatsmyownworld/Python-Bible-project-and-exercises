vowel = 0
consonants = 0

for letter in "Emanuale":
    if letter.lower()in "aeiou":
        vowel = vowel + 1
    elif letter == " ":
        pass
    else:
        consonants = consonants + 1
    
print("There are {} vowels.".format(vowel))
print("There are {} consonants.".format(consonants))


students = {
    "male":["Tom", "Charlie", "Harry", "Frank"],
    "female": ["Sarah", "Huda", "Samantha", "Emily", "Elization"]
    }

for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)
