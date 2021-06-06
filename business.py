import re
from typing import DefaultDict
import pandas as pd


# pd.set_option('display.max_rows', 5862)
# pd.set_option('display.max_columns', 6)
df = pd.read_csv('sample.csv')
#正規表現で数字と記号を削除
#無名関数で式組み立ててます。
drop_index = df.index[df['col2'].apply(lambda y: re.search(r'[0-9|(?<=\().+?(?=\))♪★]', y) != None)]
#条件にマッチしたIndexを削除
df = df.drop(drop_index)
#行の合計を計算し新しい列に追加
df = pd.concat([df,pd.DataFrame(df.sum(axis=1),columns=['Total'])],axis=1)
df_s = df.sort_values('Total', ascending=False)
#表示する行を指定 
#この場合は3行目まで出る
print(df_s[1:4])

