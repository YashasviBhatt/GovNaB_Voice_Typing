# Importing Libraries
from tkinter import Tk, Label, Text, Button
import pyautogui
import speech_recognition as sr

# Creating Instance
root = Tk()

# Configuring TKinter Window
root.title('GovNaB Voice Typing')
width_x = 300
width_y = 170
root.geometry(f'{width_x}x{width_y}')
root.minsize(width_x, width_y)
root.maxsize(width_x, width_y)

def speechToText():
    '''
    Function to take input as speech and return it in text form
    :return: Text converted from Speech
    '''
    r = sr.Recognizer()                                             # creating object
    with sr.Microphone() as source:                                 # using the default microphone as voice input source
        print('Listening...')
        r.pause_threshold = 1                                       # seconds of non-speaking audio before considered complete
        r.energy_threshold = 300
        audio = r.listen(source)  # taking voice input from source
    msg = ''
    try:
        print('Recognizing...')
        msg = r.recognize_google(audio, language='en-in')           # audio recognition and conversion to text
    except:
        print('Please! Say that Again')

    return msg


def writeOnSceen():
    '''
    Function which write message on screen
    :return: success status
    '''
    coord_x, coord_y = entry_message.winfo_rootx(), entry_message.winfo_rooty()         # fetching coordinates
    pyautogui.click(x=coord_x, y=coord_y)                                               # clicking on the text area
    msg = speechToText()                                                                # converting to text
    pyautogui.write(msg, interval=0.01)                                                 # writing message on Text Area

    return True


# Adding TKinter Utilities
if __name__ == '__main__':

    # Adding Utilities

    # Adding Label
    label_voice_input = Label(text='Your Message')
    label_voice_input.grid(row=0, column=0, pady=5)

    # Adding Text Area
    entry_message = Text(width=25, height=5)
    entry_message.grid(row=1, column=0, padx=47, pady=5)

    # Adding Button
    button_voice_type = Button(text='Voice Type', bg='#000080', fg='#ffffff', command=writeOnSceen)
    button_voice_type.grid(row=2, column=0, pady=5)

    # Keeping TKinter Window Open
    root.mainloop()