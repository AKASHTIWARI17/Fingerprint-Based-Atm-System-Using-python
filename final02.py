from tkinter import *
from tkinter import messagebox
import re
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import os

pinname = {}
nameamount = {}

h = Tk()
h.title("Service Bank")
h.geometry("655x655")
h.maxsize(width=650, height=650)
h.minsize(width=600, height=600)


def shyam():
    top = Toplevel()
    top.maxsize(width=650, height=650)
    top.minsize(width=640, height=600)
    head = Label(top, text="Welcome to Registration Form", bg="green", fg="white", font=("", 26)).pack()

    def submit():
        if en.get() == "" or en2.get() == "":
            messagebox.showwarning("warning", "Blank Invalid")
        else:
            v = en.get()
            g = int(v)

            v2 = en2.get()
            g2 = str(v2)

            v2 = en2.get()
            g2 = str(v2)

            pinname[g] = g2
            print(pinname)
            if pinname == "":
                messagebox.showwarning("warning", "Not filled properly")
            else:
                ko = messagebox.showinfo("info", "congratulations you are registered")
                if ko == True:
                    print("hello")
                else:
                    top.destroy()


    en = Entry(top, bd=2)
    en.place(x=160, y=150)
    pin = Label(top, text="Enter your new pin:")
    pin.place(x=20, y=150)

    en2 = Entry(top, bd=2)
    en2.place(x=160, y=200)
    pin = Label(top, text="Enter your new name:")
    pin.place(x=20, y=200)

    def select_image():
        global image_path
        filetypes = (("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*"))
        image_path = filedialog.askopenfilename(title="Select Image")
        if image_path:
            image_label.config(text="Selected Image: " + image_path)
        else:
            image_label.config(text="No image selected.")

    def save_image():
        if image_path:
            save_dir = r"C:/Users/akash/OneDrive\Documents/fingerProject/new001/img"  # Change this to the directory you want to save the image to
            image_name = image_path.split("/")[-1]
            save_path = f"{save_dir}/{image_name}"
            Image.open(image_path).save(save_path)
            messagebox.showinfo(title="Success!", message="Image saved to " + save_path)
            message1 = True
            if message1:
                submit1()
        else:
            messagebox.showerror(title="Error", message="No image selected.")

    select_image_button = tk.Button(top, text="Select Fingerprint", command=select_image)
    select_image_button.place(x=150, y=250)
    image_label = tk.Label(top)
    image_label.pack()

    save_image_button = tk.Button(top, text="Save", command=save_image)
    save_image_button.place(x=280, y=250)

    def submit1():
        su = Button(top, text="SUBMIT", fg="green", command=submit)
        su.place(x=9, y=250)


te = Frame(h)
te.pack(side=TOP)
Label(te, text="Welcome to the ATM service", fg="white", font=("arial", 33), bg="blue").pack()

en = Frame(h)
en.pack()
war = StringVar()

bt = Button(text="Register yourself", bd=5, command=shyam)
bt.place(x=20, y=110)


def depo():
    top2 = Toplevel()
    top2.maxsize(width=650, height=650)
    top2.minsize(width=640, height=600)
    head2 = Label(top2, text="Welcome to cash deposit", bg="orange", fg="black", font=("", 26)).pack()

    ent5 = Entry(top2, bd=2)
    ent5.place(x=160, y=150)

    def upload_file():
        img1_path = filedialog.askopenfilename(title="Select the first image file",
                                                filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        img1 = cv2.imread(img1_path)
        folder_path = r"C:/Users/akash/OneDrive\Documents/fingerProject/new001/img"
        match_found = False
        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
                img2 = cv2.imread(os.path.join(folder_path, filename))
                if img1.shape == img2.shape:
                    difference = cv2.subtract(img1, img2)
                    result = cv2.countNonZero(cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY))
                    if result == 0:
                        messagebox.showinfo("Image Matched", "Image matched successfully!")
                        print("The images are completely identical")
                        match_found = True
                        message = True
                        if message:
                            submit()
                        break
        if not match_found:
            messagebox.showerror("Error", "Images do not match.")

    textho = Label(top2, fg="green")
    textho.place(x=170, y=400)

    def amou():
        if len(pinname) < 1:
            messagebox.showwarning("Warning", "Register yourself")
        else:
            v = ent5.get()
            do = int(v)
            for i in pinname:
                if i == do:
                    k = entvalue.get()
                    fo = int(k)
                    print(fo)

                    # Check if the user already has an account balance
                    if pinname.get(i) in nameamount:
                        nameamount[pinname.get(i)] += fo
                    else:
                        nameamount[pinname.get(i)] = fo

                    print(nameamount)
                    lp = messagebox.showinfo("Successfully", "Money deposited successfully")
                    if lp:
                        print("Yes")
                else:
                    messagebox.showwarning("Warning", "You are not a customer")
                    top2.destroy()

    pinvalue = Label(top2, text="Enter your PIN:")
    pinvalue.place(x=20, y=150)
    entvalue = Entry(top2, bd=2)
    entvalue.place(x=160, y=200)
    pin = Label(top2, text="Enter your Amount:")
    pin.place(x=6, y=200)

    def submit():
        su = Button(top2, text="SUBMIT", fg="green", command=amou)
        su.place(x=9, y=240)

    b1 = Button(top2, text='Upload Finger print',
                width=20, command=lambda: upload_file())
    b1.place(x=20, y=300)


bt = Button(text="Cash deposit", bd=5, command=depo)
bt.place(x=450, y=110)

