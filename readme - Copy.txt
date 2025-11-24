#Chatbot - A chatbot is a computer program that simulates human conversation through text or voice, 
used to interact with users and perform tasks I am here generating a simple python chat bot to perform some local tasks 


# MIA - A Basic Python Voice Assistant for a pc
This script run a simple voice assistant named "MIA" using Python.

# Pre installed modules and pips
- Python 3.14
- Required python libraries:
    - pyttsx3 for text-to-speech
    - datetime for time functions
    - speech_recognition for converting speech to text
    - wikipedia for fetching Wikipedia summaries
    - webbrowser for opening web pages
    - os for system interactions, like opening programs

# Setup
1. Install Libraries:*
   You can install the necessary Python packages using pip:
   pip install pyttsx3 SpeechRecognition wikipedia

2. Run the script:
   vityarthee.py

# Key Features
Voice Output: Uses the pyttsx3 library to speak responses.
Greeting: Wakes up and greets the user based on the time of day morning, afternoon, evening.
Voice Command Input: Listens for commands via the microphone using speech_recognition and Google Speech Recognition API.
Commands:
    - wikipedia query: Searches Wikipedia and reads a summary.
    - open youtube: Opens YouTube in the default web browser.
    - open google: Opens Google in the default web browser.
    - open stackoverflow: Opens Stack Overflow.
    - open vtop: Opens a specific VIT Bhopal VTOP URL.
    - open Vityarthi: Opens a specific Vityarthi URL.
    - open Github: Opens GitHub.
    - open spotify: Opens Spotify's web player.
    - the time: Reads the current time.
    - open code: Opens VS Code (Assumes a local installation path).
    - quit: Terminates the assistant.

# Notes
-Voice: The assistant is set to use the second available voice voices[1]. This may vary by system.
-VS Code Path: The path for VS Code is local. You shoud change it first for using on another pc 

Created by-Lokesh Kewat/25BCE11012/VIT