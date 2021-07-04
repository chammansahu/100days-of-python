# this is collction of some edabit exercises

def combinations(*items):
    result = 1
    for i in items:
        if i == 0:
            continue
        else:
            result *= i
    return result

# print(combinations(6, 7, 0))

# Karaksa encryption algorithm
def encrypt(word):

    # Step 1: Reverse the input: "elppa"
    wordReversed = []
    for i in range(0, len(word)):
        wordReversed.append(word[i])

    wordReversed.reverse()
    reversed = ""
    for item in wordReversed:
        reversed += item

    # Step 2: Replace all vowels using the following chart:
    replaced = ""
    vowels = 'aeiou'

    replaced = reversed.replace('a', '0').replace(
        'e', '1').replace('i', '2').replace('o', '2').replace('u', '3')
    return replaced+"aca"
# a = > 0
# e = > 1
# i = > 2
# o = > 2
# u = > 3

# # "1lpp0"
# Step 3: Add "aca" to the end of the word: "1lpp0aca"

# Output: "1lpp0aca"

# Examples
# encrypt("banana") ➞ "0n0n0baca"


print(encrypt("banana"))
