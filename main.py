from gensim import corpora, models, similarities, downloader
import matplotlib.pyplot as plt

# class bebrochka:models.ldamodel.LdaModel(corpus=None, num_topics=100, 
#                                 id2word=None, distributed=False, 
#                                 chunksize=2000, passes=1, update_every=1, 
#                                 alpha='symmetric', eta=None, decay=0.5, 
#                                 offset=1.0, eval_every=10, iterations=50, 
#                                 gamma_threshold=0.001, minimum_probability=0.01, 
#                                 random_state=None, ns_conf=None, minimum_phi_value=0.01, 
#                                 per_word_topics=False, callbacks=None)


# first part of lab 7
# corpus = corpora.BleiCorpus('ap/ap.dat', 'ap/vocab.txt')
# model = models.ldamodel.LdaModel(corpus, id2word = corpus.id2word)
# doc = corpus.docbyoffset(0) # первый документ
# topics = model[doc]
# print(topics)
# num_topics_used = [len(model[doc]) for doc in corpus]
# print(num_topics_used)
# plt.hist(num_topics_used)
# plt.show()