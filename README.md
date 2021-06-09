# business-py
CSVファイル処理



※任意で弄る箇所だけ抜粋しております

手順:1<br>
任意のcsvファイルを読み込ませてください<br>
df = pd.read_csv('任意のCSVファイル')

手順:2<br>
Grcで取得したものでエクセルのBの列に自動的に生成させる'Unnamed 0'の名前を'id'に変更しております。
この'id'は任意で名前を変更して大丈夫です。<br><br>
df = df.rename(columns={'Unnamed: 0':'id'})<br><br>
※macでwindowsのcsvを表示した際に'Unnamed 0'が二つ出力されたため名前を変更する
コードを追加いたしました。

手順：3<br>
ここでは行の合計を計算し降順に並べ、新しい列を作成し格納しています。<br>
新しく追加する列の名前は任意で決めてください。<br>

df = pd.concat([df,pd.DataFrame(df.sum(axis=1),columns=['任意で決めてください。'])],axis=1)<br>
df_s = df.sort_values('任意で決めたものと同じになるように', ascending=False)

<降順を解除したい場合><br>
ascending=False を使い降順にしているので昇順に戻したい場合は記述しないか　FalseをTrueに変更してください



手順：4
ここでは何行表示するか決めています。<br>
今回の出力では3行数目まで出力するようにしております。<br>
print(df_s[1:4])

例えば10行数表示したい場合<br>
print(df_s[1:11])にしてください。

