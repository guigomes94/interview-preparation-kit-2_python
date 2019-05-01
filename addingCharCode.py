def addingCharCode(str):
    arr = convert(str)
    return sum(arr)

def convert(str):
    code = []
    for letter in str:
        code.append(ord(letter))
    return code
