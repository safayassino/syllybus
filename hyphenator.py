"""hyphenator.py takes a (line = sentence) file and does syllabification, it gives one file with (line = syllabi-zed
sentence) one file with (line = syllable) """

from hyphen import Hyphenator


def sliceSentence(sentence):
    h = Hyphenator('it_IT')
    cleanSentence = ''.join(list(filter(lambda n: n != '.', sentence)))
    syllablesList = []
    wordsList = cleanSentence.split()
    for word in wordsList:
        if len(word) < 4:
            syllablesList.append(word)
        else:
            for syllable in h.syllables(word):
                syllablesList.append(syllable)
    return syllablesList


def main():
    file_path = input("Please enter the file's fully qualified path: ")
    with open(file_path, 'r', encoding='utf-8') as in_file:
        with open("hyphenSentences.txt", 'w', encoding='utf-8') as out_file_1:
            with open("hyphenSyllables.txt", 'w', encoding='utf-8') as out_file_2:
                for line in in_file.readlines():
                    out_file_1.write("".join(str(item + ' ') for item in sliceSentence(line)) + '\n')
                    out_file_2.write("".join(str(item + '\n') for item in sliceSentence(line)))


if __name__ == '__main__':
    main()
