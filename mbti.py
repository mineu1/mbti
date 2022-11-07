import time
import pandas as pd
import streamlit as st

inflobj = open('file.txt', 'r', encoding='utf-8')

data = inflobj.read()
inflobj.close()

st.title("2-6 MBTI 설문조사")
num = st.number_input("학번을 입력해주세요", min_value=20601, max_value=20626)

box = st.text_input(label="이름(3글자)을 입력해주세요")

radfirst = st.radio("MBTI 첫번째 자리", ('I', 'E'))
radsecond = st.radio("MBTI 두번째 자리", ('N', 'S'))
radthird = st.radio("MBTI 세번째 자리", ('T', 'F'))
radfourth = st.radio("MBTI 네번째 자리", ('J', 'P'))

def chart(data):
    c = "IE NS TF JP"
    cl = c.split(" ")
    op = []
    for i in range(16):
        bina = str(bin(i))[2:]
        x = "0" * (4 - len(bina)) + bina
        print(x)
        #list = list(x)
        result = []
        for j in range(0, 4):
            print(int(x[j]))
            result.append(str(cl[j][int(x[j])]))
        op.append("".join(result))

    print(op)

    amount = []
    for i in range(16):
        amount.append(data.count(op[i]))


    #lst = "INTJ INTP INFJ INFP ISTJ ISTP ISFP"

    chart_data = pd.DataFrame(
        amount, index=op)
    st.bar_chart(chart_data)

def chartb(data):
    c = list("IENSTFJP")
    amount = []
    for i in range(8):
        amount.append(data.count(c[i]))

    chartb_data = pd.DataFrame(
        amount, index=c)
    st.bar_chart(chartb_data)

if st.button("제출"):
    if 20600 < num < 20627 and len(box) == 3:
        mbti = radfirst + radsecond + radthird + radfourth
        wri = str(num) + " " + str(box) + " : " + mbti + " - "
        if wri not in data:
            inflobj = open('file.txt', 'a', encoding='utf-8')


            inflobj.write(wri + str(time.time()) + '\n')
            inflobj.close()

            inflobj = open('file.txt', 'r', encoding='utf-8')
            output = inflobj.read()
            inflobj.close()

            st.code(output)
            a = st.caption("-------------------------\n총" + str(output.count("\n")) + "명이 설문조사에 참여했습니다")
            chart(output)
            chartb(output)
        else:
            st.caption("중복되는 데이터가 있습니다")
            st.code(data)
            chart(data)
            chartb(data)
    else:
        st.caption("학번이나 이름이 잘못 입력되었습니다")
        st.code(data)
        chart(data)
        chartb(data)

else:
    st.code(data)

    st.caption("-------------------------\n총" + str(data.count("\n")) + "명이 설문조사에 참여했습니다")

    chart(data)
    chartb(data)

st.caption("Made by 민경현")
