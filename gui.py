import tkinter as tk
from tkinter import ttk
from tkinter import * 
from webserver import *
import threading

host_name = "localhost"
server_port = 8080
web_server = HTTPServer((host_name, server_port), WebServer)

def serve(webserver):
    webserver.serve_forever()


def close(webserver):
    webserver.server_close()


# this is the function called when the button is clicked
def startServer():
    thread = threading.Thread(target=serve, args=(web_server,))
    thread.start()
    print(f'Started server http://{host_name}:{server_port}')


# this is the function called when the button is clicked
def stopServer():
    web_server.server_close()
    print('Server stopped')
    


root = Tk()

# This is the section of code which creates the main window
root.geometry('450x290')
root.configure(background='#00FFFF')
root.title('WebServer')


# This is the section of code which creates the a label
Label(root, text='Start / Stop webserver by pressing on the buttons below:', bg='#00FFFF', font=('arial', 10, 'normal')).place(x=36, y=35)


# This is the section of code which creates a button
Button(root, text='Start', bg='#F0F8FF', font=('arial', 10, 'normal'), command=startServer).place(x=56, y=165)


# This is the section of code which creates a button
Button(root, text='Stop', bg='#F0F8FF', font=('arial', 10, 'normal'), command=stopServer).place(x=326, y=155)


root.mainloop()
