list1 = ['apple', 'banana', 'orange']

for i, value in enumerate(list1): #indexと要素を同時に取り出すコマンド
    print(i,value)

dic1 = {'cat': 3, 'dog': 3, 'elephant': 8}
for key in dic1: #dic1.keys()扱いになる
    print(key)

for value in dic1.values():
    print(value) #valueを取り出したい時

for key, value in dic1.items():
    print(key, value) #両方同時に取り出せるぜ

def reverse_lookup2(dic1):
    new_dic = {}
    for key2 in dic1:
        new_dic[dic1[key2]]= key2 #リストと値を入れ替える
    return new_dic

#1から10までの偶数を足す
s = 0
for i in range(2,11,2) :
    s = s + i 
print(s)

#復習
def construct_list(int_size):
    new_list = []
    for i in  range(int_size):
        new_list.append(i)
    return new_list
print(construct_list(10))


def sum_matrix(list1, list2):
    list3 = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3): #行(rangeは0から数える）
        for j in range(3): #列 行列と考えると入れ子構造はわかりやすい
            list3[i][j] =  list1[i][j] + list2[i][j]
    return list3


words = ['apple', 'banana', 'orange']
for i,w in enumerate(words): #iはインデックス(何番目か),wはリストの要素を表す
    print(i, w) 

#str2 を含む場合、 その部分文字列が開始される str1 のインデックスを返値として返してください。 str2 を含まない場合、 -1 
def simple_match(str1, str2):
    if str2 in str1:
        return str1.index(str2) #はりまりの場所？
    else:
        return -1
print(simple_match('location', 'cat'))

#continueぶん
colors = ['red', 'green', 'blue', 'black', 'white']
for c in colors:
    if c == 'black':
        continue #c == blackの場合だけ飛ばして実行
    print(c)


#引数の中の3文字以上の英単語を返す
def collect_engwords(str_engsentence):
    voc = []
    for p in ['.', ',', '!', '?', ';', ':']:
        str_engsentence = str_engsentence.replace(p, '')
    new_str  = str_engsentence.split()
    for i in new_str:
        if len(i) >= 3:
            voc.append(i)
    return voc
print(collect_engwords('Unfortunately no, it requires something with a little more kick, plutonium.') )

#奇数インデックス(最初の項は0)の要素を入れ替えて,タプルに
# ln1[::2]
def swap_lists(ln1, ln2):
    for i in range(1, len(ln1), 2): #rangeは(1,3,2)のような形で書く
        ln1[i], ln2[i] = ln2[i],ln1[i] #入れ替える時は a, b = b, a
    return tuple(ln1),tuple(ln2) #tupleは組み込み関数
print(swap_lists([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e']))

#大文字の数をカウント
def count_capitalletters(str1):
    str2 = str1.lower()
    count = 0
    for i in range(len(str1)): #i番目を比べたい、変えたい-> range()
# for i in str1: だとiが文字になってしまい,str1[i]が文字じゃなくなる(str2[i]) の部分がかけない
        if str1[i] != str2[i]:
            count += 1
    return count
print(count_capitalletters('Que Será, Será'))

#3の倍数の文字列を3ずつに区切り、リスト化
def identify_codons(str_augc):
    str1 = []
    for i in range(0,len(str_augc),3):
        str1.append(str_augc[i:i+3])
    return str1
print(identify_codons('CCCCCGGCACCT'))

#
def sum_strings(list1):
    str1 = ''
    for i in range(len(list1)):
        if i < len(list1) - 2:
            str1 = str1 + str(list1[i]) + ', ' #お尻に,を付け加えている
        elif i == len(list1) - 2:
            str1 = str1 + str(list1[i]) + ' and '
        else:
            str1 = str1 + str(list1[i])
    return str1
print(sum_strings([1, 2, 3]))

def handle_collision2(dic1, str1):
#登録されていない場合 n = len(str1)
    if len(str1) not in dic1.keys():
        dic1[len(str1)] = str1
#登録されている場合
    else:
        while len(str1)+1 < i < 10 :
            if i not in dic1.keys():
                dic1[i] = str1
        while i > 10:
            dic1[i-10] = str1
# これでも登録できない場合
