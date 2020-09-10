import socket
from tkinter import * 
#server definitions

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT = '!DISCONNE45CT!\?<>'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

#app
root = Tk()
root.geometry('500x500')
root.title('Social App')
root.wm_iconbitmap(r'C:\Users\Robera\Documents\new\Screenshot (1).ico')
class Users:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    def get_name(self):
        return self.name
    def get_email(self):
        return self.email
    def get_password(self):
        return self.password
def send(info):
    info = info.encode(FORMAT)
    info_length = len(info)
    send_length = str(info_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(info)


def display():
    send(x_user.get_name())
    send(x_user.get_email())
    send(x_user.get_password())

#password
def getpassword():
    global z
    global x_user
    z = get_password.get()
    print(z)
    x_user = Users(x, y, z)
    submitpassword['state'] = DISABLED
    get_password['state'] = DISABLED
    display()



ask_password = Label(root,text='Password: ')
get_password = Entry(root)
submitpassword = Button(root, text='Submit', command = getpassword)

def number3():
    ask_password.grid(row=3,column=1)
    get_password.grid(row=3,column=2)
    submitpassword.grid(row=3,column=3)


#email
def getemail():
    global y
    y = get_email.get()
    print(y)
    submitEmail['state'] = DISABLED
    get_email['state'] = DISABLED
    number3()    

ask_email = Label(root, text='Email: ')
get_email = Entry(root)
submitEmail = Button(root, text='Submit',command=getemail)

def number2():
    ask_email.grid(row=2,column=1)
    get_email.grid(row=2,column=2)
    submitEmail.grid(row=2,column=3)

#name
def getname():
    global x
    x = get_name.get()
    print(x)
    submitName['state'] = DISABLED
    get_name['state'] = DISABLED
    number2()




ask_name = Label(root, text='User name:')
get_name = Entry(root)
submitName = Button(root,text='Submit',command=getname)

ask_name.grid(row=1,column=1)
get_name.grid(row=1, column=2)
submitName.grid(row=1,column=3)

#main loop
root.mainloop()
#send the disconnect message when the main loop ends

send(DISCONNECT)