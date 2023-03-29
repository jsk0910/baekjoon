
N = int(input())

resultList = []

def hanoi(n, from_position, to_position, aux_position):
    if n == 1:
        resultList.append([from_position, to_position])
        return
    
    hanoi(n - 1, from_position, aux_position, to_position)
    resultList.append([from_position, to_position])
    hanoi(n - 1, aux_position, to_position, from_position)

hanoi(N, 1, 3, 2)
print(len(resultList))
for i in resultList:
    print(i[0], i[1])
