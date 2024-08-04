import streamlit as st
import pandas as pd
import pickle
st.title("Your Expected Marks Prediction ")


hours = st.number_input("Hours Studied: ", 1, 9)
score = st.number_input("Previous Exam Scores: ", 40, 99)
activities = st.slider("Extracurricular Activities\nSelect 1 for Yes, 0 For No: ", 0, 1)
sleep = st.number_input("Sleep Hours: ", 4, 9)
paper = st.number_input("Sample Papers Solved:", 0, 9)

submit = st.button("Submit")

if submit:

    data = {
        "Hours Studied": [hours],
        "Previous Scores": [score],
        "Extracurricular Activities": [activities],
        "Sleep Hours": [sleep],
        "Sample Question Papers Practiced": [paper]
    }
    
    df = pd.DataFrame(data)
    
    st.write(df)
    model = pickle.load(open('Marks.pkl', 'rb'))
    scaler = pickle.load(open('scaler.pkl', 'rb'))
    
    df_scaled = scaler.transform(df)
    ans = model.predict(df_scaled)
    st.write("Your Performance Index is: ")
    df['score'] = ans
    st.write(ans)
    st.write(df)