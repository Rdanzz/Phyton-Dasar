# GUI -> Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
# window.resizable(False, False)
window.title("Graphical")

# frame input
inputFrame = ttk.Frame(window)
# penempatan Grid, Pack, Place

inputFrame.pack(padx=10, fill="x", expand=True)

NAMADEPAN = tk.StringVar()
NAMABELAKANG = tk.StringVar()
# component
# 1. Label
namaDepan = ttk.Label(inputFrame, text="Nama Depan")
namaDepan.pack(padx=10, fill="x", expand=True)

# 2. Entry
namaDepanEntry = ttk.Entry(inputFrame, textvariable=NAMADEPAN)
namaDepanEntry.pack(padx=10, fill="x", expand=True)

namaBelakang = ttk.Label(inputFrame, text="Nama Belakang")
namaBelakang.pack(padx=10, fill="x", expand=True)

namaBelakangEntry = ttk.Entry(inputFrame, textvariable=NAMABELAKANG)
namaBelakangEntry.pack(padx=10, fill="x", expand=True)

# Button
def onClick():
    # print(f"Halo, {NAMADEPAN.get()} {NAMABELAKANG.get()}")
    showinfo(title="Notifications", message=f"Halo, {NAMADEPAN.get()} {NAMABELAKANG.get()}")

button = ttk.Button(inputFrame, text="Submit", command=onClick)
button.pack(fill="x", expand=True, padx=10, pady=10)    

window.mainloop()