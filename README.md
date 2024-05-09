# Audiobook Reader

## Description
Audiobook Reader is a Python program that allows users to convert PDF documents into spoken audio. It utilizes the PyPDF2 library to extract text from PDF files and the pyttsx3 library to convert the text into speech. The program provides a simple user interface (UI) where users can select a PDF file, specify the page number or choose to read the entire document, and initiate the reading process.

## Features
- Select a PDF file from your system.
- Specify a page number to start reading from, or read the entire document.
- Real-time status updates on the reading process.
- Advisory message for a better user experience.

## Requirements
- Python 3.x
- PyPDF2 library
- pyttsx3 library
- Tkinter library (usually included with Python installations)
- PIL library (Python Imaging Library) for handling images

## Installation and Usage
1. **Code**
 https://github.com/AdityaSinghMandrawal/AudioPDF-Your-Personal-Audiobook-Reader.git
2. **Install Dependencies:**
 pip install PyPDF2 pyttsx3 pillow
3. **Run the Program:**
 python PDFBOOK.py
4. **Using the Program:**
- Click on the "Select PDF File" button to choose a PDF document.
- Enter the page number you wish to start reading from (leave empty or enter -1 for the entire PDF).
- Click on the "Speak" button to initiate the reading process.
- Real-time status updates will be displayed, indicating whether the program is reading or not.
- Advisory messages will guide you for a better experience.

## Example
$ python PDFBOOK.py


