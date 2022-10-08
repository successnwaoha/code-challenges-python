
def hasWon(val, play, player):
    splitted = play.split(",")
    a = int(splitted[0])
    b = int(splitted[1])

    if a == b:
        if val[0][0] == val[1][1] == val[2][2]:
            return True
    
    if a == 1 and b == 3:
        if val[0][2] == val[1][1] == val[2][0]:
            return True

    if a == 3 and b == 1:
        if val[2][0] == val[1][1] == val[0][2]:
            return True

    vert = True
    hori = True
    for x in val[a - 1]:
        if x != player:
            v = False
            break
    for y in val:
        if y[b - 1] != player:
            hori = False
            break
    
    return vert and hori

