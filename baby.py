from random import choice

question = ["Why the sun is hot?", "Why the stars are sparkling like diamonds?",
            "Why are you mad? I'm just asking questions"]

question = choice(question)

answer = input(question).strip().lower()

while answer != "just because":
   answer = input("why")

print("ah okay")
