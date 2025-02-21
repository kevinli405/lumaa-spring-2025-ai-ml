import pandas as pd
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load movie dataset from a CSV file
def load_dataset(filepath):
    df = pd.read_csv(filepath)
    return df[['movie_title', 'plot_keywords']].dropna()

# Preprocess keywords by converting to lowercase
def preprocess_keywords(keywords):
    return ' '.join(keywords.lower().split('|'))

# Compute cosine similarity between user query and movie keywords
def compute_similarity(df, user_query, top_n=5):
    df['processed_keywords'] = df['plot_keywords'].apply(preprocess_keywords)
    
    vectorizer = TfidfVectorizer()
    keyword_matrix = vectorizer.fit_transform(df['processed_keywords'])
    query_vector = vectorizer.transform([user_query.lower()])
    
    similarity_scores = cosine_similarity(query_vector, keyword_matrix).flatten()
    df['similarity'] = similarity_scores

    return df.nlargest(top_n, 'similarity')[['movie_title', 'similarity']]

# Main function to handle user input and generate recommendations
def main():
    if len(sys.argv) < 2:
        print("Usage: python recommend.py \"<user query>\"")
        sys.exit(1)
    
    user_query = sys.argv[1]
    dataset_path = 'dataset/movie_metadata.csv'
    
    df = load_dataset(dataset_path)
    recommendations = compute_similarity(df, user_query)
    
    print("Top movie recommendations:")
    for _, row in recommendations.iterrows():
        print(f"{row['movie_title']} (Similarity: {row['similarity']:.2f})")

if __name__ == "__main__":
    main()
