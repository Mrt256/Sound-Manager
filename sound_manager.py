import pygame
import tkinter as tk
from tkinter import filedialog

pygame.mixer.init()

sounds = {}

def load_sound():
    path = filedialog.askopenfilename(
        title="Select a sound file",
        filetypes=[("Audio Files", "*.wav *.mp3"), ("All Files", "*.*")]
    )
    if path:
        name = path.split("/")[-1]
        sounds[name] = path
        listbox.insert(tk.END, name)

def play_sound():
    selection = listbox.curselection()
    if selection:
        sound_name = listbox.get(selection)
        pygame.mixer.music.load(sounds[sound_name])
        pygame.mixer.music.play()

def stop_sound():
    pygame.mixer.music.stop()

window = tk.Tk()
window.title("Sound Effect Manager")
window.geometry("360x300")
window.configure(bg="#202020")

tk.Label(window, text="Sound Effect Manager", fg="white", bg="#202020", font=("Arial", 14, "bold")).pack(pady=10)

frame = tk.Frame(window, bg="#202020")
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=40, height=8, bg="#303030", fg="white", selectbackground="#505050")
listbox.pack(side=tk.LEFT, padx=5)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

btn_load = tk.Button(window, text="Load Sound", command=load_sound, width=20, bg="#404040", fg="white")
btn_load.pack(pady=5)

btn_play = tk.Button(window, text="Play", command=play_sound, width=20, bg="#404040", fg="white")
btn_play.pack(pady=5)

btn_stop = tk.Button(window, text="Stop", command=stop_sound, width=20, bg="#404040", fg="white")
btn_stop.pack(pady=5)

window.mainloop()
