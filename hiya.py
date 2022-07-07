from cProfile import label
from tkinter import *
from tkinter import messagebox
from turtle import heading

root=Tk()

root.geometry("1080x720")
root.configure(bg = "white")
root.iconbitmap('C:/Users/ASUS/PycharmProjects/pythonProject/icon.ico')
root.title("Tampilan App")
root.resizable(width=False, height=False)

def sign_in():
    username=user.get()
    password=Password.get()
    
    if username=='admin' and password=='12345':
        print('Masuk')

img = PhotoImage(file = "background.png")
Label(root, image=img, bg='white').place(x=0, y=0)

frame = Frame(root, width=380, height=460, bg="white").place(x=640, y=80)

heading = Label(frame, text='Sign In', fg='#57a1f8', bg='white',font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=640, y=100)

#textbox username
def on_enter(e):
    user.delete(0, 'end')
    
def on_leave(e):
    name=user.get()
    if name == '':
        user.insert(0, 'Username')
        
user = Entry(frame, width=40, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=640, y=190)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=325,height=2,bg='black').place(x=640, y=220)

#textbox password
def on_enter(e):
    Password.delete(0, 'end')
    
def on_leave(e):
    name=Password.get()
    if name == '':
        Password.insert(0, 'Password')
        
Password = Entry(frame, width=40, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
Password.place(x=640, y=270)
Password.insert(0, 'Password')
Password.bind('<FocusIn>', on_enter)
Password.bind('<FocusOut>', on_leave)

Frame(frame,width=325,height=2,bg='black').place(x=640, y=300)

#button
img0 = PhotoImage(file = f"button1.png")
b0 = Button(root, image = img0, bg="white", borderwidth = 0, highlightthickness = 0, command=sign_in, relief = "flat")
b0.place(x = 745, y = 377,width = 146,height = 50)
label_button = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label_button.place(x = 735, y = 437)

sign_up = Button(frame, width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=870, y=437)

root.mainloop()