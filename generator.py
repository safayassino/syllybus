"""generator.py takes a (line = syllable) file  and gives a corresponding randomized one, checking repetition"""

import random


def main():
    syllables = []
    with open('hyphenSyllables.txt', 'r', encoding='utf-8') as in_file:
        for line in in_file.readlines():
            syllables.append(line.strip())
    random_syl = []
    for i in range(len(syllables)):
        choice = random.choice(syllables)
        if len(random_syl) == 0 or choice != random_syl[-1]:
            syllables.remove(choice)
            random_syl.append(choice)
    with open("randomSyllables.txt", 'w', encoding='utf-8') as out_file:
        out_file.write("".join(str(item + '\n') for item in random_syl))
    return random_syl


if __name__ == '__main__':
    main()
