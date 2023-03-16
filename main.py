import tkinter
import customtkinter
from pytube import YouTube
import os

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title)
        video.download()
        finishLabel.configure(text="Download Complete",text_color="green")
    except:
        finishLabel.configure(text="Download Error",text_color="red")

def startConvertion():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_audio_only()
        title.configure(text=ytObject.title)
        destination = '.'
        out_file = video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        finishLabel.configure(text="Download Complete",text_color="green")
    except:
        finishLabel.configure(text="Download Error",text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    progressBar.set(float(percentage_of_completion) / 100)

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#App Frame
app = customtkinter.CTk();
app.geometry("720x480")
app.title("Makkunii | Youtube Downloader")

#UI Elemetents
title = customtkinter.CTkLabel(app, text="Insert a Youtube Link")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)



downloadvideo = customtkinter.CTkButton(app, width=350, height=40, text="Download Video", command=startDownload)
downloadmusic = customtkinter.CTkButton(app, width=350, height=40, text="Convert to Mp3", command=startConvertion)
downloadmusic.pack(padx=10,pady=0)
downloadvideo.pack(padx=10,pady=5)



# Run App
app.mainloop();
