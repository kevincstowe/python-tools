import time
import gensim
import numpy as np

def get_pretrained_vectors(model_loc="/home/kevin/SVN/GoogleNews-vectors-negative300.bin"):
    print ("loading pretrained word embeddings from " + model_loc + "...")
    st = time.time()
    result = gensim.models.Word2Vec.load_word2vec_format(model_loc, binary=True)
    print ("pretrained embeddings loaded in " + str(time.time()-st))
    return result

def word_w2v(word, w2v_model, context=[]):
    if word in w2v_model:
        vec = w2v_model[word]
    else:
        vec = np.zeros((300,))

    for w in context:
        if w in w2v_model:
            vec = np.append(vec,w2v_model[w])
        else:
            np.append(vec, [0]*w2v_model.layer1_size)
    return vec
