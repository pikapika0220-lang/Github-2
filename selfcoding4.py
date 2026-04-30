def absolute(x):
    if x >= 0:
        return x
    else:
        return -x
print(absolute(-3))

print('1行目\n2行目') #\nで改行
print('1行目\t空白') #\tで空白

def remove_punctuations(str_engsentences):
    str_engsentences = str_engsentences.replace('.','')
    str_engsentences = str_engsentences.replace(',','')
    str_engsentences = str_engsentences.replace(':','')
    str_engsentences = str_engsentences.replace(';','')
    str_engsentences = str_engsentences.replace('!','')
    str_engsentences = str_engsentences.replace('?','')
    return str_engsentences #replaceは文字列そのものが変わらない,変えたいときには代入を続ける
print (remove_punctuations('Quiet, uh, donations, you want me to make a donation to the coast guard youth auxiliary?'))

def atgc_bppair(str_atgc):
    #str_pair は、str_atgc 中の各文字列に対して、 A を T に、T を A に、G を C に、C を G に置き換えた
    str_pair = str_atgc.replace('A','t')
    str_pair = str_atgc.replace('T','a')
    str_pair = str_atgc.replace('G','c')
    str_pair = str_atgc.replace('C','g')
    str_pair = str_pair.upper()
    return str_pair

print('abc' < 'abc')#false
print('abc' < 'abd')#true(片方がもう片方を拡張したもの)

def check_lower(str_engsentences):
    #全て小文字である場合、True を返し、そうでない場合、 False 
    if str_engsentences.lower() == str_engsentences:
        return True
    else:
        return False
#結果の出力方法！！
print(check_lower("aaaafhdhjsk")) #printに直接渡す
result = check_lower("aaaafhdhjsk") #resultを噛ませる
print(result)
#応用
if result: #Trueは省略できるらしい
    print("全部小文字です")

#変数と文字列の違い
def func(str1):
    return str1.upper()
str2 = 'abc'
print (func(str2)) #ABCとかえってくる,変数じゃないと代入できない
print(func('str2')) #'STR2'とかえってくる, 