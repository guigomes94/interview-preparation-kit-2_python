def birthdayCakeCandles(candles):
    higher = max(candles)
    count = 0
    for v in candles:
        if v == higher:
            count += 1
    return count
