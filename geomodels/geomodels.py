import pandas as pd
import pickle
from sklearn.metrics.pairwise import linear_kernel

def georecommend_prep(s, vectorizer, svd, model, labels):
    s_vector = vectorizer.transform([s])
    s_X = svd.transform(s_vector)
    s_cluster_idx = model.predict(s_X)[0]
    s_cluster_name = labels[s_cluster_idx]   
    return s_cluster_idx, s_vector


def georecommend(s):
    
    df_clustered = pd.read_csv('clustered_dataset.csv')
    vectorizer = pickle.load(open('vectorizer.pickle', 'rb'))
    svd = pickle.load(open('svd.pickle', 'rb'))
    model = pickle.load(open('model.pickle', 'rb'))
    labels = pickle.load(open('cluster_labels.pickle', 'rb'))
    
    idx, s_vector = georecommend_prep(s, vectorizer, svd, model, labels)
    df = df_clustered[df_clustered.cluster_idx == idx].dropna().reset_index()
    cluster_vectors = vectorizer.transform(df.abstract)
    
    cosine_similarities = linear_kernel(s_vector, cluster_vectors).flatten()
    ranked_indices = cosine_similarities.argsort()[::-1]
    
    return df.iloc[ranked_indices]
    