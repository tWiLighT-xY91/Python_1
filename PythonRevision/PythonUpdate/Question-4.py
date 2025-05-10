# To count vowels in a string

def count_vowels(s) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


word = input("Enter any word to check the number of vowels present: ")
print(f"The number of vowels in the word you entered is: {count_vowels(word)}")