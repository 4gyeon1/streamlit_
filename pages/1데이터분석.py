import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title='page1',page_icon='1️⃣')
st.sidebar.header('1️⃣ 데이터 분석')


st.header('당뇨병 데이터 웹앱',divider='rainbow')
st.markdown("""
                
        - Pregnancies: 임신 횟수
        - Glucose: 포도당 부하 검사 수치
        - BloodPressure: 혈압(nm Hg)
        - SkinThickness: 팔 삼두근 뒤쪽의 피하지방 측정값(nm)
        - Insulin: 혈청 인슐린(mu U/ml)
        - BMI: 체질량지수
        - DiabetesPedigreeFunction: 당뇨 내력 가중치 값
        - Age: 나이
        - Outcome: 당뇨병 여부
""")

df= pd.read_csv('diabetes.csv')

t1,t2,t3,t4,=st.tabs(['상위데이터','데이터 통계','컬럼데이터','조건데이터'])
with t1:
    dh=df.head(10)
    st.write(dh)

with t2:
    dd=df.describe()
    st.write(dd)
    
    zero_features = ['Glucose', 'BloodPressure','SkinThickness','Insulin','BMI']
    df[zero_features]=df[zero_features].replace(0, df[zero_features].mean())
    st.write('🔽 최솟값이 0이 나온 것들을 평균값으로 대체 🔽')
    
    dd=df.describe()
    st.write(dd)


with t3:
    col=df.columns
    scol=st.multiselect('select col',col)
    ldf=df.loc[:,scol]
    st.write(ldf)

with t4:
    c=st.selectbox('select outcome',(0,1))
    cl=df['Outcome']==c
    c_df=df.loc[cl]
    st.write(c_df)


    

