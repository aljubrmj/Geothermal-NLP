import pandas as pd
import pickle

def georecommend_prep(s, vectorizer, svd, model, labels):
    s_vector = vectorizer.transform([s])
    s_X = svd.transform(s_vector)
    s_cluster_idx = model.predict(s_X)[0]
    s_cluster_name = labels[s_cluster_idx]   
    return s_cluster_idx


def georecommend_find(s):

    df_clustered = pd.read_csv('clustered_dataset.csv')
    vectorizer = pickle.load(open('vectorizer.pickle', 'rb'))
    svd = pickle.load(open('svd.pickle', 'rb'))
    model = pickle.load(open('model.pickle', 'rb'))
    labels = pickle.load(open('cluster_labels.pickle', 'rb'))
    idx = georecommend_prep(s, vectorizer, svd, model, labels)
    
    return df_clustered[df_clustered.cluster_idx == idx]
    