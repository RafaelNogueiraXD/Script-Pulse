import os
import stat
import shutil
import subprocess
from tkinter import filedialog, Tk

import tkinter as tk
from tkinter import ttk

from datetime import datetime
from telas.notifica import *
import threading
from time import sleep
def hora_atual_numerica():

    agora = datetime.now()
    hora_numerica = agora.month * 2592000 + agora.day *86400 + agora.hour * 3600 + agora.minute * 60 + agora.second
    return hora_numerica

def copy_all_files(src_dir, dst_dir):
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    shutil.copytree(src_dir, dst_dir)
    
def give_execution_permission(path):
    current_permissions = stat.S_IMODE(os.lstat(path).st_mode)
    os.chmod(path, current_permissions | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

def run_shell_script(path):
    give_execution_permission(path) 
    command = ['bash', path]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    # print(stdout.decode())
    if stderr:
        # print(f"Errors:\n{stderr.decode()}")
        return stderr.decode()
    else: 
        return stdout.decode()

def read_bash_file(path):
    with open(path, 'r') as file:
        print(file.read())

def identify_file_type(file_path,ssh=0):
    sleep(5)
    _, extension = os.path.splitext(file_path)
    if extension == '.py':
        print('Python file')
        return ''
    elif extension == '.sh':
        # progress bar
        contentFile = main(file_path)
        print("Shell script")
        return contentFile
    else:
        print('Unknown file type')
        return ''

def get_directory_from_path(file_path):
    return os.path.dirname(file_path)

def clear_directory(path):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)  # remove file or symlink
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)  # remove directory
            
def main(file_path):
    tempoInitApp = hora_atual_numerica()
    file_path_file = os.path.basename(file_path)
    file_path_paste = get_directory_from_path(file_path)
    copy_all_files(file_path_paste, "./copiados/")
    tempoEndApp = hora_atual_numerica()
    os.chdir("./copiados/")
    
    tempoInicial = hora_atual_numerica()
    contentFile = run_shell_script(file_path_file)
    
    tempoFinal = hora_atual_numerica()
    tempoTotal = tempoFinal - tempoInicial
    tempoTotalApp = tempoEndApp - tempoInitApp
    data = {
        "nomeArquivo": file_path_file,
        "conteudo": contentFile,
        "tempoExecArquivo": tempoTotal,
        "tempoApp": tempoTotalApp
    }
    os.chdir("..")
    clear_directory("./copiados/")
    return data

def open_file_dialog(ssh=0):
    if ssh == 0:
        filename = filedialog.askopenfilename()
    else:
        print("Coloque aqui o caminho do arquivo: ",end=" ")
        filename = input()
    print(f"File selected: {filename}")
    content = identify_file_type(filename,ssh)
    return content