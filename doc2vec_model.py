# import pre_process as pp
import joining_the_sheeple as vcb
# Gensim
import gensim


# Create the tagged document needed for Doc2Vec
def create_tagged_documents(vocab):
    documents = []
    sentence = []
    i = 0
    for line in vocab["data"]:
        for word in line.split():
            sentence.append(word)

        documents.append(gensim.models.doc2vec.TaggedDocument(sentence, [i]))
        i += 1
        sentence = []

    return documents


train_data = create_tagged_documents(vcb.vocab1)

# Init the Doc2Vec model
model = gensim.models.doc2vec.Doc2Vec(vector_size=5, min_count=5, epochs=20)
model.build_vocab(train_data)
model.save("C:\\Users\\Zacha\\PycharmProjects\\dv_midterm\\d2v.model")
model_stored = gensim.models.doc2vec.Doc2Vec.load("C:\\Users\\Zacha\\PycharmProjects\\dv_midterm\\d2v.model")







