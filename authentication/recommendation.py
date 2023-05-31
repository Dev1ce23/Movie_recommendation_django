import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity
from .models import Movie

def recommendations(title):
    

    # db_Title = Movie.objects.all()
    # data = list(db_Title.values("Title"))
    # print(data)
    # Title = []
    # for i in data:
    #     Title.append(i["Title"])
    # print(len(Title))

    movies = dict(Movie.objects.values_list("Title","Plot"))
    x= list(movies.keys())
    y= list(movies.values())
    data = pd.DataFrame({'Title': x, 'Plot': y})
    finaldata=data[["Title","Plot"]]
    finaldata=finaldata.set_index('Title')


    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    lemmatizer=WordNetLemmatizer()

    nltk.download('stopwords')
    stop_words=set(stopwords.words('english'))

    VERB_CODES = {'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}



    
    def preprocess_sentences(text):
        text=text.lower()
        temp_sent=[]
        words=nltk.word_tokenize(text)
        tags=nltk.pos_tag(words)
        for i, word in enumerate(words):
            if tags[i][1] in VERB_CODES: 
                lemmatized = lemmatizer.lemmatize(word, 'v')
            else:
                lemmatized =lemmatizer.lemmatize(word)
            if lemmatized not in stop_words and lemmatized.isalpha():
                temp_sent.append(lemmatized)
                
        finalsent = ' '.join(temp_sent)
        finalsent = finalsent.replace("n't", " not")
        finalsent = finalsent.replace("'m", " am")
        finalsent = finalsent.replace("'s", " is")
        finalsent = finalsent.replace("'re"," are")
        finalsent = finalsent.replace("'ll", " will")
        finalsent = finalsent.replace("'ve", " have")
        finalsent = finalsent.replace("'d", " would")
        return finalsent
    

        
    finaldata["plot_processed"]=finaldata["Plot"].apply(preprocess_sentences)

    tfidfvec=TfidfVectorizer()

    tfidf_movieid=tfidfvec.fit_transform((finaldata["plot_processed"]))

    cos_sim=cosine_similarity(tfidf_movieid,tfidf_movieid)

    indices=pd.Series(finaldata.index)

    cosine_sim = cos_sim


    recommended_movies = []
    index = indices[indices == title].index[0]
    similarity_scores = pd.Series(cosine_sim[index]).sort_values(ascending = False)
    top_10_movies = list(similarity_scores.iloc[1:11].index)
    for i in top_10_movies:
        recommended_movies.append(list(finaldata.index)[i])
    return recommended_movies

