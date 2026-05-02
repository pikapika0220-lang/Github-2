# Python辞書まとめ
### mdは#大見出し,##中見出し,###小見出しで使う
### - 箇条書き,'コード',

## 基本操作
- 空の辞書を作る: `dic = {}`
- 値を追加: `dic['key'] = value`
- 値を取得: `dic['key']`

## よく使うメソッド
- キー一覧: `dic.keys()`
- 値一覧: `dic.values()`
- キーの存在確認: `key in dic`

## 変数の定石
- i,j,k(ループの際)
- x,y,z (座標,数値)

## 意味あるへんすう
- user_name    # スネークケース（単語を_で繋ぐ）
- is_valid     # True/Falseの変数はis_で始める

## 辞書、リスト
- A_dic, B_list

## 用語
- continue(そのループだけ飛ばして次のループへ)
- break(そうなった瞬間にるループをやめる)
- pass文一旦スルーするの意味(後で実装する文に関して有効に使える)

## dockerで使えるコマンド
- 環境をまるごと箱に入れて管理するツール
- docker start sql-practice(①Dockerコンテナ起動)
- docker exec -it sql-practice mysql -u root -ppassword(mysqlの起動)
- USE mydb; (データベースの選択)
- SELECT 
- INSERT, INSERT INTO users  (name,   age)  VALUES ('Honda', 20);(20歳のホンダを登録する時)
- WHERE, SELECT * FROM users WHERE age >= 25; (全てから年齢が25歳以上の人を抽出)
- UPDATE, UPDATE users SET age = 23 WHERE name = 'toyomasu';(データ内容の変更,setで変更する内容、nameで誰を変更するのか) 
- DELETE, DELETE FROM users WHERE name = 'Honda';
- SHOW TABLES;(テーブルの中身の名前一覧を見る)
- SELECT * from users; 名前を指定しその中身を見る
- ユーザーが「Katoのツイート見たい」->裏でこのSQLが動く SELECT * FROM tweets WHERE user_id = 7; ->Katoのツイートだけ表示！
- 欠損値の判定 → isna(), 欠損値の削除 → dropna(), 欠損値を埋める → fillna()