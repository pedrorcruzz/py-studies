input_word = input("Enter a word or sentence: ").lower()  # Converte tudo para minúsculas
vowels = "aeiou"  
count = 0 

for char in input_word:
    if char in vowels:  
        count += 1

print(f"The input contains {count} vowel(s).")