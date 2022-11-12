from multiprocessing.connection import wait
import streamlit as st
import numpy as np
import pandas as pd
import datetime
import os
import base64
import io
import openpyxl

def dt_change(dt):
  return '{:0=4}{:0=2}{:0=2}'.format(dt.year, dt.month, dt.day)
now = datetime.datetime.now()
end = dt_change(now)

def BEFORE14(dt):
  dt1 = f'{dt[0:4]}-{dt[4:6]}-{dt[6:8]}'
  dt1 = datetime.datetime.strptime(dt1, '%Y-%m-%d') + datetime.timedelta(days=1)
  dt2 = dt1 - datetime.timedelta(days=14)
  return dt1, dt2 
  
def dt_change2(dt):
  return '{}/{}'.format(dt.month, dt.day)

def data_shaping(df): 
  # カラムを限定
  df_ = df[["'氏名'", "'日付・時刻'", "'体温(体調情報)'"]]
  
  # カラムの名前を変更
  df_ = df_.rename(columns={"'氏名'":"氏名", 
          "'日付・時刻'":"日付",
          "'体温(体調情報)'":"体温"})
  
  #日付型に変更
  df_['日付'] = pd.to_datetime(df_['日付'])
  # 日付を直近14日に限定
  dt1, dt2 = BEFORE14(end)
  df_ = df_[df_['日付'] <= dt1]
  df_ = df_[df_['日付'] >= dt2] 

  # 日付をわかりやすい形に変換

  f = lambda x: '{:0=2}/{:0=2}'.format(x.month, x.day)
  # f = lambda x: str(x.strftime('%m')) + '/' + str(x.strftime('%d'))
  df_['日付'] = df_['日付'].map(f)

  # 引用符をなくす
  for c in ['氏名', '体温']:
    df_[c] = df_[c].str[1:-1]
      
  return df_.reset_index(drop=True)

def data_merging(df3, df4):
    for i in df4['氏名'].unique():
        if i in df3['氏名'].unique():
            df4 = df4[df4['氏名']!=i]
    return pd.concat([df3, df4])

# メンバー一覧：省略しています
# OND’Uに登録しているのと同じ名前にする
# 1年生：
# 1年生：
year1 =[
'苗字 一郎'
'苗字 二郎'
'苗字 三郎'
'苗字 四郎'
'苗字 五郎'
]
# 2年生:
year2 = ['苗字 六郎']
# 3年生:
year3 = ['苗字 七郎']
# 4年生 
year4 = ['苗字 八郎']
# 院生
grad = ['苗字 九郎']
# 社会人さん
social = ['苗字 十郎']

members = year1+year2+year3+year4+grad+social

#名前×日付データ
def name_day(df, members=members):  
  # 日付一覧
  days = sorted([d for d in df['日付'].unique()])

  A = pd.DataFrame(index=members, columns=days)
  A.insert(0, '未記録数','0')
  A.insert(0, '属性','')
  
  # 37.5度以上あったら★を付ける
  # f = lambda x: '★'+str(x)  if float(x) > 37.4 else x
  for m in members:
    df_m = df[df['氏名']==m].reset_index(drop=True)
    for i in range(len(df_m)):
      x = df_m.at[i,'体温']
      if float(x) > 37.4:
        df_m.at[i, '体温'] = '★'+str(x)

    n = 0
    for d in days:
      day_data = df_m[df_m['日付']==d]

      # 一日に複数回入れている場合を削除
      if len(day_data) > 1:
        day_data = day_data.iloc[-1:]
      
      if day_data.empty is False:
        A.loc[m][d] = day_data.iloc[0]['体温']
        n += 1

    # 未記録数
    A.at[m, '未記録数'] = 14-n

    # 属性
    if   m in year1: A.at[m, '属性'] = '1年'
    elif m in year2: A.at[m, '属性'] = '2年'
    elif m in year3: A.at[m, '属性'] = '3年'
    elif m in year4: A.at[m, '属性'] = '4年'
    elif m in grad : A.at[m, '属性'] = '院生'
    else:            A.at[m, '属性'] = '社会人' 

  return A

# attribute(属性)...1個目は業務用、2個目は少し丁寧な言い方(見せる用)
atts = ['1年', '2年', '3年', '4年', '院生', '社会人']
atts_ = ['1年生', '2年生', '3年生', '4年生', '院生', '社会人さん']

zero = []
def attr(i):
  a = atts[i]
  a_ = atts_[i]
  B2 = B[B['属性']==a]
  lst1 = []
  lst2 = []
  for i in B2.index:
    if B2.at[i, '未記録数'] == 0:
      lst1.append(i)
    elif B2.at[i, '未記録数'] == 14:
      zero.append(i)
    else: 
      b = B2.at[i, '未記録数']
      lst2.append(f'{i}({b})')

  txt1 = f"【{a_}({len(lst1)})】{', '.join(lst1)}"
  txt2 = f"【{a_}({len(lst2)})】{', '.join(lst2)}"
  
  if len(lst1) == len(B2):
    txt1 = f"【{a_} 全員】"

  return txt1, txt2

def text1():
  for txt in can:
    st.write(txt)
  st.write()
  st.write('今日の名簿です。検温の記入漏れ等ありましたらご連絡ください。')

def text2():
  # st.write('出してない人リスト')
  st.write()
  for txt in cant:
    st.write(txt)
  st.write()
  st.write('【2週間1回も出していない人リスト】')
  st.write(', '.join(zero))

def download():
  towrite = io.BytesIO()
  downloaded_file = A.to_excel(towrite, encoding='utf-8', index=True, header=True) # write to BytesIO buffer
  towrite.seek(0)  # reset pointer
  b64 = base64.b64encode(towrite.read()).decode() 
  linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="斬桐舞体温記録_{end}.xlsx">ファイルをダウンロード</a>'
  st.markdown(linko, unsafe_allow_html=True)     



# MAIN
st.title("OND'U管理")
if st.checkbox('日付を入力する(自動でうまくいかないとき)'):
  end = st.text_input('今日の日付を入力して下さい (例：20211107)')
"※日付の変更はファイルアップロード前に行ってください"

"ファイルをアップロードしてください"
file1 = st.file_uploader("【学生支部】", type='csv') 
wait = 1
file2 = st.file_uploader("【社会人支部】", type='csv') 



if file1 is not None:
    if file2 is not None:
        "ファイルのアップロードが完了しました"
        st.write('-'*50)
        st.write('しばらくお待ちください')
        bar = st.progress(0) 
        df1 = pd.read_csv(file1)
        df2 = pd.read_csv(file2)
        df3 = data_shaping(df1)
        df4 = data_shaping(df2)
        df5 = data_merging(df3, df4)
        bar.progress(50)
        A = name_day(df5, members=members)

        B = A.iloc[:, :2]
        y1, y1_ = attr(0)
        y2, y2_ = attr(1)
        y3, y3_ = attr(2)
        y4, y4_ = attr(3)
        gr, gr_ = attr(4)
        so, so_ = attr(5)
        can  = [y1, y2, y3, y4, gr, so]
        cant = [y1_, y2_, y3_, y4_, gr_, so_]

        st.write('-'*50)
        text1()
        st.write('-'*50)
        bar.progress(100)

        if st.checkbox('出してない人リストを表示する'):
          text2()
        st.write('-'*50)

        button = st.button('Excelデータを出力する')
        if button:
          download()
          st.write('ファイルの出力が完了しました')

        

