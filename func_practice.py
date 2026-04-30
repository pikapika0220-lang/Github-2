def last_line(name):
    last = ''
    with open(name, 'r') as f: #withを用いれば自動的にcloseされる
        while True:
            line = f.readline()
            if line == '':
                return last #終わる時だけlast行を返す(''は最後の行に到達しないのでその前のlastが出力される)
            last = line #return でおわんなかった時にそのループに対応する行を入れる

#ファイルの文字数を返す
def  number_of_characters(name):
    f = open(name, 'r')
    s = f.read()
    f.close()
    return len(s)

def file_upper(infile,outfile):
    with open(infile,'r') as f:
        with open(outfile, 'w') as g: #withは1行でまとめることも可能
            g.write(f.read().upper())


from math import sqrt, sin, pi
print(sin(pi)) #fromから書くことにより、math.とかを書く必要がなくなる