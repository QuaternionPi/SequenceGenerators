import time
count = 1
ledger = []
while count < 1002:
    List = []
    count += 2
    runtotal = count
    List.append(count)
    while runtotal>1 and runtotal not in ledger:
        runtotal2 = runtotal
        if runtotal% 2 == 0:
            runtotal = int(runtotal/2)
        elif runtotal% 2 == 1:
            runtotal = runtotal*3+1
        else:
            runtotal = 0
        ledger.append(runtotal2)
        List.append(runtotal)
    if len (List) != 1:
        print (List)
print (max(ledger))
input()
