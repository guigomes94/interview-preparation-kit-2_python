def hackerrankInString(str):
    original = 'hackerrank'
    index_o = 0
    replica = ''
    for i in range(len(str)):
        if str[i] == original[index_o]:
            replica += str[i]
            index_o += 1
    if replica == original:
        return 'YES'
    return 'NO'
