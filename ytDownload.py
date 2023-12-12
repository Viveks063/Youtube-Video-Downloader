import tkinter
import customtkinter
from pytube import YouTube
import threading

customtkinter.set_appearance_mode("Default")
customtkinter.set_default_color_theme("blue")


def startDownload():
    def download():
        try:
            ytlink = link.get()
            ytObject = YouTube(ytlink)
            video = ytObject.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            if video:
                video.download(filename="downloaded_video.mp4")
                finishLabel.configure(text="Downloaded successfully!")
            else:
                finishLabel.configure(text="Error: No suitable video format found.")
        except Exception as e:
            finishLabel.configure(text=f"Error: {str(e)}")

    download_thread = threading.Thread(target=download)
    download_thread.start()


app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=300, textvariable=url_var)
link.pack()

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

app.mainloop()
