def exception3(x,y,z):
    if x == y:
        return z
    elif x == z: #上のif文が違うかつ次の文が真の時に動く
            return y
    else:
        return x
print(exception3(2,2,4))

def exception9(a):
    for value in a:
        if a.count(value) == 1:
            return value

print(exception9([2, 1, 1, 1, 1, 1, 1, 1, 1]))

for value in range(5): #range(同じ動作を(n)回繰り返す)
    print('Hi!')

