import random
import streamlit as st
if 'ran' not in st.session_state or st.session_state.ran < 1:
  st.session_state.ran=20
if 'level' not in st.session_state:
  st.session_state.level=1
if 'num' not in st.session_state:
  st.session_state.num=0
if 'sc' not in st.session_state:
  st.session_state.sc=0
if 'count' not in st.session_state:
  st.session_state.count=0
if 'num1' not in st.session_state:
 st.session_state.num1=random.randint(1,st.session_state.ran)
if 'num2' not in st.session_state:
 st.session_state.num2=random.randint(1,st.session_state.ran)
if 'sign' not in st.session_state:
 st.session_state.sign=random.choice(['+','-','*','/'])
if "feed " not in st.session_state:
  st.session_state.feed = 0
if "correct" not in st.session_state:
  st.session_state.correct=0


num1 = st.session_state.num1
num2 = st.session_state.num2
sign = st.session_state.sign
if sign=='+':
 sc=num1+num2
if sign=='-':
 sc=num1-num2
if sign=='*':
 sc=num1*num2
if sign=='/':
 sc=num1/num2
st.title("Welcome to Mohamed's game ")
st.write(num1,sign,num2)
number=st.number_input("ادخل النتيجه ")
if st.button("تأكيد التخمين "):
  st.session_state.count += 1
  if number == sc:
    st.session_state.feed="correct"
  else:
    st.session_state.feed="false"
if st.session_state.feed=="correct":
  st.success("اجابتك صحيحه انك اسكوره ")
  st.session_state.num += 1
  
if st.session_state.feed=="false":
   st.error(f"اجابتك خاطئة! الإجابة الصحيحة كانت : {sc}")
   st.session_state.num =0
del st.session_state.num1 
del st.session_state.num2 
del st.session_state.sign 

if st.session_state.num > 0 and st.session_state.num % 10 == 0:
  st.success("انت بطل! تحدي صديقك انه بالطبع لن يستطيع ان يصل لمستواك  ")
  if st.button("الليفل التالي "):
     st.session_state.level+=1
     st.session_state.ran+=20
     del st.session_state.num1
     del st.session_state.num2
     del st.session_state.sign
     st.session_state.count=0
     st.session_state.num=0

st.write("your points are " ,st.session_state.num,"from",st.session_state.count,"Questions" )
st.write("you are in level",st.session_state.level)

