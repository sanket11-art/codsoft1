import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the CSV
df = pd.read_csv('movies.csv')

# Combine 'genres' and 'description'
df['combined'] = df['genres'] + " " + df['description']

# Vectorize using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined'])

# Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommendation function
def recommend(movie_title, num_recommendations=3):
    if movie_title not in df['title'].values:
        print("Movie not found!")
        return

    idx = df[df['title'] == movie_title].index[0]
    scores = list(enumerate(cosine_sim[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:num_recommendations + 1]

    print(f"\nMovies similar to '{movie_title}':")
    for i, score in scores:
        print("-", df.iloc[i]['title'])

# Ask user for input
user_input = input("Enter a movie title: ")
recommend(user_input)
