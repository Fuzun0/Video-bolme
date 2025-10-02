import tkinter
import os
from moviepy.editor import *
from tkinter import filedialog

Window = tkinter.Tk()

def openFile():
    file = filedialog.askopenfilename()
    if not file:
        return
    clip = VideoFileClip(file)
    folder = os.path.dirname(file)
    filename = os.path.splitext(os.path.basename(file))[0]

    # Görüntü Dosyası
    silent_clip = clip.without_audio()
    silent_video_path = os.path.join(folder, f"{filename}_sessiz.mp4")
    silent_clip.write_videofile(silent_video_path, codec="libx264")

    # Ses Dosyası
    audio_path = os.path.join(folder, f"{filename}.mp3")
    clip.audio.write_audiofile(audio_path)

    print("Sesi olmayan video:", silent_video_path)
    print("MP3 dosyası:", audio_path)

entry = tkinter.Entry(Window)
entry.pack()

button = tkinter.Button(Window, text="dosyayı aç", command=openFile)
button.pack()


Window.mainloop()
