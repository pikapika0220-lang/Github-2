
squares = [x**2 for x in range(6) ]
print(squares)
#以下と同じ
#squares = []
#for x in range(6)
# squares.append(x**2)

print(sum(x**2 for x in range(6))) #sumを使うこともできる
print([chr(i + ord('a')) for i in range(26)])

str1 = '123,45,-3'
for x in str1.split(','): #splitは非破壊的や
    print(int(x))

str1 = '123,45,-3'
print([int(x) for x in str1.split(',')]) #[]で囲むことでリストを作るという意味になる

#分散
def var(lst):
    ave = sum(lst)/ len(lst)
    return sum((x - ave)**2 for x in lst)/ len(lst)
print(var([3,4,1,2]))

def sum_lists(list1):
    return sum(sum(i) for i in list1)
print(sum_lists([[20, 5], [6, 16, 14, 5], [16, 8, 16, 17, 14], [1], [5, 3, 5, 7]]))



def sum_matrix(list1, list2):
    list3 = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(list1[i][j] + list2[i][j])
        list3.append(row)
    return list3

print(sum_matrix([[1,5,3],[4,5,6],[7,8,9]], [[1,4,7],[2,5,8],[3,6,9]]))

def sum_matrix(list1, list2):
    list3 = [[list1[i][j]+list2[i][j] for j in range(3)] for i in range(3)]
    return list3