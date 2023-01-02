# importing the required modules here.
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from colorthief import ColorThief
import os
import pyperclip

# creating the button functions here.
def select_image():
    global filename

    try:
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),
        title="Select Image File", filetype = (("PNG file", "*.png"),
                                                ("JPG file", "*.jpg"),
                                                ("ALL file", "*.txt")))
        img = Image.open(filename)
        img = img.resize((240, 230))
        img = ImageTk.PhotoImage(img)

        lbl.configure(image = img, width = 240, height = 230)
        lbl.image = img
    
    except:
        pass

def find_colors():
    global hexcodes

    try:
        ct = ColorThief(filename)
        palette = ct.get_palette(color_count = 11)

        # getting the rgbs values here and storing them in a list of rgbs.
        rgbs = list()
        for i in range(10):
            rgb = palette[i]
            rgbs.append(rgb)

        # converting the rgbs into hex values here.
        hexcodes = list()
        for i in rgbs:
            color = f"#{i[0]:02x}{i[1]:02x}{i[2]:02x}"
            hexcodes.append(color)

        # printing the respective hex values for the rgbs here. backend!
        for i in range(10):
            print(f"{rgbs[i]} = {hexcodes[i]}")

        # changing the colors here according to the fetched hex values in the button.
        for i in range(10):
            btns_list[i].configure(bg = f"{hexcodes[i]}")
        
        # creating the labels over the image here.
        canvas.create_text(167, 187, text = f"{hexcodes[0]}", fill = "black", font = ('arial', 18, 'bold'))
        canvas.create_text(167, 227, text = f"{hexcodes[1]}", fill = "black", font = ('arial', 18, 'bold'))
        canvas.create_text(167, 267, text = f"{hexcodes[2]}", fill = "black", font = ('arial', 18, 'bold'))
        canvas.create_text(167, 307, text = f"{hexcodes[3]}", fill = "black", font = ('arial', 18, 'bold'))
        canvas.create_text(167, 347, text = f"{hexcodes[4]}", fill = "black", font = ('arial', 18, 'bold'))    

        canvas.create_text(348, 187, text = f"{hexcodes[5]}", fill = "black", font = ('arial', 18, 'bold'))
        canvas.create_text(348, 227, text = f"{hexcodes[6]}", fill = "black", font = ('arial', 18, 'bold'))
        canvas.create_text(348, 267, text = f"{hexcodes[7]}", fill = "black", font = ('arial', 18, 'bold'))
        canvas.create_text(348, 307, text = f"{hexcodes[8]}", fill = "black", font = ('arial', 18, 'bold'))
        canvas.create_text(348, 347, text = f"{hexcodes[9]}", fill = "black", font = ('arial', 18, 'bold'))
    
    except:
        messagebox.showerror("File Not Found", "Please Select An Image First !")

def copy_return1():
    value = hexcodes[0]
    pyperclip.copy(value)
    messagebox.showinfo("Color Copied", f"{value} Copied Successfully !")

def copy_return2():
    value = hexcodes[1]
    pyperclip.copy(value)
    messagebox.showinfo("Color Copied", f"{value} Copied Successfully !")

def copy_return3():
    value = hexcodes[2]
    pyperclip.copy(value)
    messagebox.showinfo("Color Copied", f"{value} Copied Successfully !")

def copy_return4():
    value = hexcodes[3]
    pyperclip.copy(value)
    messagebox.showinfo("Color Copied", f"{value} Copied Successfully !")

def copy_return5():
    value = hexcodes[4]
    pyperclip.copy(value)
    messagebox.showinfo("Color Copied", f"{value} Copied Successfully !")

def copy_return6():
    value = hexcodes[5]
    pyperclip.copy(value)
    messagebox.showinfo("Color Copied", f"{value} Copied Successfully !")

def copy_return7():
    value = hexcodes[6]
    pyperclip.copy(value)
    messagebox.showinfo("Color Copied", f"{value} Copied Successfully !")

