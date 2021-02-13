import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
###### helper functions.#######
def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]
##################################################

##Step 1: Read CSV File
df=pd.read_csv("movie_dataset.csv")
#print(df.columns)
##Step 2: Select Features
features=['keywords','cast','genres','director']
##Step 3: Create a column in DF which combines all selected features
for feat in features:
	df[feat]=df[feat].fillna('')
def combine_features(row):
	try:
		return row['keywords']+''+row['cast']+''+row['genres']+''+row['director']
	except:
		print("Error:",row)
df["combined_features"]=df.apply(combine_features,axis=1)
#print(df["combined_features"].head())
##Step 4: Create count matrix from this new combined column
cv=CountVectorizer()
count_matrix=cv.fit_transform(df["combined_features"])
#print(count_matrix.toarray())
##Step 5: Compute the Cosine Similarity based on the count_matrix
sim_scores=cosine_similarity(count_matrix)
#print(sim_scores)
userpick = "Iron Man"
## Step 6: Get index of this movie from its title
movie_index=get_index_from_title(userpick)
sim_movies=list(enumerate(sim_scores[movie_index]))

## Step 7: Get a list of similar movies in descending order of similarity score
sorted_movies=sorted(sim_movies, key=lambda x:x[1],reverse=True)
## Step 8: Print titles of first 50 movies
i=0
for movie in sorted_movies:
	print(get_title_from_index(movie[0]))
	i+=1
	if i>10:
		break
