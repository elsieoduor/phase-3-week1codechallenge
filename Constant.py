# 1. Given a lowercase string that has alphabetic characters only and no spaces, 
# return the highest value of consonant substrings. 
# 2. Consonants are any letters of the alphabet except "aeiou".
# 3. We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

def get_consonant(c):
    return ord(c) - ord('a') + 1

def highest_consonant(s):
    max_value = 0
    current_value = 0

    for char in s:
        if char not in "aeiou":
            current_value += get_consonant(char)
            max_value = max(max_value, current_value)
        else:
            current_value = 0
    
    return max_value


string = input('Enter your string: ')
value = highest_consonant(string)
print(value)

