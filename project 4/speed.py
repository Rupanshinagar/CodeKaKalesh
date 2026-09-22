import random 
import time

print("Let's see how fast you are!")
print()

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Pack my box with five dozen liquor jugs.",
    "How vexingly quick daft zebras jump!", 
    "Sphinx of black quartz, judge my vow.",
    "The five boxing wizards jump quickly.",
    "Jackdaws love my big sphinx of quartz.",
    "The quick onyx goblin jumps over the lazy dwarf.",
]

sentences = random.choice(sentences)

print("type this sentence like a flash from DC would type")
print()
print(sentences)
print()

input("press enter when feel like that you are flash")
print()

start_time = time.time()

typed_sentence = input("start typing\n ")

end_time = time.time()

time_taken = end_time - start_time
time_taken_minutes=time_taken / 60

word_typed = len(typed_sentence.split())
wpm = word_typed / time_taken_minutes

if time_taken_minutes > 0:
    speed = word_typed / time_taken_minutes
else:
    wpm = 0
original_words= sentences.split()
typed_words= typed_sentence.split()
correct_words=0
total_words = len(original_words)

for i in range(len(typed_words)):
    if i < len(original_words) and typed_words[i] == original_words[i]:
        correct_words += 1

if total_words > 0:
    accuracy = (correct_words / total_words) * 100
else:
    accuracy = 0

print()
print("Here we found you are flash or not")
print(f"time taken:", round(time_taken, 2), "seconds" )
print(f"words per minute:", round(wpm, 2))
print(f"accuracy:", round(accuracy, 2), "%")

print()
if wpm<20:
    print("You are not flash")
elif wpm<40:
    print("You are average")
elif wpm<60:
    print("You are fast")
else:
    print("You are flash")  


