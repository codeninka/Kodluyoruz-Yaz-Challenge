text = input(" Gimme ur text\n")
###
# words = text.split(' ')
# letters = words.split()
###

letters = list(text)  # Splitting the text into individual letters

def count_letters(placeholder4letters):
    letter_count = {}
    for letter in letters:
        if letter.isalpha():
            letter = letter.lower()  # Convert to lowercase to treat uppercase and lowercase letters as the same
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

# Example usage

result = count_letters(letters)
print(result)