def cash():
    top3 = Toplevel()
    top3.maxsize(width=650, height=650)
    top3.minsize(width=640, height=600)
    head2 = Label(top3, text="Welcome to CASH withdrawal", bg="purple", fg="white", font=("", 26)).pack()

    ent6 = Entry(top3, bd=2)
    ent6.place(x=160, y=150)

    def upload_filew():
        img1_path = filedialog.askopenfilename(title="Select the first image file",
                                                filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        img1 = cv2.imread(img1_path)
        folder_path = r"C:/Users/akash/OneDrive\Documents/fingerProject/new001/img"
        match_found = False
        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
                img2 = cv2.imread(os.path.join(folder_path, filename))
                if img1.shape == img2.shape:
                    difference = cv2.subtract(img1, img2)
                    result = cv2.countNonZero(cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY))
                    if result == 0:
                        messagebox.showinfo("Image Matched", "Image matched successfully!")
                        print("The images are completely identical")
                        match_found = True
                        message = True
                        if message:
                            submitw()
                        break
        if not match_found:
            messagebox.showerror("Error", "Images do not match.")

    textho4 = Label(top3, fg="green")
    textho4.place(x=170, y=400)

    textho2 = Label(top3, fg="green")
    textho2.place(x=170, y=400)

    def submitwith():
        if len(nameamount) < 1:
            messagebox.showwarning("Warning", "Deposit money first")
        else:
            vp = ent6.get()
            dos = int(vp)
            for i in pinname:
                if i == dos:
                    ky = entvalue1.get()
                    so = int(ky)
                    if so > nameamount.get(pinname[i]):
                        messagebox.showwarning("Warning", "Insufficient balance")
                    else:
                        textho2.config(text="Welcome back Mr:" + pinname.get(i) + "\nthanks for using bank\nwithdrawal amount:" + ky)
                        nameamount[pinname.get(i)] -= so  # Deduct the withdrawal amount
                        print(nameamount)
                        lp = messagebox.showinfo("Successfully", "Money withdrawal successful")
                        if lp:
                            print("yes")
                    break
            else:
                messagebox.showwarning("Warning", "You are not a customer")
                top3.destroy()


    b1 = Button(top3, text='Upload Finger print',
                width=20, command=lambda: upload_filew())
    b1.place(x=20, y=300)

    pinvalue1 = Label(top3, text="Enter your pin:")
    pinvalue1.place(x=20, y=150)

    entvalue1 = Entry(top3, bd=2)
    entvalue1.place(x=230, y=200)
    pin2 = Label(top3, text="Enter your withdrawl amount:")
    pin2.place(x=2, y=200)

    def submitw():
        su1 = Button(top3, text="SUBMIT", fg="green", command=submitwith)
        su1.place(x=9, y=240)


bt = Button(text="Cash withdrawal", bd=5, command=cash)
bt.place(x=20, y=160)


def checkb():
    top4 = Toplevel()
    top4.maxsize(width=650, height=650)
    top4.minsize(width=640, height=600)
    head2 = Label(top4, text="welcome to balance check service", bg="pink", fg="white", font=("", 26)).pack()

    ent7 = Entry(top4, bd=2)
    ent7.place(x=160, y=150)

    def upload_fileb():
        img1_path = filedialog.askopenfilename(title="Select the first image file",
                                                filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        img1 = cv2.imread(img1_path)
        folder_path = r"C:/Users/akash/OneDrive\Documents/fingerProject/new001/img"
        match_found = False
        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
                img2 = cv2.imread(os.path.join(folder_path, filename))
                if img1.shape == img2.shape:
                    difference = cv2.subtract(img1, img2)
                    result = cv2.countNonZero(cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY))
                    if result == 0:
                        messagebox.showinfo("Image Matched", "Image matched successfully!")
                        print("The images are completely identical")
                        match_found = True
                        message = True
                        if message:
                            submitb()
                        break
        if not match_found:
            messagebox.showerror("Error", "Images do not match.")

    def click():
        if len(nameamount) < 1:
            messagebox.showwarning("Warning", "Deposit money to check balance")
        else:
            vpo = ent7.get()
            dosh = int(vpo)
            for i in pinname:
                if i == dosh:
                    if pinname.get(i) in nameamount:
                        balance = nameamount[pinname.get(i)]
                        if balance >= 0:
                            textho3.config(text="Welcome back Mr:" + pinname.get(i) + "\nThanks for using the bank\nBalance: " + str(balance) + " Rupees")
                        else:
                            messagebox.showerror("Negative Balance", "Your account balance is negative.")
                    else:
                        messagebox.showerror("Error", "Account balance not found.")


    b1 = Button(top4, text='Upload Finger print',
                width=20, command=lambda: upload_fileb())
    b1.place(x=20, y=300)

    pinvalue2 = Label(top4, text="Enter your PIN:")
    pinvalue2.place(x=20, y=150)

    textho5 = Label(top4, fg="green")
    textho5.place(x=170, y=400)

    textho3 = Label(top4, fg="green")
    textho3.place(x=170, y=400)

    def submitb():
        su1 = Button(top4, text="SUBMIT", fg="green", command=click)
        su1.place(x=9, y=240)


bt = Button(text="Check balance", bd=5, command=checkb)
bt.place(x=450, y=160)


def ex():
    y = messagebox.askyesno("Exit", "Do you want to exit?")
    if y == True:
        h.destroy()
    else:
        print("no")


exit = Button(text="Exit", bd=1, fg="red", command=ex)
exit.place(x=20, y=500)

bu = Frame(h)
bu.pack(side=BOTTOM)
Label(bu, text="Made by Srinivasan and Team").pack()

h.mainloop()


