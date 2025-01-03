import streamlit as st
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score
from sklearn.metrics import f1_score, confusion_matrix, precision_recall_curve, classification_report
from sklearn.preprocessing import StandardScaler, Binarizer
from sklearn.linear_model import LogisticRegression

st.set_page_config(page_title='page3', page_icon='3️⃣')
st.sidebar.header('3️⃣머신러닝 보고서')




df = pd.read_csv('diabetes.csv')
st.header("당뇨병 머신러닝 보고서")
st.subheader('데이터보기')
st.write(df)

# 값이0인것들 평균값으로 대체
zero_features = ['Glucose', 'BloodPressure','SkinThickness','Insulin','BMI']
df[zero_features]=df[zero_features].replace(0, df[zero_features].mean())

# 맨 끝이 Outcome 칼럼으로 레이블 값임, 칼럼 위치 -1을 이용해 추출
X = df.drop('Outcome', axis =1)
y = df.Outcome

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model= LogisticRegression()          
# 학습하기
model.fit(X_train, y_train)


# 로지스틱 회귀로 학습, 예측, 평가 
lr_clf = LogisticRegression()
lr_clf.fit(X_train, y_train)
pred = lr_clf.predict(X_test)


# 정확도
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, pred)
st.write(f'Accuracy: {accuracy:.2f}')


# Rapport de classification
st.write(classification_report(y_test,pred))

# 상관계수 구하기
colormap = plt.cm.gist_heat   #그래프의 색상 구성을 정합니다

fig=plt.figure(figsize=(15,8))

sns.heatmap(df.corr(),linewidths=0.1,vmax=0.5, cmap=colormap, linecolor='white', annot=True)

st.pyplot(fig)