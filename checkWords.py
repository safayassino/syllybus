import phunspell
import random


def main():
    syllables = []
    N_syl = 72
    with open('hyphenSyllables.txt', 'r', encoding='utf-8') as in_file:
        for line in in_file.readlines():
            syllables.append(line.strip()
    random_syl = []
    pspell = phunspell.Phunspell('it_IT')
    while len(random_syl) != N_syl:
        choice = random.choice(syllables)
        if len(random_syl) == 0 or choice != random_syl[-1]:
            random_syl.append(choice)
            index = random_syl.index(choice)
            if len(random_syl) > 1:
                word = "".join(random_syl[index - 1: index + 1])
                print(word)
                print(random_syl)
                if pspell.lookup(word):
                    random_syl.pop()
                else:
                    syllables.remove(choice)
                    print(random_syl)
    with open("checkedSyllables.txt", 'w', encoding='utf-8') as out_file:
        out_file.write("".join(str(item + '\n') for item in random_syl))


if __name__ == '__main__':
    main()
