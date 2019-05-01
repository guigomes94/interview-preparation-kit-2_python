def countingValleys(s):
    level = valley = 0
    for l in s:
        if l == 'U':
            level += 1
            if level == 0:
                valley += 1
        else:
            level -= 1

    return valley

