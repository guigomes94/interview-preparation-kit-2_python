def catAndMouse(a, b, c):
    winner = ['Cat A', 'Cat B', 'Mouse C']
    distance_a_c = abs(a - c)
    distance_b_c = abs(b - c)
    if distance_a_c == distance_b_c:
        return winner[2]
    elif distance_a_c > distance_b_c:
        return winner[1]
    else:
        return winner[0]
