h = 169
w = 62
w = w - 3#右辺を評価した後に左辺に割り当てる
print(w/(h/100)**2)

def bmi(height,weight):
    return weight/(height/100)**2 #return に続く式の評価結果を、関数の呼び出し元に返して（これを返値と言います）、関数を終了する,
height = float(input("身長")) #""はプロンプト文字列(親切のため),実際は入力文字列をうけとる
weight = float(input("体重")) #""と’’の違いは特になし
print(f'bmi:{bmi(height,weight)}')