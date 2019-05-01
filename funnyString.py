from addingCharCode import convert

def funnyString(str):
    #converse char to code
    charCode = convert(str)
    #copy and reverse
    revCode = charCode[:]
    revCode.reverse()
    res_char = []
    res_rev = []
    #calcs
    for i in range(len(str) - 1):
        res_char.append(abs(charCode[i] - charCode[i+1]))
        res_rev.append(abs(revCode[i] - revCode[i+1]))
    #funny or not funny
    count = 0
    for i in range(len(res_char)):
        if res_char[i] == res_rev[i]:
            count += 1
    if count == len(res_rev):
        return 'Funny'
    return 'Not Funny'
