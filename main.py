from tkinter import *

from PIL import ImageTk, Image

import tkinter.font as font

from tkinter import messagebox

from instascrape import Reel
import time




# lets create function for download button

def download(link):

    try:

        if link:

            SESSIONID = "41235325%3A5Ni059Bl8d3gbi%3A19" #enter you session id here

            headers = {

                "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WIN64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.75"

                               "Safari/537.36 Edg/79.0.309.43",

                "cookie" : f'sessionId = {SESSIONID}'

            }


            google_reel = Reel(link)

            google_reel.scrape(headers = headers)

            google_reel.download(fp = f".\\reel{int(time.time())}.mp4")

            messagebox.showinfo("Status", "Reel Downloaded Successfully ")

        else:

            messagebox.showwarning("Empty Field", "Please enter the link")

    except Exception as e :

        messagebox.showerror("Error", "Something went wrong Please try again later")
        print(e)


root = Tk()

root.title("Instagram Reel Downloader")

root.minsize(600, 500)

root.maxsize(600, 500)

HEIGHT = 500

WIDTH = 600

FONT = font.Font(family = "Cambria", size = "16", weight = "bold")

(Canvas(root, height= HEIGHT, width=WIDTH)).pack()


frame = Frame(root, bg="pink")

frame.place(relwidth = 1, relheight = 1)


background_image = ImageTk.PhotoImage(Image.open(r"C:\Users\ADMIN\Downloads\imagereel.jpg"))  # image path will be given here

background_label = Label(frame, image = background_image)

background_label.place(relx= -0.25, relwidth = 0.7, relheight= 1)


label1 = Label(frame, text = "Download Instagram Reel", font= FONT, bd= 5, fg="#0d1137", bg="white")

label1.place(relx = 0.48, rely = 0.1, relheight = 0.1)


entry = Entry(frame, font = FONT, fg = "#fbad50")

entry.place(relx=0.48, rely=0.35, relwidth= 0.4, relheight= 0.05)


button1  =  Button(root, text = "Download", font = FONT, bg="white", fg="black", activeforeground = "pink", activebackground = "black",

                   command = lambda:download(entry.get()))  #function for download

button1.place(relx = 0.48, rely = 0.45, relwidth = 0.2, relheight = 0.06)


root.mainloop()


