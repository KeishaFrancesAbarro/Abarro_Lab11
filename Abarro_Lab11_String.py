words = []
lenght = []

for user in range(10):
    x = input("Enter a word:")
    words.append(x)
    
letters = int(input("Enter the number of letters:"))

for word in words:
    if len(word) == letters:
        lenght.append(word)
        
    else:
        continue 
    
print(f"Here are the words that have {letters} letters: {lenght}")