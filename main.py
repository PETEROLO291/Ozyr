#!/usr/bin/env python

# Imports
from time import sleep
from os import path, mkdir
import os
from pathlib import Path
import PySimpleGUI as sg
import pytesseract
import PIL.Image
from PIL import ImageGrab as ig
from pyperclip import copy
from subprocess import run


# Made By PETEROLO 291©


# Custop dark theme configuration
sg.LOOK_AND_FEEL_TABLE['CustomDarkTheme'] = {'BACKGROUND': '#202020',
                                        'TEXT': '#FFFFFF',
                                        'INPUT': '#272727',
                                        'TEXT_INPUT': 'white',
                                        'SCROLL': '#ff00d4',
                                        'BUTTON': ('white', '#2d2d2d'),
                                        'PROGRESS': ('#01826B', '#D0D0D0'),
                                        'BORDER': 0, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                        }

# Set Theme
sg.theme("CustomDarkTheme")

# Get images button
cwd = Path(os.getcwd())

scan_pic = cwd / "Buttons" / "button_scan.png"

copy_pic = cwd / "Buttons" / "button_copy.png"


# Variables
running = True
image = None
text = ""
lang = "eng"
invisible_char = "⠀"

# Create and read saved language file
try:
    with open("language.txt", "r") as langu:
        lang = langu.read()

except FileNotFoundError:
    with open("language.txt", "w") as create_langu:
        create_langu.write("eng")
        create_langu.close()

# Dictionary
lang_dict = dict(eng="English", spa="Spanish", ita="Italian", deu="German", fra="French")

# Create directory where screenshot get stored
try:
    mkdir(path.expandvars(r"C:\Users\%USERNAME%\Ozyr"))

except FileExistsError:
    pass


# Snipping
def Snip():
    run("explorer ms-screenclip:")
    image = None
    copy('')
    while image == None:
        sleep(1)
        image = ig.grabclipboard()
    image.save(path.expandvars(r"C:\Users\%USERNAME%\Ozyr\OCR-Screenshot.png"))
    OCR()
    return image

# OCR Recognition
def OCR():
    global text
    ocr_config = r"--psm 6 --oem 3"
    text = pytesseract.image_to_string(PIL.Image.open(path.expandvars(r"C:\Users\%USERNAME%\Ozyr\OCR-Screenshot.png")), config=ocr_config, lang=lang)
    copy(text)


# User Interface
frame = [   [sg.Titlebar('Ozyr', icon=b'iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAEBUlEQVR4nJWUWWyUVRiGn/NvM8OgbBUIrbQWsJROiSXBuKBUExRiCIniHTcYIFAkEqImEm/FxIUbCGo0XqFBI2pBE80YF1JCRGNNO6Us7ZRqi22ny7Sz/9vnxUzHkTQxvsk5N1/ynO+c7z2vAjSllC8i66qrq3+pX7U65NgOmq4hvqgnntzWXVtbOw0wMDCw8LvotxGlKfE9H9Myiff35YaHhzcqpa6IiAagG4YBsHn/gYMiIl5iIiWTyZxMTGVkJm1LKutKKuvKTNqWiamMTCZzkphIiYh4+w8cFGBziaEb/CPPsgL0Xo1z6NABTNMkGAwiIoKIAKCKyufzOI7DiZPvYFkBAG8WUglUtl2g5u4ajr3+Bpl0mmvXrgIoAQWlDWhoWEt4/nxqamqw7UJlqQh0HEeZyhSAeSGLSFOEWHcXF374HqUUIn6pQQ0RYUPLBiJNEQIBvQQxxHEcpZSidHFDfDyj4Doks3lGRseobmjg/TMf4fNvaUByOsPArWGWL1tKwXVwcQ3dMKTc6h2mdXKBFXxaCwWXRlbW6/lCgf1btrNt40M4uVyxS8D3fULhMF9fvsi70fMEAwFif8Q9P5cfm7bzn6cc+3kFsG7BXdeONm+69+LIoP/2A09pId8DXxXPs/NgmKC00uhc0DXQwDYCvHCp3d+0vE471t1x/cp0okEDaFm8rDdsmIKmJHTnIj642c32jk95s/8yVFXRmZ9i+6XPONgV5S/D59mfz9H2WxRMHcswJWyY0rJ4We/sk3B6R1t0SSCkAroh8ZGbfHijk+OPPMOPt+J809/Na7//RNvqDRxuephkNs316XEujA4yNDWGrpQssULq9I62aBn4XxIEXWmMZGdwxacnOYapNGqrVpB2bJQqu6YI3NV+astEIScFz1X1y+t4bk0LRzrO0rqinq2rmnn1vlZO3PiVj+NdBE2L4/dvZWddE4mZSRZYQZUoZGRX+6ktZR92To42bqteo/BF5Wam2FPXzJ6V64tDGR+nJbiI8w/uBKXAc1hzTwsooWBYZOyCyrqu6pwcbfzftvF8n3nhMF9d7uC96Fdz2gZA13QdoHX33n0ynsp5sb5BGUpmJC0iM7ettIgMJTMS6xuU8VTO2713nwCtJUYxHDzXVaYy3YBhsnBekNCKamLdXbx0/K05v97hIy8SaV5PIKATMEwMDNdxK76eaZri4iqAbM6mt7eXTDbLo489Xp5y8X2K08xks8R6YjQ2NgLg4irTLGZBZdqIZQUY+nOIo6+8XI6vudTe/sXt8SWztUqgbtsFGtfWc+aTs+i6Xo7B26WUwvM8qhbPn40vvRIonucBJM6f+zLb0xMLObYjqtKtc0hExLRMFe/vywKJEkP+BlghExsvY9PCAAAAAElFTkSuQmCC', background_color="#202020")],
            [sg.Button(image_filename=scan_pic, font=("Arial", 15), size=(13, 0), key="-CUT-", button_color=(sg.theme_background_color(), sg.theme_background_color())),
            sg.InputOptionMenu(('English', 'Spanish', 'German', 'French', 'Italian', 'Catalan'), default_value=lang_dict[lang], size=(9,120), key="-LANG-"),
            sg.Button(image_filename=copy_pic, font=("Arial", 15), size=(13, 0), key="-COPY-", button_color=(sg.theme_background_color(), sg.theme_background_color()))],
            [sg.Multiline(expand_y=True, default_text=f'{invisible_char * 143 + " "}Here you can edit and then copy the output', size=(1000, 5), font=("Arial", 13), key='-OUT-', no_scrollbar=True)]]

# Window construction
window = sg.Window('Ozyr', frame, size=(510, 215), element_justification="c", resizable=True, finalize=True, margins=(0, 2))

# Minimum windows size
window.set_min_size((510, 215))

# Cursor color
window['-OUT-'].Widget.config(insertbackground='#D4D4D4')


# Tesseract lpoadUp
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

while running:
    event, values = window.read()

    # Language detection and definition
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

    # Window hide, snip and textbox update
    if event == "-CUT-":
        window.Hide()
        image = Snip()
        window["-OUT-"].update(text)
        window.UnHide()

    # Copy output text
    if event == "-COPY-":
        get_text = str(values["-OUT-"])
        get_text = copy(get_text)

    # Window closing event
    if event == sg.WINDOW_CLOSED or event == "Close":
        running = False
