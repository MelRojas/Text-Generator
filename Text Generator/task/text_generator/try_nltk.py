import nltk

nltk.download("punkt")

sentence = """Green tea is very healthy. The grass was very green in spring. I always drink black tea, but my mother prefers green tea."""

bigramFinder = nltk.collocations.BigramCollocationFinder.from_words(
    nltk.word_tokenize(sentence)
)

bigram_freq = bigramFinder.ngram_fd.items()
print(bigram_freq)

n_grams = nltk.probability.FreqDist(nltk.word_tokenize(sentence))

for grams in n_grams:
    print(grams)

print(n_grams.freq("tea"))