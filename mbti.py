import streamlit as st
import time

inflobj = open('file.txt', 'r', encoding='utf-8')

data = inflobj.read()
inflobj.close()

st.title("2-6 MBTI 설문조사")
num = st.number_input("학번을 입력해주세요", min_value=20601, max_value=20626)

box = st.text_input(label="이름을 입력해주세요")

radfirst = st.radio("MBTI 첫번째 자리", ('I', 'E'))
radsecond = st.radio("MBTI 두번째 자리", ('N', 'S'))
radthird = st.radio("MBTI 세번째 자리", ('T', 'F'))
radfourth = st.radio("MBTI 네번째 자리", ('J', 'P'))

if st.button("제출"):
    if 20600 < num < 20627 and len(box) == 3:
        mbti = radfirst + radsecond + radthird + radfourth
        wri = str(num) + " " + str(box) + " : " + mbti + " - "
        if wri not in data:
            inflobj = open('file.txt', 'a', encoding='utf-8')


            inflobj.write('\n' + wri + str(time.time()))
            inflobj.close()

            inflobj = open('file.txt', 'r', encoding='utf-8')
            output = inflobj.read()
            inflobj.close()

            st.code(output)
        else:
            st.caption("중복되는 데이터가 있습니다")
    else:
        st.caption("학번이나 이름이 잘못 입력되었습니다")

st.caption("-------------------------\n설문지를 제출하면 이곳에 명단이 표시됩니다")
