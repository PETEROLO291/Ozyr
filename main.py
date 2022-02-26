#!/usr/bin/env python

from string import whitespace
from time import sleep
from os import path, mkdir, system
import os
from pathlib import Path
import PySimpleGUI as sg
import pytesseract
import PIL.Image
from PIL import ImageGrab as ig
from pyperclip import copy


# Made By PETEROLO 291©


# Custop dark theme configuration
sg.LOOK_AND_FEEL_TABLE['CustomDarkTheme'] = {'BACKGROUND': '#373737',
                                        'TEXT': '#FFFFFF',
                                        'INPUT': '#474747',
                                        'TEXT_INPUT': '#FFFFFF',
                                        'SCROLL': '#ff00d4',
                                        'BUTTON': ('white', '#474747'),
                                        'PROGRESS': ('#01826B', '#D0D0D0'),
                                        'BORDER': 0, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                        }


sg.theme("CustomDarkTheme")

# Get Images Path
cwd = Path(os.getcwd())

scan_pic = cwd / "Buttons" / "button_scan.png"

copy_pic = cwd / "Buttons" / "button_copy-output.png"


try:
    with open("language.txt", "r") as langu:
        lang = langu.read()

except FileNotFoundError:
    with open("language.txt", "w") as create_langu:
        create_langu.write("eng")
        create_langu.close()



# Variables
running = True
threads_started = False
image = None
text = ""
lang = "eng"
invisible_char = "⠀"

try:
    with open("language.txt", "r") as langu:
        lang = langu.read()

except FileNotFoundError:
    with open("language.txt", "w") as create_langu:
        create_langu.write("eng")
        create_langu.close()

# Dictionary

lang_dict = dict(eng="English", spa="Spanish", ita="Italian", deu="German", fra="French")

try:
    mkdir(path.expandvars(r"C:\Users\%USERNAME%\Q-OCR"))

except FileExistsError:
    pass

# LpoadUp
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def Snip():
    system('explorer ms-screenclip:')
    image = None
    copy('')
    while image == None:
        sleep(1)
        image = ig.grabclipboard()
    image.save(path.expandvars(r"C:\Users\%USERNAME%\Q-OCR\OCR-Screenshot.png"))
    OCR()
    return image

# OCR Recognition
def OCR():
    global text
    ocr_config = r"--psm 6 --oem 3"
    text = pytesseract.image_to_string(PIL.Image.open(path.expandvars(r"C:\Users\%USERNAME%\Q-OCR\OCR-Screenshot.png")), config=ocr_config, lang=lang)
    copy(text)


# User Interface
frame = [   [sg.Button(image_filename=scan_pic, border_width=0, font=("Arial", 15), size=(13, 0), key="-CUT-", button_color=(sg.theme_background_color(), sg.theme_background_color())),
            sg.InputOptionMenu(('English', 'Spanish', 'German', 'French', 'Italian', 'Catalan'), default_value=lang_dict[lang], size=(9,120), key="-LANG-"),
            sg.Button(image_filename=copy_pic, font=("Arial", 15), size=(13, 0), key="-COPY-", button_color=(sg.theme_background_color(), sg.theme_background_color()))],
            [sg.Multiline(default_text=f'{invisible_char * 78 + " "}Here you can edit and then copy the output', size=(1000, 1000), font=("Arial", 13), key='-OUT-', no_scrollbar=True)]]

window = sg.Window('Ozyr', frame, size=(425, 152), element_justification="c", resizable=True, finalize=True, margins=(0, 2), icon="ico.ico")
window.set_min_size((425, 152))
window['-OUT-'].Widget.config(insertbackground='#D4D4D4')



while running:
    event, values = window.read()
    try:
        if values["-LANG-"] == "English":
            lang = "eng"

        if values["-LANG-"] == "Spanish":
            lang = "spa"

        if values["-LANG-"] == "German":
            lang = "deu"

        if values["-LANG-"] == "French":
            lang = "fra"

        if values["-LANG-"] == "Italian":
            lang = "ita"

        if values["-LANG-"] == "Catalan":
            lang = "cat"

        with open("language.txt", "w+") as save_langu:
            save_langu.write(lang) # Save start key in txt file
            save_langu.close()

    except TypeError:
        pass


    if event == "-CUT-":
        window.Hide()
        image = Snip()
        window["-OUT-"].update(text)
        window.UnHide()

    if event == "-COPY-":
        get_text = str(values["-OUT-"])
        get_text = copy(get_text)

    # Window closing event
    if event == sg.WINDOW_CLOSED or event == "Close":
        running = False
