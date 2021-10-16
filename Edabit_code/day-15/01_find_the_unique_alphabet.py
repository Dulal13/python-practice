def find_letters(word):
    word = list(word)
    unique_alphabet = []
    for alphabet in word:
        if(alphabet not in unique_alphabet and word.count(alphabet) == 1):
             unique_alphabet.append(alphabet)
    return unique_alphabet

res = find_letters("monopoly")
print(res)

