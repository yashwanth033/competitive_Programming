def can_two_movies_fill_flight(movie_lengths,flight_length):
    lengths = {}
    for length in movie_lengths:
        complement = flight_length - length
        if complement in lengths:
            return True
        lengths[length] = True
    return False

if __name__ == '__main__':
    print(can_two_movies_fill_flight([3, 8], 6))