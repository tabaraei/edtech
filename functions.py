import google.generativeai as genai
import streamlit as st
from PIL import Image
import whisper
import os
from pytube import YouTube
import json


def extract_text_from_file(uploaded_file, directory):
    if uploaded_file:
        model = genai.GenerativeModel('gemini-pro-vision')
        if uploaded_file.type.startswith('image'):
            image = Image.open(uploaded_file)
            response = model.generate_content(image)
            return response.text

        elif uploaded_file.type.startswith('audio') or uploaded_file.type.startswith('video'):
            # Check directory existence
            uploads_directory = os.path.join(directory, 'uploads')
            if not os.path.exists(uploads_directory):
                os.makedirs(uploads_directory)

            # Download the file
            file_path = os.path.join(uploads_directory, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Extract the text
            model = whisper.load_model("base")
            transcript = model.transcribe(file_path)

            # Delete the file
            if os.path.exists(file_path):
                os.remove(file_path)

            # Return the transcript
            return transcript['text']

    else:
        return None


def extract_text_from_yt(link, directory):
    # Check directory existence
    uploads_directory = os.path.join(directory, 'uploads')
    if not os.path.exists(uploads_directory):
        os.makedirs(uploads_directory)

    # Download the file
    file_path = os.path.join(uploads_directory, 'YouTube.mp3')
    yt = YouTube(link)
    stream = yt.streams.filter(only_audio=True)[0]
    stream.download(filename=file_path)

    # Extract the text
    model = whisper.load_model("base")
    transcript = model.transcribe(file_path)

    # Delete the file
    if os.path.exists(file_path):
        os.remove(file_path)

    # Return the transcript
    return transcript['text']


def prompt_action(action, extracted_text):
    if action == 'Explain':
        prompt = f'Explain this text for me so I can understand better:\n{extracted_text}'
    elif action == 'Summarize':
        prompt = f'Summarize this text for me and highlight the key points:\n{extracted_text}'
    elif action == 'Expand':
        prompt = f'Expand this text for me by additional information from your knowledge. Organize the content and return the result:\n{extracted_text}'

    return prompt


def generate_quiz():
    model = genai.GenerativeModel('gemini-pro')
    prompt = 'Generate a multiple-choice question with 4 choices from our conversation as a quiz so I can test how much I learn. Only give a JSON without additional text, containing a "question", "choices", and the "correct_answer" among those choices'
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
    return quiz