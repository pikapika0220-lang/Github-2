from sklearn.linear_model import LogisticRegression #教師あり学習としてまず初めにデータを学習させるクラス
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

iris = load_iris()
X_iris = iris.data #データ自体の取得
y_iris = iris.target #ラベルの取得

#データをランダムにtest=30%として分ける。(stratify)-きちんと30%になるように
X_train, X_test, y_train, y_test = train_test_split(X_iris, y_iris, test_size=0.3, random_state=1, stratify=y_iris)

model = LogisticRegression(solver='lbfgs') #class, 引数の部分はおまじない

model.fit(X_train,y_train) #教師ありとしてデータを学習させるメソッド(クラスの中にfitっていう関数がある)
#modelにパターンが保存される

y_predicted = model.predict(X_test) #学習結果で予測するメソッド(クラスの中にpredictっていう関数がある)
#ここでy_predictedにX_testに対応するラベルが入る

#小文字始まりの関数を呼び出す
print(accuracy_score(y_test, y_predicted)) #ここで正答率を出す


#教師なしversion
import pandas as pd
from sklearn.cluster import KMeans

iris = pd.read_csv('iris.csv')
X_iris=iris[['petal_length', 'petal_width']].values

model = KMeans(n_clusters=3) # k-meansモデル
model.fit(X_iris) # モデルをデータに適合,答えがないから勝手にグループ分けする
y_km=model.predict(X_iris) # 各データがどこに位置するか

iris['cluster']=y_km
iris.plot.scatter(x='petal_length', y='petal_width', c='cluster', colormap='viridis')