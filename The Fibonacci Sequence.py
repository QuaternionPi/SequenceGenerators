import time
List = []
List.append(0)
List.append(1)
global Listaddition
Listaddition = 0
while List[-1] < 1000000000000000000000000000000000000000000000000000000000000:
    Listaddition = List[-1]+List[-2]
    List.append(Listaddition)
    print(List[-1])
    time.sleep(0.04)
print('(one trillion trillion trillion trillion trillion)')
input()
