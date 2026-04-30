def remove_evenindex(ln):
    return ln[1::2] #偶数番目の削除

lns = [[1, 2, 3], [10, 20, 30], ['a', 'b', 'c']]
print(lns[1][0]) #10

numbers = [30, 50, 10, 20, 40, 60]
numbers.sort()
print('sortメソッドの実行後の元のリスト:', numbers) #[10, 20, 30, 40, 50, 60]→破壊する
numbers = [30, 50, 10, 20, 40, 60]
sorted(numbers)
print('sorted関数の実行後の元のリスト:', numbers) #[30, 50, 10, 20, 40, 60]→破壊しない

#listの数え方
list = [1, 2, [3, 4, 5]]
len(list)  # → 3

#popの使いかた
list = [1, 2, 3, 4, 5]
list.pop()  # → 5が取り出される
print(list) # → [1, 2, 3, 4]


def change_domain(email, domain):
    leftemail = email.split('@')
    return leftemail[0] + '@' + domain
print(change_domain('spam@utokyo-ipp.org', 'ipp.u-tokyo.ac.jp'))
#僕の回答def change_domain(email, domain):
    #newemail.append(leftemail[0],domain) appendは一つしか引数取らない
    #return newemail.split(',') リストにsplitは使えない

def reverse_totuple(ln):
    return tuple(ln[::-1])#[::-1]は「全要素を逆順に取り出す」スライス
#もしくは
# ln.reverse() reverseは破壊的であるためln自体が変わってくれる
# return tuple(ln)

#オブジェクト同一性
'''a == b の場合
a → [1, 2, 3]
b → [1, 2, 3]  ← 別々の箱だけど中身が同じ

a is b の場合
a → [1, 2, 3]
b ↗            ← 同じ箱を指してる'''