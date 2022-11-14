from gensim import corpora, models, similarities, downloader
import matplotlib.pyplot as plt
from features import *
import os.path
from collections import Counter

# class bebrochka:models.ldamodel.LdaModel(corpus=None, num_topics=100, 
#                                 id2word=None, distributed=False, 
#                                 chunksize=2000, passes=1, update_every=1, 
#                                 alpha='symmetric', eta=None, decay=0.5, 
#                                 offset=1.0, eval_every=10, iterations=50, 
#                                 gamma_threshold=0.001, minimum_probability=0.01, 
#                                 random_state=None, ns_conf=None, minimum_phi_value=0.01, 
#                                 per_word_topics=False, callbacks=None)


# first part of lab 7
corpus = corpora.BleiCorpus('ap/ap.dat', 'ap/vocab.txt')
# print(corpus)
model = models.ldamodel.LdaModel(corpus, id2word = corpus.id2word)
# print(model)
doc = corpus.docbyoffset(0) # первый документ
topics = model[doc]
# print(topics)

num_topics_used = [len(model[doc]) for doc in corpus]
# print(num_topics_used)

plt.hist(num_topics_used)
plt.show()

# Работаем с ap.txt
text = ''
if os.path.exists('preprocessed_ap/ap.txt') is not True: # Если проблемы с файликом preprocessed_ap/ap.txt, удалите его
    with open("ap/ap.txt") as ap:
        text = ap.read()

    articles = articles_splitter(text)
    with open('preprocessed_ap/ap.txt','w') as ap: # Если проблемы, добавьте аргумет в open() - encoding='utf-8'
        for article in articles:
            ap.write(article)
else:
    with open("preprocessed_ap/ap.txt") as ap:
        text = ap.read()

# Работаем с vocab.txt
vocab = ''
if os.path.exists('preprocessed_ap/vocab.txt') is not True:
    with open("ap/vocab.txt") as v:
        vocab = v.read()
    with open('preprocessed_ap/vocab.txt','w') as v: # Если проблемы, добавьте аргумет в open() - encoding='utf-8'
        vocab = full_preprocessing(vocab)
        vocab = list(set(vocab))
        for word in vocab:
            v.write(str(word) + "\n")
else:
    with open("preprocessed_ap/vocab.txt") as v:
        vocab = v.read()

if os.path.exists('preprocessed_ap/ap.dat') is not True:
    ap_data = []
    list_of_texts = text.splitlines()
    list_of_vocab = vocab.split()
    texts = []
    for tekst in list_of_texts:
        tekst = clean_text(tekst)
        tekst = full_preprocessing(tekst)
        texts.append(tekst)

    match = ''
    output_data = ''
    for t in texts:
        words = Counter(t)
        count_er = 0
        for k, v in words.items():
            for w in list_of_vocab:
                if k == w:
                    count_er += 1
                    match += str(list_of_vocab.index(w)) + ":" + str(v) + " "
        output_data += str(count_er) + " " + match + "\n"
        match = ''

    file = open('preprocessed_ap/ap.dat', 'w')
    file.write(output_data)
    file.close

# first part of lab 7
corpus_pp = corpora.BleiCorpus('preprocessed_ap/ap.dat', 'preprocessed_ap/vocab.txt')
# print(corpus)
model = models.ldamodel.LdaModel(corpus, id2word = corpus.id2word)
# print(model)
doc = corpus.docbyoffset(0) # первый документ
topics = model[doc]
# print(topics)

num_topics_used = [len(model[doc]) for doc in corpus]
# print(num_topics_used)

plt.hist(num_topics_used)
plt.show()

# попытка прогенерировать словарик на основе обработанного текста
# with open('preprocessed_ap/vocab.txt', 'w') as f:
#     text_vocab = text.split()
#     text_vocab = list(set(text_vocab))
#     for word in text_vocab:
#         f.write(word + "\n")

#РАЗБИВАЕМ ТЕКСТЫ, ПРОГОНЯЕМ КАЖДОЕ СЛОВО ПО ТЕКСТУ И СЧИТАЕМ СКОЛЬКО ОНО РАЗ ВСТРЕТИЛОСЬ




