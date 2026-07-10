import random
import os

print("=" * 60)
print("TEXT GENERATION USING MARKOV CHAINS")
print("=" * 60)

os.makedirs("outputs", exist_ok=True)

text = """
Artificial Intelligence is changing the world.
Artificial Intelligence helps humans solve complex problems.
Machine Learning is a part of Artificial Intelligence.
Deep Learning is a subset of Machine Learning.
Generative AI creates text images audio and videos.
Technology makes our lives easier and smarter.
Python is one of the most popular programming languages.
Python is widely used in Artificial Intelligence projects.
"""

words = text.split()

markov_chain = {}

for i in range(len(words)-1):

    word = words[i]

    next_word = words[i+1]

    if word not in markov_chain:
        markov_chain[word] = []

    markov_chain[word].append(next_word)

start = input("Enter starting word : ")

if start not in markov_chain:
    print("Word not found")
    exit()

generated = [start]

current = start

for i in range(40):

    if current not in markov_chain:
        break

    nxt = random.choice(markov_chain[current])

    generated.append(nxt)

    current = nxt

result = " ".join(generated)

print("\nGenerated Text\n")

print(result)

with open("outputs/generated_text.txt","w") as file:

    file.write(result)

print("\nOutput saved in outputs/generated_text.txt")
