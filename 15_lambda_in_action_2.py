movies = {
    1: {"title": "Lift", "score": 32},
    2: {"title": "Napoleon", "score": 78},
    3: {"title": "The Marvels", "score": 14},
    4: {"title": "Aquaman and the Lost Kingdom", "score": 95},
    5: {"title": "Society of the Snow", "score": 67},
    6: {"title": "Deep Fear", "score": 52}
}


movies_sorted = sorted(movies, key=lambda movie_id: movies[movie_id]["score"], reverse=True)

for movie_id in movies_sorted:
    print(f"Title:{movies[movie_id]['title']} Score: {movies[movie_id]['score']}")