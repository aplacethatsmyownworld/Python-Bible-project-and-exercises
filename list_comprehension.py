even_numbers = [x for x in range(1,1002)if x%2 ==0]
print(even_numbers)

odd_numbers = [y for y in range(1,1002) if y%2 !=0]
print(odd_numbers)

words = ["the", "long", "white", "airplane", "flies", "over", "the", "giant", "green",
         "mountain"]
answer = [[w.upper(), w.lower(), len(w)]for w in words]
print(answer)

[[w.upper(), w.lower(), len(w)]for w in words]
