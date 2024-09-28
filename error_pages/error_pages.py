import streamlit as st
import pandas as pd
import time
import random

chapter = ['高数', '线代', '概率论']
chapter = st.selectbox('选择你要做的章节', chapter)

if chapter == '高数':
    chapter = 'highmath'
if chapter == '线代':
    chapter = 'metric'
if chapter == '概率论':
    chapter = 'probility'

path = f"csv\error_csv\{chapter}_error.csv"
df = pd.read_csv(path)

dict_df = df.to_dict(orient='records')
for i in range(len(dict_df)):
    dict_df[i]['options'] = dict_df[i]['options'].split(',')


# 定义空白页面
def nl(num_of_lines):
    for i in range(num_of_lines):
        st.write(" ")


st.markdown("*Write Quiz Description and Instructions.* ")
scorecard_placeholder = st.empty()

# Activate Session States
ss = st.session_state
# Initializing Session States
if 'counter' not in ss:
    ss['counter'] = 0
if 'start' not in ss:
    ss['start'] = False
if 'stop' not in ss:
    ss['stop'] = False
if 'refresh' not in ss:
    ss['refresh'] = False
if "button_label" not in ss:
    ss['button_label'] = ['START', 'SUBMIT', 'RELOAD']
if 'current_quiz' not in ss:
    ss['current_quiz'] = {}
if 'user_answers' not in ss:
    ss['user_answers'] = []
if 'grade' not in ss:
    ss['grade'] = 0


# Function for button click
def btn_click():
    ss.counter += 1
    if ss.counter > 2:
        ss.counter = 0
        ss.clear()
    else:
        update_session_state()
        with st.spinner("*this may take a while*"):
            time.sleep(2)


# Function to update current session
def update_session_state():
    if ss.counter == 1:
        ss['start'] = True
        ss.current_quiz = random.sample(dict_df, 2)
    elif ss.counter == 2:
        # Set start to False
        ss['start'] = True
        # Set stop to True
        ss['stop'] = True


st.button(label=ss.button_label[ss.counter],
         key='button_press', on_click=btn_click)


# Function to display a question
def quiz_app():
    # create container
    with st.container():
        if (ss.start):
            for i in range(len(ss.current_quiz)):
                number_placeholder = st.empty()
                question_placeholder = st.empty()
                options_placeholder = st.empty()
                results_placeholder = st.empty()
                expander_area = st.empty()
                # Add '1' to current_question tracking variable cause python starts counting from 0
                current_question = i+1
                # display question_number
                number_placeholder.write(f"*Question {current_question}*")
                # display question based on question_number
                question_placeholder.write(f"**{ss.current_quiz[i].get('question')}**")
                # list of options
                options = ss.current_quiz[i].get("options")
                # track the user selection
                options_placeholder.radio("", options, index=1, key=f"Q{current_question}")
                nl(1)
                # Grade Answers and Return Corrections
                if ss.stop:
                    # Track length of user_answers
                    if len(ss.user_answers) < 10:
                        # comparing answers to track score
                        if ss[f'Q{current_question}'] == ss.current_quiz[i].get("correct_answer"):
                            ss.user_answers.append(True)
                        else:
                            ss.user_answers.append(False)
                    else:
                        pass
                    # Results Feedback

                    if ss.user_answers[i] == True:
                        results_placeholder.success("CORRECT")
                    else:
                        results_placeholder.error("INCORRECT")
                    # Explanation of the Answer
                    expander_area.write(f"*{ss.current_quiz[i].get('explanation')}*")

    # calculate score
    if ss.stop:
        ss['grade'] = ss.user_answers.count(True)
        scorecard_placeholder.write(f"### **Your Final Score : {ss['grade']} / {len(ss.current_quiz)}**")

quiz_app()
