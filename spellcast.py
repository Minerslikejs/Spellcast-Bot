adjPos = open('collins.txt', 'r')
lines = adjPos.readlines()
adjPos.close()

letters = {
    'A': 2,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 1,
    'F': 5,
    'G': 3,
    'H': 4,
    'I': 1,
    'J': 7,
    'K': 6,
    'L': 3,
    'M': 4,
    'N': 2,
    'O': 1,
    'P': 4,
    'Q': 8,
    'R': 2,
    'S': 2,
    'T': 2,
    'U': 4,
    'V': 5,
    'W': 5,
    'X': 7,
    'Y': 4,
    'Z': 4
}
def getNearest(row,col):
    final = []
    for a in range(-1,2):
        for b in range(-1,2):
            if (0 <= int(row)+int(a) < 5) and (0 <= int(col)+int(b) < 5) and (a!=0 or b!=0):
                final.append([board[row+a][col+b],[int(row)+int(a),int(col)+int(b)]])
    return final
board = []
for i in range(0,5):
    b1 = input('input: ')
    t = []
    for i in b1:
        t.append(i.upper())
    board.append(t)
b1 = input('bonus letter (pos/val) (row/col): ')
dl = [int(b1[0]),int(b1[1])]
dlv = int(b1[2])
b1 = input('double word (row/col): ')
dw = [int(b1[0]),int(b1[1])]
print(dl,dw)

#board = [['L','A','G','E','T'],['O','O','K','A','F'],['O','Q','O','M','O'],['R','O','I','E','L'],['R','A','F','Y','G']]
# dl = [4,0]
# dw = [0,1]

row = 0
col = 0
lineCounter=0
words=[]
for lined in lines:
    lineCounter+=1
    line = lined[:-1]
    word = ''
    flag=False
    for r in board:
        for c in r:
            if line.startswith(c):
                counting = True
                wordPos = 1
                word+=c
                ro = row
                co = col
                path = []
                path.append([row,col])
                while counting:
                    if word==line or len(word)>len(line):
                        break
                    adjPos = getNearest(ro,co) 
                    if not any(pos[0]==line[wordPos] for pos in adjPos) or flag==True:
                        break
                    flag=True
                    for pos in adjPos:
                        if pos[0]==line[wordPos] and (pos[1][0]!=ro or pos[1][1]!=co) and not any([pos[1][0],pos[1][1]]==i for i in path):
                            ro = pos[1][0]
                            co = pos[1][1]
                            path.append([ro,co])
                            word+=pos[0]
                            wordPos+=1
                            flag=False
                            break
                if word==line:
                    score = 0
                    letter = 0
                    for l in word:
                        if dl==path[letter]:
                            score+=letters[l]*dlv
                        else:
                            score+=letters[l]
                        letter+=1
                    if dw in path:
                        score*=2
                    if len(word)>5:
                        score+=10
                    words.append([word,score,path])
                d = False
                word = ''
                if lineCounter%100==0:
                    print(str(round(lineCounter/279496*100,3)) + "%")
            col+=1
        row+=1
        col = 0
    row = 0
    col = 0
words.sort(key=lambda x: x[1],reverse=False)
for word in words:
    print(word)
w = input('input word given: ')
c = 1
words.sort(key=lambda x: x[1],reverse=True)
for word in words:
    print(word)
    if w==word[0]:
        print(word[0] + " Is the " + str(c) + "th best word.")
        break
    c+=1
