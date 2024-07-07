# Write your code here
import random
import string

import nltk
from nltk.tokenize import TweetTokenizer
from nltk import ngrams
from collections import Counter

if __name__ == '__main__':
    f = open("../test/corpus.txt", "r", encoding="utf-8")
    # f = open(input(), "r", encoding="utf-8")

    tokens = f.read().split()
    # tokenizer = TweetTokenizer()
    # tokens = tokenizer.tokenize(f.read())


    # print(f'''Corpus statistics
    # All tokens: {len(tokens)}
    # Unique tokens: {len(set(tokens))}''')

    n = 3
    n_grams = list(ngrams(tokens, n))
    # print(f'Number of bigrams: {len(n_grams)}')

    grams_dict = {}
    for a, b, tail in n_grams:
        head = ' '.join([a, b])
        if head not in grams_dict.keys():
            grams_dict[head] = []

        grams_dict[head].append(tail)


    val = ""


    def checkSentenceStart(tokens):
        start = random.choice(tokens)
        if (start[0] in string.ascii_lowercase) or start.split(" ")[0][-1] in ['.', '!', '?']:
            return checkSentenceStart(tokens)
        else:
            return start



    # while True:
    try:
        # val = input()

        # if val == "exit":
        #     quit()

        # print(tokens[int(val)])

        # bigram = n_grams[int(val)]
        # print(f'Head: {bigram[0]}\tTail: {bigram[1]}')

        # tails = Counter(grams_dict[val])
        # print(f'Head: {val}')
        # for tail, count in tails.items():
        #     print(f'Tail: {tail}\tCount: {count}')

        sentences = []

        while len(sentences) < 10:
            start = checkSentenceStart(list(grams_dict.keys()))
            sentence = [start]
            sentenceDone = False
            while not sentenceDone:
                tails = Counter(grams_dict[start])
                nextWord = random.choices(list(tails.keys()), weights=tuple(tails.values()))[0]
                sentence.append(nextWord)
                start = start.split(' ')[1] + ' ' + nextWord

                sentenceDone = len(' '.join(sentence).split(' ')) >= 5 and start[-1] in ['.', '?', '!']

            sentences.append(sentence)
            print(" ".join(sentence))


    except KeyError:
        print("Key Error. The requested word is not in the model. Please input another word.")
    except IndexError as err:
        print("Index Error. Please input a value that is not greater than the number of all bigrams.")
    except (TypeError, ValueError) as err:
        print("Type Error. Please input an integer.")
