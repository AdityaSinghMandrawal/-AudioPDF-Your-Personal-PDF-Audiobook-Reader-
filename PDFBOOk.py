import pyttsx3
from PyPDF2 import PdfReader
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import threading

# Define background color
bg = '#ffdab9'

# Create the main Tkinter window
app = Tk()
app.geometry("550x550")
app.title("Audiobook")
app.configure(bg=bg)

# Global variables
path = None
status = "Not Reading"

# Function to handle file selection
def click():
    global path
    # Open file dialog and get selected file path
    path = filedialog.askopenfilename()
    pdf_path_label.config(text=f"Selected PDF: {path}")
    update_status("Not Reading")

# Function to read the selected PDF
def talk():
    global status
    if path:
        try:
            speaker = pyttsx3.init()
            with open(path, 'rb') as book:
                read_file = PdfReader(book)
                total_pages = len(read_file.pages)

                # Get the specified page number or read the entire PDF if -1 is entered
                page_number = page_number_box.get()
                if not page_number or int(page_number) == -1:
                    start_page = 1
                    end_page = total_pages
                elif 1 <= int(page_number) <= total_pages:
                    start_page = int(page_number)
                    end_page = int(page_number)
                else:
                    raise ValueError("Invalid page number")

                # Update status and read the specified pages
                update_status("Reading", "green")
                for current_page in range(start_page, end_page + 1):
                    page = read_file.pages[current_page - 1]
                    text = page.extract_text()
                    speaker.say(text)
                    speaker.runAndWait()

                # Update status and display advisory message
                update_status("Not Reading")
                advisory_label.config(text="Remember to open your original PDF!", fg="blue")

        except Exception as e:
            update_status(f"Error: Please Enter a valid integer", "red")

# Function to update the status label
def update_status(new_status, color="black"):
    global status
    if status != new_status:
        status_label.config(text=f"Status: {new_status}", fg=color, font=("Arial", 14))
        status = new_status
    app.after(500, check_status)

# Function to check the current status
def check_status():
    if threading.active_count() > 1:
        app.after(500, check_status)
    else:
        update_status(status)

# Function to read the PDF in a separate thread
def talk_threaded():
    threading.Thread(target=talk).start()

# Load and display the logo
image = Image.open('booklogo.png')
image_resized = image.resize((70, 70), Image.LANCZOS)
image1 = ImageTk.PhotoImage(image_resized)
logo = Label(app, image=image1, bg=bg)
logo.pack()

# Display project title and description
title = Label(app, text="AUDIOBOOK", bg=bg, font='none 25')
title.pack(pady=(5, 0))

description = Label(app, text="A digital reading tool", bg=bg, font='none 18')
description.pack()

subtitle = Label(app, text="Let's listen to the book", bg=bg, font='none 12')
subtitle.pack(pady=(20, 0))

# UI components for PDF selection and reading
page_number_label = Label(app, text="Please enter the page number (leave empty or enter -1 for entire PDF)", bg=bg, font='none 10')
page_number_label.pack(pady=(30, 0))

page_number_box = Entry(app)
page_number_box.pack()

open_PDF_button = Button(app, text='Select PDF File', width=20, command=click)
open_PDF_button.pack(pady=(20, 0))

pdf_path_label = Label(app, text="", bg=bg, font=("Arial", 8))
pdf_path_label.pack(pady=(10, 0))

# Button to initiate reading
say_PDF_button = Button(app, text="Speak", width=20, command=talk_threaded)
say_PDF_button.pack(pady=(20, 0))

# Labels for status and advisory message
status_label = Label(app, text="Status: Not Reading", bg=bg, font=("Arial", 14))
status_label.pack(pady=(45, 0))

advisory_label = Label(app, text="*It is advised that For better experience please open your original PDF once the 'status' is 'reading'", bg=bg, fg="blue", font=("Arial", 9))
advisory_label.pack(pady=(50, 0))

# Start the Tkinter main loop
app.mainloop()
