# A simple next-word prediction dictionary

predictions = {
    "I": ["am", "like", "have"],
    "am": ["learning", "a", "working"],
    "learning": ["Python", "AI", "LLMs"],
    "Python": ["programming", "today", "basics"],
    "AI": ["today", "models", "concepts"]
}

sentence = input("Enter a sentence: ")

words = sentence.split()

if not words:
    print("Please enter some text.")
    exit()

last_word = words[-1]

print("\nPossible Next Words")
print("-" * 30)

if last_word in predictions:
    for i, word in enumerate(predictions[last_word], start=1):
        print(f"{i}. {word}")
else:
    print("No prediction available.")