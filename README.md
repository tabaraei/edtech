# EdTech Challenge

This project was developed during the "GDSC AI Hackathon" managed by Google Developer Student Clubs, Polimi, April 2024

## Abstract

Throughout the development of this application, we aimed to leverage the power of Gemini and OpenAI LLMs to enable personalized training paths for individuals. The developed app empowers users from diverse backgrounds and learning needs to:

1. Interact directly with their tutor bot through prompts and ask for explanation, summarization, and expansion of the topic
2. Add supplementary educational multimedia (including images, audio recordings, and video) to utilize their transcripts as a prompt
3. Seek further explanations on YouTube tutorials
4. Participate in engaging quizzes to benefit active recall from their mistakes with a dynamic learning experience.

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

## Project Gallery

| Chatbot | Quiz |
| --- | --- |
| ![chatbot](https://github.com/tabaraei/edtech/assets/36487462/6015878e-020c-4b39-91eb-349b9bfe3814) | ![quiz](https://github.com/tabaraei/edtech/assets/36487462/6e649122-77bc-4118-953e-d5f5bcdfbcbc) |

| Image | Audio |
| --- | --- |
| ![image](https://github.com/tabaraei/edtech/assets/36487462/39ec7ebf-faa3-4dca-9f53-e932d754dc20) | ![audio](https://github.com/tabaraei/edtech/assets/36487462/c976c484-9891-40f4-859c-491e17196039) |

| Video | YouTube |
| --- | --- |
| ![YouTube](https://github.com/tabaraei/edtech/assets/36487462/916546aa-28d2-4b97-9c74-f7c19690d0f8) | ![video](https://github.com/tabaraei/edtech/assets/36487462/27d42baa-65de-4a37-9e00-64a8bd41129a) |
