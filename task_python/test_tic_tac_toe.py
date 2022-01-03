import logging


def judge_the_play(data):
    logging.info("check line")
    i = 0
    while i < 3:
        line = data[i]
        if line == "XXX": return "X player is win"
        if line == "OOO": return "O player is win"
        i += 1
    logging.info("check columns")
    j = 0
    while j < 3:
        column = data[0][j] + data[1][j] + data[2][j]
        if column == "XXX": return f"X player is win"
        if column == "OOO": return "O player is win"
        j += 1

    logging.info("check diagonals")
    d1 = data[0][0] + data[1][1] + data[2][2]
    d2 = data[2][0] + data[1][1] + data[0][2]
    # print("D1: " + d1 + " - D2: " + d2)
    diagonals_values = [d1, d2]
    k = 0
    while k < 2:
        diagonal = diagonals_values[k]
        if diagonal == "XXX": return "X player is win"
        if diagonal == "OOO": return "O player is win"
        k += 1

    return "It is draw"


def test_tic_tac_toe():
    print(judge_the_play([
        "X.O",
        "XX.",
        "XOO"]))
    print(judge_the_play([
        "OOO",
        "XX.",
        "XOX"]))
    print(judge_the_play([
        "OO.",
        "OXX",
        "XXO"]))
    print(judge_the_play([
        "OOX",
        "OXO",
        "OXX"]))
    print(judge_the_play([
        "O.X",
        "XX.",
        "XOO"]))
