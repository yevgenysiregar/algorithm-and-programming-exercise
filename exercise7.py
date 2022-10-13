sentence = input('Enter a Sentence: ').lower()
words = sentence.split()

for i, word in enumerate(words):

    if word[0] in 'aeiou':
        words[i] = words[i] + "yay"
    else:

        hasVowel = False

        for j, letter in enumerate(word):
            if letter in 'aeiou':
                words[i] = word[j:] + word[:j] + "ay"
                hasVowel = True
                break

        if (hasVowel == False):
            words[i] = word[j:] + word[:j] + "ay"

pigLatin = ' '.join(words)
print("Pig Latin Sentence: ", pigLatin)