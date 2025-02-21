# Movie Recommendation System

## Overview
This is a simple content-based movie recommendation system that uses TF-IDF to find the most similar movies based on user input keywords.

## Dataset
- The data is from the IMDb Top 5000 Movies dataset
- Ensure that the dataset is stored in `dataset/movie_metadata.csv`.

## Setup

### Install Dependencies
Run the following command to install the required Python packages:
```sh
pip install -r requirements.txt
```

## Usage
To run the recommendation system, use the following command:
```sh
python recommend.py "your movie preference query"
```

### Results (Example)
```sh
python recommend.py "I like superhero movies"
```
Output:
```
Top movie recommendations:
X-Men  (Similarity: 0.66)
X-Men: Apocalypse  (Similarity: 0.61)
My Super Ex-Girlfriend  (Similarity: 0.59)
Zoom  (Similarity: 0.59)
The Specials  (Similarity: 0.55)
```

## Salary Expectation Per Month
$2500

