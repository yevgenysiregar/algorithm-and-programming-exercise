sentence = input('Enter a Sentence: ').lower()
words = sentence.split()

for i, word in enumerate(words):

    if word[0] in 'aeiou':
        words[i] = words[i] + "yay"
    else:

        has_vowel = False

        for j, letter in enumerate(word):
            if letter in 'aeiou':
                words[i] = word[j:] + word[:j] + "ay"
                has_vowel = True
                break

        if (has_vowel == False):
            words[i] = word[j:] + word[:j] + "ay"

pig_latin = ' '.join(words)
print("Pig Latin: ", pig_latin)