# EdTech Challenge

This project was developed during the "GDSC AI Hackathon" managed by Google Developer Student Clubs, Polimi, April 2024

## Abstract

Through the development of this application, we aim to leverage LLMs to enable personalized training paths for individuals. This app empowers users from diverse backgrounds and with different learning needs to interact effortlessly, ask direct questions, extract text from various multimedia formats (images, audio, video, YouTube links)

Users can instruct the app to perform a range of actions such as summarizing, explaining, and expanding on topics of interest. Moreover, within an engaging environment, users are encouraged to participate in quizzes, fostering an active learning journey. This interactive approach enhances user engagement and facilitates a more dynamic learning experience.

## Installation
The project was developed and tested on the Windows platform, using Python version `3.9.13`.

> [!IMPORTANT]  
> In order to run the project locally, first clone the repository, run the commands below sequentailly in Window Terminal (CMD), and then install the ffmpeg according to this [documentation](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows). Finally, inside the `<PROJECT_DIR>/.streamlit/secrets.toml` file we should specify the private keys for Gemini and OpenAI as `GEMINI_API_KEY = "..."` and `GEMINI_API_KEY = "..."`, respectively:
>```
>  cd edtech
>  py -3 -m venv venv
>  .\venv\Scripts\activate
>  pip install -r .\requirements.txt
>  ```
> In order to deploy the project globally using `https://share.streamlit.io` platform, we specify the private OS variables inside `secrets.toml` file as `GEMINI_API_KEY = "..."` which was taken from the Google API for Gemini, and `OPENAI_API_KEY = "..."` which was taken from the OpenAI API service. The packages are automatically installed. We should note that there might be errors on using the `ffmpeg` package due to it's specific installation process.

## User Manual

In the provided PDF file below, you may find a short summary describing the capabilities of our application.

[![PDF](https://img.shields.io/badge/File-PDF-red?logo=adobe-acrobat&style=for-the-badge)](https://github.com/tabaraei/edtech/blob/master/presentation/expecto_patronull_presentation.pdf)

## Using the application

For a limited amount of time, our application will be accessible through the following link.

[![PDF](https://img.shields.io/badge/Project-Link-blue?logo=adobe-acrobat&style=for-the-badge)](https://edtech-llm.streamlit.app/)
