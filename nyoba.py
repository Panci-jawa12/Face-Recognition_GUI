import tkinter as tk
from PIL import Image, ImageTk
import cv2
import numpy as np
import imutils

root = tk.Tk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.state('zoomed')
root.iconbitmap('C:/Users/ASUS/PycharmProjects/pythonProject/icon.ico')
root.title("Tampilan App")
Bg = tk.PhotoImage(file="image/bg2.png")
Bg1 = tk.Label(root, image = Bg).place(x=0, y=0, relwidth=1, relheight=1)

left_frame = tk.LabelFrame(root, width=352, height=510, bg="#33A67B")
left_frame.place(x=698, y=106)
Labelfr = tk.Label(left_frame, text="Data User", bg="#33A67B", font=("times new roman", 14, "bold"))
Labelfr.place(x=120, y=5)

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

def Quit():
    global video
    Frame_video.place_forget()
    video.release()

# warna tombol
btn_color = "#066056"

# tombol
button = tk.Button(root, text="Mulai", bg=btn_color, relief="flat", cursor="hand2",
                   command=video_stream, width=12, height=2, font=("times new roman", 14, "bold"))
button.place(x=210, y=639)

button2 = tk.Button(root, text="Kembali", bg=btn_color, relief="flat", cursor="hand2",
                   command=quit, width=12, height=2, font=("times new roman", 14, "bold"))
button2.place(x=792, y=639)

Frame_video = tk.Label(root, bg="black")
Frame_video.place(x=30, y=105)


root.mainloop()