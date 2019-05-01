def countApplesAndOranges(s, t, a, b, apples, oranges):
    res_apple = list(map(lambda v: v + a, apples))
    res_orange = list(map(lambda v: v + b, oranges))
    res_apple = list(filter(lambda v: v >= s and v <=t, res_apple))
    res_orange = list(filter(lambda v: v >= s and v <=t, res_orange))
    res = [len(res_apple), len(res_orange)]
    return res
