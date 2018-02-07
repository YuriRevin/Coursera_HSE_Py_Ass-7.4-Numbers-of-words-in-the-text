import sys

fInp = sys.stdin
word = []
lWords = []
charList = {'\n', ' '}
for line in fInp:
    for char in line:
        if char not in charList:
            word.append(char)
        else:
            if len(word) > 0:
                lWords.append(''.join(word))
                word = []
setLWords = set(lWords)
print(len(setLWords))
