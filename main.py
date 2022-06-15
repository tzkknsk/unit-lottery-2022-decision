import streamlit as st
from PIL import Image
import random
import pandas as pd

st.header("【第１部―２】　各問題の色の決定")

buttom = st.button('決定')
st.subheader("")

dic = {} 

if buttom:
    for i in range(1, 145):
        color_id = random.randint(0, 1)

        if color_id == 0:
            color = "緑"
            color_en = "Green"
        else:
            color = "赤"
            color_en = "Red"
        
        st.subheader(f"【NO. {i} 】")
        st.subheader(color)
        st.subheader("")

        dic[i] = color_en



## ---------- 回答結果の出力 ---------- ##

def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')

output_dict={}
for k,v in dic.items():   # 一度pd.Seriesに変換
    output_dict[k]=pd.Series(v)

df = pd.DataFrame(output_dict)

def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv(index=False).encode('utf-8')

csv = convert_df(df)

st.download_button(
     label="結果を出力(csv)",
     data=csv,
     file_name= f'UnitLottery_ColorDecision.csv',
     mime='text/csv',
 )
