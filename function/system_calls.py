import os
import subprocess as sp

paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'vivaldi': "C:\\Windows\\System32\\vivaldi.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_notepad():
    os.startfile(paths['notepad'])


def open_browser():
    sp.run('start microsoft.windows.browser:', shell=True)

def open_cmd():
    os.system('start cmd')

