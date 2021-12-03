
import tkinter as tk

def jendelaInput():

    def saveInput():
        suhu = inputsuhu.get()
        viewersuhu.config(state='normal')
        viewersuhu.insert(0, "24"+"\u00B0")

        viewersuhu.config(state='readonly')

    def tambah():
        suhu = inputsuhu.get()
        if suhu == 27:
            viewersuhu.config(state='normal')
            viewersuhu.delete(0, suhu)
            viewersuhu.insert(0, "maximum is 27 ", "\u00B0")


    inputWindow = tk.Tk()
    inputWindow.title("Kontrol Temperatur")
    inputWindow.geometry("250x120")
    inputsuhu = tk.Entry(inputWindow, justify="center", width=40)

    tk.Button(inputWindow, text="+", command=tambah).grid(row=2, column=0, sticky=tk.E + tk.W)
    tk.Button(inputWindow, text="-").grid(row=2, column=1, sticky=tk.E + tk.W)
    inputsuhu.grid(row=0, column=0,columnspan=2 ,padx=2, pady=5,sticky=tk. E +tk.W)
    saveInput()



master = tk.Tk()
master.title("Pengontrol AC")
master.geometry("250x120")

viewersuhu = tk.Entry(master, justify="center")

tk.Label(master, text="Temperatur: ").grid(row=0, column=0, sticky=tk.W)
viewersuhu.grid(row=0, column=2, sticky=tk.W+tk.E)


tk.Button(master, text="Buka Panel", command=jendelaInput, width=30).grid(row=2, column=0, columnspan=5, padx=20, pady=5, sticky=tk.E)

viewersuhu.config(state='readonly')
jendelaInput()
tk.mainloop()