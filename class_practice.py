#データと処理と同時に行うために必要
# 1. クラスの定義
#class クラス名:

# 2. 初期設定
#def __init__(self, 引数):
    #self.変数 = 引数

# 3. メソッドの定義
#def メソッド名(self):
#処理

# 4. インスタンスの作成
#インスタンス = クラス名(引数)

# 5. メソッドの呼び出し
#インスタンス.メソッド名()

# 6. 継承
#class 子クラス(親クラス):

# 7. 親クラスのメソッドを呼び出す
#super().メソッド名()

class Helloforever:
    def readline(self):
        return 'Good morning.\n'
f = Helloforever()
print(f.readline())

class Hellofile:
#初期値設定みたいなもの
    def __init__(self,n): #インスタンス(実際に出力した時に)を作った時に最初に実行される
        self.n = n #nを代入する意味
    def readline(self):
        if self.n == 0:
            return ''
        self.n = self.n - 1
        return 'Hello.\n'
f = Hellofile(3)
for i in range(4):
    print(f.readline())
#4回やるとようやく''が帰る

class Hellofile(Helloforever):
    def __init__(self, n):
        self.n = n
    def readline(self):
        if self.n == 0:
            return ''
        self.n = self.n - 1
        return super().readline() #Helloforeverを実行することになる
f = Hellofile(3)
for i in range(4):
    print(f.readline()) #出力方法は上と同じ

class HelloFileIterator(Hellofile):
    def __iter__(self):
        return self
    def __next__(self):
        line = self.readline()
        if line == '':
            raise StopIteration
        return line

class StringFileIterator(HelloFileIterator):
    def __init__(self, s , n):
        self.s = s
        self.n = n
    def readline(self):
        if self.n == 0:
            return ''
        self.n = self.n - 1
        return self.s #Helloforeverを実行することになる
f = StringFileIterator('abc', 3)
print(list(f)) #list(f)とすることによって一気にabcを3つ取り出せる