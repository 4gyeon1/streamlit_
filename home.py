import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='Home',page_icon='🏥')

df=pd.read_csv('diabetes.csv')
st.sidebar.title('Home')

st.write("# 당뇨병 데이터 웹앱 ")

st.header("당뇨병 데이터 개요",divider='rainbow')

df= pd.read_csv('diabetes.csv')
st.markdown('''
kaggle 데이터 분석. diabetes.csv 데이터 참조.

이 데이터 세트는 원래 National Institute of Diabetes and Digestive and Kidney Diseases에서 가져왔습니다. 목표는 진단 측정을 기반으로 환자가 당뇨병을 앓고 있는지 예측하는 것입니다.

모든 환자는 피마 인디언 유전자을 가진 21세 이상의 여성입니다.
            
피마 인디언은 애리조나 사막지역 원주민으로, 세계에서 당뇨병 발병률이 가장 높은 종족으로 알려져 있습니다. 피마 인디언은 비만, 인슐린 저항성, 인슐린 분비 기능 장애, 내인성 포도당 생성 속도 증가와 같은 당뇨병의 임상적 특징을 보입니다.
            

임신횟수, 포도당 부하 검사 수치, 혈압, 팔 삼두근 뒤쪽의 피하지방 측정값, 혈청 인슐린, 체질량 지수, 당뇨 내력 가중치 값, 나이와 같은 피처로 구성되어 있습니다.
            
''')

col1,col2,col3=st.columns([4,4,4])
with col1:
    st.subheader('')
    st.image('d1.png')
with col2:
    st.subheader('')
    st.image('d2.png')
with col3:
    st.subheader('')
    st.image('d3.png')