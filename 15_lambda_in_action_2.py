movies = {
    1: {"title": "Lift", "score": 63},
    2: {"title": "Napoleon", "score": 65},
    3: {"title": "The Marvels", "score": 64},
    4: {"title": "Aquaman and the Lost Kingdom", "score": 65},
    5: {"title": "Society of the Snow", "score": 80},
    6: {"title": "Deep Fear", "score": 53}
}


def get_score(movie_id):
    print(movie_id)
    return movie_id


movies_sorted = sorted(movies, key=get_score)
print(movies_sorted)