def copy_return8():
    value = hexcodes[7]
    pyperclip.copy(value)
    messagebox.showinfo("Color Copied", f"{value} Copied Successfully !")

def copy_return9():
    value = hexcodes[8]
    pyperclip.copy(value)
    messagebox.showinfo("Color Copied", f"{value} Copied Successfully !")

def copy_return10():
    value = hexcodes[9]
    pyperclip.copy(value)
    messagebox.showinfo("Color Copied", f"{value} Copied Successfully !")
        
# creating the window here.
window = Tk()
window.title("Color Finder")
width = 800
height = 500
window.geometry(f"{width}x{height}")
window.configure(bg = "#ffffff")
window.resizable(False, False)

# setting the app icon here.
window.iconbitmap("logo.ico")

# placing the window at the center of the screen here.
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width / 2) - (width / 2)
y_coordinate = (screen_height / 2) - (height / 2)
window.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))

# creating the canvas here for the window here.
canvas = Canvas(window,bg = "#ffffff",height = 500,width = 800,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

# creating the image here to set in the above canvas.
background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(400.0, 250.0,image=background_img)

# creating the button-1 here.
img0 = PhotoImage(file = f"img0.png")
b0 = Button(image = img0,borderwidth = 0,background = "#0F016A",activebackground = "#0F016A",highlightthickness = 0,command = find_colors,relief = "flat")
b0.place(x = 610, y = 368,width = 109,height = 25)

# creating the button-2 here.
img1 = PhotoImage(file = f"img1.png")
b1 = Button(image = img1,borderwidth = 0,highlightthickness = 0,background = "#67014C",activebackground = "#67014C",command = select_image,relief = "flat")
b1.place(x = 477, y = 368,width = 109,height = 25)

# creating the square buttons for the colors here.
btn1 = Button(text = " ", bg = "white", activebackground='black', relief='flat', command = copy_return1)
btn2 = Button(text = " ", bg = "white", activebackground='black', relief='flat', command = copy_return2)
btn3 = Button(text = " ", bg = "white", activebackground='black', relief='flat', command = copy_return3)
btn4 = Button(text = " ", bg = "white", activebackground='black', relief='flat', command = copy_return4)
btn5 = Button(text = " ", bg = "white", activebackground='black', relief='flat', command = copy_return5)

btn6 = Button(text = " ", bg = "white", activebackground='black', relief='flat', command = copy_return6)
btn7 = Button(text = " ", bg = "white", activebackground='black', relief='flat', command = copy_return7)
btn8 = Button(text = " ", bg = "white", activebackground='black', relief='flat', command = copy_return8)
btn9 = Button(text = " ", bg = "white", activebackground='black', relief='flat', command = copy_return9)
btn10 = Button(text = " ", bg = "white", activebackground='black', relief='flat', command = copy_return10)

btns_list = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10]

# packing the buttons here.
btn1.place(x = 80, y = 172,width = 34,height = 34)
btn2.place(x = 80, y = 212,width = 34,height = 34)
btn3.place(x = 80, y = 252,width = 34,height = 34)
btn4.place(x = 80, y = 292,width = 34,height = 34)
btn5.place(x = 80, y = 332,width = 34,height = 34)

btn6.place(x = 261, y = 172,width = 34,height = 34)
btn7.place(x = 261, y = 212,width = 34,height = 34)
btn8.place(x = 261, y = 252,width = 34,height = 34)
btn9.place(x = 261, y = 292,width = 34,height = 34)
btn10.place(x = 261, y = 332,width = 34,height = 34)

# creating the select image frame here.
selectimage = Frame(canvas, width = 240, height = 230, bg = "white", relief = GROOVE)
selectimage.place(x = 477, y = 88)
# creating the label to hold the coming image here.
lbl = Label(selectimage, bg = "white")
lbl.place(x = 0, y = 0)

# running the window in loop here.
window.mainloop()