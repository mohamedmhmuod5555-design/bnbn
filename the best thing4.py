import random
import streamlit as st

# تهيئة المتغيرات في الجلسة (Session State)
if 'ran' not in st.session_state or st.session_state.ran < 1:
    st.session_state.ran = 20
if 'level' not in st.session_state:
    st.session_state.level = 1
if 'num' not in st.session_state:
    st.session_state.num = 0
if 'count' not in st.session_state:
    st.session_state.count = 0

# توليد مسألة جديدة إذا لم تكن موجودة
if 'num1' not in st.session_state:
    st.session_state.num1 = random.randint(1, st.session_state.session_state.ran if 'ran' in st.session_state else 20)
    # تعديل بسيط لضمان اختيار أرقام تقبل القسمة بدون فواصل صعبة
    st.session_state.sign = random.choice(['+', '-', '*', '/'])
    
    if st.session_state.sign == '/':
        # لضمان قسمة صحيحة سهلة وبدون أرقام عشرية معقدة
        st.session_state.num2 = random.randint(1, 10)
        st.session_state.num1 = st.session_state.num2 * random.randint(1, 10)
    else:
        st.session_state.num2 = random.randint(1, st.session_state.ran)

num1 = st.session_state.num1
num2 = st.session_state.num2
sign = st.session_state.sign

# حساب الإجابة الصحيحة
if sign == '+': sc = num1 + num2
elif sign == '-': sc = num1 - num2
elif sign == '*': sc = num1 * num2
elif sign == '/': sc = int(num1 / num2) # تحويل لعدد صحيح لتسهيل الإدخال

st.title("Welcome to Mohamed's game 🎮")
st.write(f"### المستوي الحالي: {st.session_state.level}")
st.write(f"## {num1} {sign} {num2} = ؟")

# حقل إدخال النتيجة
number = st.number_input("ادخل النتيجه", value=0, step=1)

# زر تأكيد التخمين
if st.button("تأكيد التخمين 🎯"):
    st.session_state.count += 1
    
    if number == sc:
        st.success("اجابتك صحيحه انك اسطورة! 🎉")
        st.session_state.num += 1
    else:
        st.error(f"اجابتك خاطئة! الإجابة الصحيحة كانت: {sc} ❌")
        st.session_state.num = 0  # تصفير الـ streak عند الخطأ حسب كودك الأصلي
    
    # حذف السؤال الحالي ليتم توليد سؤال جديد في التحديث القادم
    del st.session_state.num1
    del st.session_state.num2
    del st.session_state.sign
    
    # زر جانبي يظهر للمتابعة وتحديث الشاشة للسؤال الجديد
    st.button("السؤال التالي ➡️")

# إظهار رسالة التحدي البطل إذا وصل لـ 10 إجابات متتالية
if st.session_state.num > 0 and st.session_state.num % 10 == 0:
    st.success("أنت بطل! تحدى صديقك، فبالتأكيد لن يستطيع الوصول لمستواك! 🏆")

# عرض النقاط الحالية
st.write(f"نقاطك الحالية المستمرة: {st.session_state.num}")
st.write(f"إجمالي الأسئلة المجابة: {st.session_state.count}")

# زر الانتقال للمستوى التالي
st.write("---")
if st.button("الليفل التالي 🚀"):
    st.session_state.level += 1
    st.session_state.ran += 20
    st.session_state.count = 0
    st.session_state.num = 0
    if 'num1' in st.session_state: del st.session_state.num1
    if 'num2' in st.session_state: del st.session_state.num2
    if 'sign' in st.session_state: del st.session_state.sign
    st.rerun()
