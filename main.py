import google.generativeai as genai
import streamlit as st
from PIL import Image
from functions import *
import os
import json


genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-pro')



if "history" not in st.session_state:
    st.session_state.history = []

if "subjects" not in st.session_state:
    st.session_state.subjects = []

if "act" not in st.session_state:
    st.session_state.act = None

if "directory" not in st.session_state:
    st.session_state.directory = os.getcwd()

if "extracted_text" not in st.session_state:
    st.session_state.extracted_text = None

if "quiz" not in st.session_state:
    st.session_state.quiz = None



with st.sidebar:
    # Title
    st.title("💬 Private Tutor")

    # Subject
    name = st.text_input('New Subject')
    if st.button('Add Subject') and name:
        st.session_state.subjects.append(name)
    subject = st.selectbox('Select a subject to learn', st.session_state.subjects)
    st.markdown("<hr>", unsafe_allow_html=True)

    # Extract Text
    extract_method = st.selectbox('Choose your educational supplement', ['File Upload', 'YouTube Link'])
    if extract_method == 'File Upload':
        # File upload
        uploaded_file  = st.file_uploader('Extract text from a file', type=["jpg", "png", "wav", "mp3", "mp4"])
        extracted_text = extract_text_from_file(uploaded_file, directory=st.session_state.directory)
        st.session_state.extracted_text = extracted_text
    else:
        # YouTube
        link = st.text_input('Enter YouTube Link')
        if st.button('Extract') and link:
            extracted_text = extract_text_from_yt(link, directory=st.session_state.directory)
            st.session_state.extracted_text = extracted_text

    # Action
    if st.session_state.extracted_text:
        action = st.selectbox('Action on the extracted text', ['Explain', 'Summarize', 'Expand'])
        if st.button('Submit Action'):
            st.session_state.act = {
                'action': action,
                'extracted_text': st.session_state.extracted_text
            }
    

if subject:
    st.title(f'Lets learn {subject} together!')

for message in st.session_state.history:
    role = message['role']
    if role == 'model':
        role = 'assistant'
    if message['parts'][0].startswith('Generate a multiple-choice') or message['parts'][0].startswith('```json'):
        continue
    with st.chat_message(role):
        st.markdown(message['parts'][0])

if st.session_state.act:
    with st.chat_message("user"):
        prompt = prompt_action(st.session_state.act['action'], st.session_state.act['extracted_text'])
        st.markdown(prompt)
        st.session_state.history.append({
            "role": "user",
            "parts": [prompt],
        })
    with st.chat_message("assistant"):
        response = model.generate_content(st.session_state.history).text
        st.markdown(response)
        st.session_state.history.append({
            "role": "model",
            "parts": [response],
        })
        st.session_state.act = None
        st.session_state.extracted_text = None

if prompt := st.chat_input("Enter your command here"):
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.history.append({
            "role": "user",
            "parts": [prompt],
        })
    with st.chat_message("assistant"):
        response = model.generate_content(st.session_state.history).text
        st.markdown(response)
        st.session_state.history.append({
            "role": "model",
            "parts": [response],
        })


# Test with Quiz
if st.session_state.history:
    test = st.button('Test Yourself with a Quiz!')
    if test:
        try:
            prompt = 'Generate a new multiple-choice question with 4 choices from our conversation as a quiz so I can test how much I learn. Only give a JSON without additional text, containing a "question", "choices", and the "correct_answer" among those choices'
            st.session_state.history.append({
                "role": "user",
                "parts": [prompt],
            })
            response = model.generate_content(st.session_state.history).text
            st.session_state.history.append({
                "role": "model",
                "parts": [response],
            })
            quiz = json.loads(response[response.find('{'):response.rfind('}')+1])
            st.session_state.quiz = quiz
        except:
            st.error('Could not generate a quiz based on the current chat history')

    if st.session_state.quiz:  
        chosen_answer = st.radio(st.session_state.quiz['question'], st.session_state.quiz['choices'])
        result_placeholder = st.empty()
        submitted = st.button("Submit Answer")
        if submitted:
            if chosen_answer:
                if chosen_answer == st.session_state.quiz['correct_answer']:
                    result_placeholder.success('Bravo, your answer is correct!')
                else:
                    result_placeholder.error('You did not choose the correct answer!')
            else:
                result_placeholder.warning("Please choose an answer before submitting.")
