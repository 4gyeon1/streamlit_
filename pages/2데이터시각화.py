import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




st.set_page_config(page_title='page2', page_icon= '2️⃣')
st.sidebar.header('2️⃣ 데이터 시각화')


st.header('데이터 개요',divider='rainbow')

st.markdown('''

''')
st.subheader('연관성 파악을 위한 시각화')
df= pd.read_csv('diabetes.csv')
t1,t2,t3,t4,t5,t6,t7,t8=st.tabs(['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age'])

# 값이0인것들 평균값으로 대체
zero_features = ['Glucose', 'BloodPressure','SkinThickness','Insulin','BMI']
df[zero_features]=df[zero_features].replace(0, df[zero_features].mean())

with t1:
    fig=plt.figure(figsize=(20,8))
    st.header('Pregnancies 히스토그램')
    sns.countplot(data=df, x='Pregnancies',hue='Outcome')
    st.pyplot(fig)

with t2:
    st.header('Glucose 히스토그램')
    fig=plt.figure(figsize=(20,10))
    sns.histplot(data=df, x='Glucose',hue='Outcome')
    st.pyplot(fig)

with t3:
    st.header('BloodPressure')
    fig=plt.figure(figsize=(20,10))
    sns.boxplot(data=df, x='BloodPressure',hue='Outcome')
    st.pyplot(fig)

with t4:
    st.header('SkinThickness 히스토그램')
    fig=plt.figure(figsize=(20,10))
    sns.histplot(data=df, x='SkinThickness',hue='Outcome')
    st.pyplot(fig)

with t5:
    st.header('Insulin 히스토그램')
    fig=plt.figure(figsize=(20,10))
    sns.scatterplot(data=df, x='Insulin',y='Outcome')
    st.pyplot(fig)

with t6:
    st.header('BMI 히스토그램')
    fig=plt.figure(figsize=(20,10))
    sns.histplot(data=df, x='BMI',hue='Outcome')
    st.pyplot(fig)


with t7:
    st.header('DiabetesPedigreeFunction 히스토그램')
    fig=plt.figure(figsize=(20,10))
    sns.barplot(data=df, x='DiabetesPedigreeFunction',hue='Outcome')
    st.pyplot(fig)


with t8:
    st.header('Age 히스토그램')
    fig=plt.figure(figsize=(20,10))
    sns.countplot(data=df, x='Age',hue='Outcome')
    st.pyplot(fig)





# st.subheader("Pregnancies 히스토그램")
# fig=plt.figure(figsize=(10,5))
# sns.histplot(x='Pregnancies',data=df,hue='Outcome',kde=True)
# st.pyplot(fig)
# st.subheader("Outcome BloodPressure Boxplot")
# fig=plt.figure(figsize=(10,5))
# sns.boxplot(x='Outcome',y='BloodPressure', data=df)
# st.pyplot(fig)
# st.subheader("Glucose Insulin Scatter")
# fig=plt.figure(figsize=(10,4))
# sns.scatterplot(x='Glucose', y='Insulin' ,hue='Outcome', data=df)
# st.pyplot(fig)