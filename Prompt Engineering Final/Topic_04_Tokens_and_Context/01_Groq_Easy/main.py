text = input("Enter some text: ")

# Approximate token count using words
tokens = text.split()

print("\nAnalysis")
print("-" * 40)
print(f"Characters : {len(text)}")
print(f"Words      : {len(tokens)}")
print(f"Approx Tokens : {len(tokens)}")

print("\nTokens")
for i, token in enumerate(tokens, start=1):
    print(f"{i}. {token}")