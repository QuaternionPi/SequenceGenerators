from math import *
Count = 5
PCount = 0
PLedger = [2,3]
PLedger2 = [2]
PList = []
for Count in range (0,100000):
    if PLedger[-1]!=PLedger2[-1] and sqrt(Count) < PLedger[-1]:
        PLedger2.append(PLedger[-1])
    Length = len(PLedger2)+5
    i = 5
    State = True
    while i <= Length and State == True:
        if Count%i == 0:
            State = False
        if i == Length:
            PLedger.append(Count)
            PCount += 1
        i += 1
    Count += 2
    if PCount == 100:
        PCount -= 100
        PList = PLedger[1:]
        print(PList)
