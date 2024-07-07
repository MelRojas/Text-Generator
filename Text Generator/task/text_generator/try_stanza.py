import stanza

nlp = stanza.Pipeline(lang='ko', processors='tokenize,pos')

doc = nlp(input())

print(*[f'{word.text} - {word.upos}' for sent in doc.sentences for word in sent.words], sep='\n')
