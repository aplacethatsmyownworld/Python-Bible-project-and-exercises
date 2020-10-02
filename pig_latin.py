#get sentence from user

original = input("Compose a long sentence here:").strip().lower()

#split sentence into words

words = original.split()


#loop through words and conver to pig latin

new_words = []

for w in words:
    if w[0] in "aeiou":
        new_word = w + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in w:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = w[:vowel_pos]
        the_rest = w[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)
            

# if starts with vowel, just add "yay"


# otherwise, move the first consonant cluster to end, and add "ay"

#stick words back together

output = " ".join(new_words)

#output the final string

print(output)
