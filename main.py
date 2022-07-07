import cv2
from cv2 import FONT_HERSHEY_COMPLEX
import numpy as np
from tkinter import *
from PIL import Image,ImageTk

root=Tk()

#root.geometry("500x500")
root.iconbitmap('C:/Users/ASUS/PycharmProjects/pythonProject/icon.ico')
root.title("Tampilan GUI")
root.resizable(width=False, height=False)

Label(root, text="Tampilan GUI Face Recognition", font=("times new roman", 16, "bold")).pack()
L1 = Label(root)
L1.pack()

cap = cv2.VideoCapture(1)

while True:
    img = cap.read()[1]
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(Image.fromarray(img))
    L1['image'] = img
    
    root.update()

#cap.release()