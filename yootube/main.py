import tkinter
from tkinter.ttk import Progressbar
import customtkinter
from pytube import YouTube

# this is a comment

def startDownload():
    try:
        ytLink = link.get()
        ytObject= YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text= ytObject.title, text_color = "white")
        finishLabel.configure(text = "")
        
        video.download()
        finishLabel.configure(text="Downloaded")
    except:
        finishLabel.configure(text="Download Error", text_color = "red")
    

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded/total_size * 100
    per = str(int(percentage_of_completion))
    print(per)
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    #update progressbar
    progressBar.set(float(percentage_of_completion))

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")


#Adding UI elements
title = customtkinter.CTkLabel(app, text="Insert a Youtube link")
title.pack(padx=10, pady=10)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#progress percentage
pPercentage = customtkinter.CTkLabel(app, text ="0%")
pPercentage.pack()



progressBar = customtkinter.CTkProgressBar(app, width =400)
progressBar.set(0)
progressBar.pack(padx = 10, pady=10)



#download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)



app.mainloop()