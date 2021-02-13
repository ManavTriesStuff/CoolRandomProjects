from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text=["Iron Man America","Captain America Iron"]
cv=CountVectorizer()
count_matrix=cv.fit_transform(text)
#print(count_matrix.toarray())
sim_scores=cosine_similarity(count_matrix)
print(sim_scores)