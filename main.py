from array.sorted_square_array_easy import prepare_sorted_square_array
from array.tournament_winner import find_tournament_winner

if __name__ == "__main__":
    # prepared_sorted_square_array = prepare_sorted_square_array([-4, -1, 0, 3, 10])
    # print(prepared_sorted_square_array)

    tournament_winner = find_tournament_winner([
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"]
      ],[0, 0, 1])

    print(tournament_winner)
