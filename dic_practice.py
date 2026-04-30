#リスト list1 が引数として与えられたとき、list1 の各要素 value をキー、value の list1 におけるインデックスをキーに対応する値とした辞書を返す関数 reverse_lookup を作成してください。
#index→この要素はリストの何番目にあるか
def reverse_lookup(list1):
    dic = {} #空の辞書を用意
    for value in list1:
        dic[list1.index(value)] = value #keyもvalueも同時に追加される, dic[辞書の値],indexはリストの中で指定した要素が何番目か
    return dic
print(reverse_lookup(['apple', 'pen', 'orange']))

#valueはリストでも可
d = {
    'fruits': ['apple', 'banana', 'orange'],
    'numbers': [1, 2, 3]
}

print(d['fruits'])  # → ['apple', 'banana', 'orange']

#keyは文字列じゃなくても可でも、変更不可の時のみ使用！
d = {
    1: 'one',       # 整数
    'name': '豊増',  # 文字列
    (1, 2): 'tuple' # タプル
}

def handle_collision(dic1, str1):
    value = len(str1)
    if value in dic1:
        dic1[value].append(str1) #valueに文字列を追加する,listじゃないと登録できない
    else:
        dic1[value] = [str1] #同時追加(訳;辞書のvalue(今回は数字じゃない方)=文字列をリストとして登録)
    return dic1

dic1_orig = {3: ['ham', 'egg'], 6: ['coffee', 'brandy'], 9: ['port wine'], 15: ['curried chicken']}
print(handle_collision(dic1_orig,'tea'))

#list.append() .がついてる → そのデータ型専用
#len()  .がない → 組み込み関数、色々使える
#リストに何かしたい → list.xxx()を調べる
#文字列に何かしたい → str.xxx()を調べる

#辞書復習

dic = {'name': '豊増', 'age': 22, 'city': '大阪'}
print(dic['age']) #22を取り出す
print(dic.keys()) #keyの一覧
print(dic.values()) #値一覧


