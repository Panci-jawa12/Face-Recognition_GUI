from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from time import strftime
import cv2
import ast
import imutils

screen=Tk()
# screen.rowconfigure(0, weight=1)
# screen.columnconfigure(0, weight=1)
# screen.state('zoomed')
screen.configure(bg="#5e72e4")
screen.geometry("1286x746")
screen.resizable(False, False)

color = {"skyblue": "#87CEEB", "home": "#F8F9D7", "topframe": "#C4D7E0"} 
    
def login():
    username=user.get()
    password=Password.get()
    
    file=open('datasheet.txt', 'r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()
    
    # print(r.keys())
    # print(r.values())
    
    if username in r.keys() and password==r[username]:
        root=Toplevel(screen)
        root.title("Halaman Dashboard")
        # root.rowconfigure(0, weight=1)
        # root.columnconfigure(0, weight=1)
        # root.state('zoomed')
        root.iconbitmap('C:/Users/ASUS/PycharmProjects/pythonProject/icon.ico')
        #root.configure(bg="#F8F9D7")
        root.geometry("1286x746")
        root.resizable(False,False)
        
        #Top Frame
        topFrame=Frame(root, width=2000, height=60, bg='#6E85B7')
        topFrame.place(x=0, y=0)
        
        def default_home():
            f2=Frame(root,width=2000,height=1000,bg='#F8F9D7')
            f2.place(x=0,y=60)
            l2=Label(f2,text="Face Recognition\nGUI",fg='black',bg='#F8F9D7')
            l2.config(font="System 30")
            l2.place(x=480, y=240)
            
        def home():
            f1.destroy()
            f2=Frame(root,width=2000,height=1000,bg='#F8F9D7')
            f2.place(x=0,y=70)
            l2=Label(f2,text="Face Recognition\nGUI",fg='black',bg='#F8F9D7')
            l2.config(font="System 30")
            l2.place(x=480, y=240)
            togle_win()
            
        def presensi():
            f1.destroy()
            f2=Frame(root,width=2000,height=1000,bg='#F8F9D7')
            f2.place(x=0,y=70)
            l3=Label(f2,text="Face Recognition GUI",fg='black',bg='#F8F9D7')
            l3.config(font=("Sans serif", 24, "bold"))
            l3.place(x=470, y=10)
            lf = LabelFrame(root, width=352, height=510, bg="#6E85B7")
            lf.place(x=818, y=136)
            l2=Label(lf,text="Data User",fg='black',bg='#6E85B7')
            l2.config(font=("Sans serif", 14, "bold"))
            l2.place(x=120, y=5)
            
            video = None
            
            def video_stream():
                global video
                video = cv2.VideoCapture(0)
                Start()
    
            def Start():
                global video
                ret, frame = video.read()
                if ret == True:
                    frame = imutils.resize(frame, width=676)
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    img = Image.fromarray(frame)
                    image = ImageTk.PhotoImage(image=img)
                    Frame_video.configure(image=image)
                    Frame_video.image = image
                    Frame_video.after(10, Start)

            def quit():
                global video
                Frame_video.place_forget()
                video.release()

            # warna tombol
            btn_color = "#6E85B7"

            # tombol
            button = Button(root, text="Mulai", bg=btn_color, activebackground=btn_color,relief="flat", cursor="hand2",
                               command=video_stream, width=12, height=2, font=("Sans serif", 14, "bold"))
            button.place(x=318, y=669)

            button2 = Button(root, text="Berhenti", bg=btn_color, activebackground=btn_color, relief="flat", cursor="hand2",
                             command=quit, width=12, height=2, font=("Sans serif", 14, "bold"))
            button2.place(x=792, y=669)

            Frame_video = Label(root, bg="black")
            Frame_video.place(x=140, y=135)
            
            togle_win()
            
        def training():
            f1.destroy()
            f2=Frame(root,width=2000,height=1000,bg='#F8F9D7')
            f2.place(x=0,y=70)
            l2=Label(f2,text="Training Gambar",fg='black',bg='#F8F9D7')
            l2.config(font="System 30")
            l2.place(x=480, y=240)
            togle_win()
                    
        def togle_win():
            global f1
            f1=Frame(root, width=300, height=1500, bg='#B2C8DF')
            f1.place(x=0, y=0)
            
            #button
            def bttn(x,y,text,bcolor,fcolor,cmd):
                
                def on_entera(e):
                    myButton1['background'] = bcolor #ffcc66
                    myButton1['foreground']= '#262626'  #000d33

                def on_leavea(e):
                    myButton1['background'] = fcolor
                    myButton1['foreground']= '#262626'
                
                myButton1 = Button(f1, text=text, width=42, height=2, fg='#262626', border=0, bg=fcolor, 
                                   activeforeground='#262626', activebackground=bcolor, command=cmd)
            
                myButton1.bind("<Enter>", on_entera)
                myButton1.bind("<Leave>", on_leavea)

                myButton1.place(x=x,y=y)
                
            bttn(0,120,'B E R A N D A','#9CB4CC','#B2C8DF',home)
            bttn(0,157,'P R E S E N S I','#9CB4CC','#B2C8DF',presensi)
            bttn(0,194,'T A M B A H  U S E R','#9CB4CC','#B2C8DF',training)
            
            def dele():
                f1.destroy()
            
            global img1
            img1=ImageTk.PhotoImage(Image.open('image/close.png'))
            Button(f1, image=img1, command=dele, border=0, activebackground='#B2C8DF', bg='#B2C8DF').place(x=15, y=10)
        
        default_home()
        
        img2=ImageTk.PhotoImage(Image.open('image/menu.png'))
        Button(root, image=img2, command=togle_win, border=0, activebackground='#6E85B7', bg='#6E85B7').place(x=15, y=10)
            
        # homeLabel=Label(root, text="Face Recognition\nGUI", font="System 30", fg="black", border=1 ,bg=color['home'])
        # homeLabel.place(x=480, y=240)
        
        root.mainloop()
    
    else:
        messagebox.showerror('Invalid','Invalid Username & Password')

#####################################################################################
def signup_command():
    window=Toplevel(screen)
    # window.rowconfigure(0, weight=1)
    # window.columnconfigure(0, weight=1)
    # window.state('zoomed')
    window.configure(bg="#5e72e4")
    window.geometry("1286x746")
    window.resizable(False, False)
    
    def sign_up():
        username=usernamed.get()
        password=Pasword.get()
        confirm_password=confirm_code.get()

        if password==confirm_password:
            try:
                file=open('datasheet.txt', 'r+')
                d=file.read()
                r=ast.literal_eval(d)
            
                dict2={username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()
            
                file=open('datasheet.txt', 'w')
                w=file.write(str(r))
            
                messagebox.showinfo('Signup', 'Sucessfully sign up')
                window.destroy()
            
            except:
                file=open('datasheet.txt', 'w')
                pp=str({'Usernam':'password'})
                file.write(pp)
                file.close()
        else:
            messagebox.showerror('Invalid', "Both Password should match")
        
    def signin():
        window.destroy()
    
    #icon
    image_icon=PhotoImage(file="image/icon.png")
    window.iconphoto(False, image_icon)
    window.title("Tampilan App")
    
    img = PhotoImage(file='image/signup.png')
    Label(window, image=img, bg='#5e72e4').place(x=0, y=0)
    
    Frame(window, width=696, height=768, bg="#5e72e4").place(x=672, y=0)
    
    heading = Label(window, text='Sign Up', fg='#ffffff', bg='#5e72e4',font=('Microsoft YaHei UI Light', 28, 'bold'))
    heading.place(x=782, y=100)
    
    #create username
    def on_enter(e):
        usernamed.delete(0, 'end')
    
    def on_leave(e):
        name=usernamed.get()
        if name == '':
            usernamed.insert(0, 'Username')
            
    usernamed = Entry(window, width=40, fg='white', border=0, bg="#5e72e4", font=('Microsoft YaHei UI Light', 14))
    usernamed.place(x=782, y=190)
    usernamed.insert(0, 'Username')
    usernamed.bind('<FocusIn>', on_enter)
    usernamed.bind('<FocusOut>', on_leave)
    Frame(window,width=385,height=2,bg='white').place(x=782, y=226)
    
    #create a new password
    def on_enter(e):
        Pasword.delete(0, 'end')
    
    def on_leave(e):
        name=Pasword.get()
        if name == '':
            Pasword.insert(0, 'Password')
            
    Pasword = Entry(window, width=40, fg='white', border=0, bg="#5e72e4", font=('Microsoft YaHei UI Light', 14))
    Pasword.place(x=782, y=260)
    Pasword.insert(0, 'Password')
    Pasword.bind('<FocusIn>', on_enter)
    Pasword.bind('<FocusOut>', on_leave)
    Frame(window,width=385,height=2,bg='white').place(x=782, y=300)
    
    #confirm password
    def on_enter(e):
        confirm_code.delete(0, 'end')
    
    def on_leave(e):
        if confirm_code.get()== '':
            confirm_code.insert(0, 'Confirm Password')
            
    confirm_code = Entry(window, width=40, fg='white', border=0, bg="#5e72e4", font=('Microsoft YaHei UI Light', 14))
    confirm_code.place(x=782, y=350)
    confirm_code.insert(0, 'Confirm Password')
    confirm_code.bind('<FocusIn>', on_enter)
    confirm_code.bind('<FocusOut>', on_leave)
    Frame(window,width=385,height=2,bg='white').place(x=782, y=380)
    
    #button
    img1 = PhotoImage(file = f"image/button1.png")
    b1 = Button(window, image = img1, bg="#5e72e4", borderwidth = 0, activebackground='#5e72e4',
                highlightthickness = 0, relief = "flat", command=sign_up)
    b1.place(x = 890, y = 427,width = 146,height = 50)
    label_buton = Label(window, text="I have an account", fg='white', bg='#5e72e4', font=('Microsoft YaHei UI Light', 9))
    label_buton.place(x = 890, y = 487)
    
    sign_in = Button(window, width=6, text='Sign In', border=0, activebackground='#5e72e4',
                     bg='#5e72e4', cursor='hand2', fg='#001D6E', command=signin)
    sign_in.place(x=990, y=487)
       
    window.mainloop()
        
################################################################################
    
#icon
image_icon=PhotoImage(file="image/icon.png")
screen.iconphoto(False, image_icon)
screen.title("Tampilan App")
    
img=PhotoImage(file="image/background.png")
Label(screen, image=img, bg='#5e72e4').place(x=0, y=0)
    
frame=Frame(screen, width=696, height=770, bg="#5e72e4").place(x=672, y=0)
    
heading = Label(frame, text='Sign In', fg='#ffffff', bg='#5e72e4',font=('Microsoft YaHei UI Light', 28, 'bold'))
heading.place(x=782, y=100)
    
#--------------textbox username---------------------#
def on_enter(e):
    user.delete(0, 'end')
    
def on_leave(e):
    name=user.get()
    if name == '':
        user.insert(0, 'Username')
    
user = Entry(frame, width=40, fg='white', border=0, bg="#5e72e4", font=('Microsoft YaHei UI Light', 14))
user.place(x=782, y=190)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame,width=385,height=2,bg='white').place(x=782, y=226)
    
#textbox password
def on_enter(e):
    Password.delete(0, 'end')
    
def on_leave(e):
    name=Password.get()
    if name == '':
        Password.insert(0, 'Password')
    
Password = Entry(frame, width=40, fg='white', border=0, bg="#5e72e4", font=('Microsoft YaHei UI Light', 14))
Password.place(x=782, y=260)
Password.insert(0, 'Password')
Password.bind('<FocusIn>', on_enter)
Password.bind('<FocusOut>', on_leave)
Frame(frame,width=385,height=2,bg='white').place(x=782, y=300)
    
#button sign up
img0 = PhotoImage(file = f"image/button1.png")
b0 = Button(screen, image = img0, bg="#5e72e4", borderwidth = 0, activebackground='#5e72e4',
            highlightthickness = 0, relief = "flat", command=login)
b0.place(x = 896, y = 356,width = 146,height = 50)
label_button = Label(frame, text="Don't have an account?", fg='white', bg='#5e72e4', font=('Microsoft YaHei UI Light', 9))
label_button.place(x = 876, y = 418)

sign_up = Button(frame, width=6, text='Sign Up', border=0, bg='#5e72e4', activebackground='#5e72e4',
                 cursor='hand2', fg='#001D6E', command=signup_command,)
sign_up.place(x=1016, y=418)

screen.mainloop()