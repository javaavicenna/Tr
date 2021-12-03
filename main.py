
import tkinter as tk

def jendelaInput():

    def saveInput():
        nama = inputNama.get()
        nim = inputNIM.get()
        viewerNama.config(state='normal')
        viewerNIM.config(state='normal')
        viewerNama.delete(0, 'end')
        viewerNama.insert(0, nama)
        viewerNIM.delete(0, 'end')
        viewerNIM.insert(0, nim)
        viewerNama.config(state='readonly')
        viewerNIM.config(state='readonly')
        inputWindow.destroy()

    inputWindow = tk.Tk()
    inputWindow.title("Masukkan Nama dan NIM")
    inputWindow.geometry("250x120")
    inputNama = tk.Entry(inputWindow, justify="left")
    inputNIM = tk.Entry(inputWindow, justify="left")

    tk.Label(inputWindow, text="Nama: ").grid(row=0, column=0, sticky=tk.W)
    inputNama.grid(row=0, column=1, sticky=tk. N +tk. E +tk. S +tk.W)
    tk.Label(inputWindow, text="NIM: ").grid(row=1, column=0, sticky=tk.W)
    inputNIM.grid(row=1, column=1, sticky=tk. N +tk. E +tk. S +tk.W)

    tk.Button(inputWindow, text="Simpan Nama", command=saveInput).grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky=tk. E +tk.W)

master = tk.Tk()
master.title("Aplikasi Nama & NIM")
master.geometry("250x120")

viewerNama = tk.Entry(master, justify="left")
viewerNIM = tk.Entry(master, justify="left")

tk.Label(master, text="Nama: ").grid(row=0, column=0, sticky=tk.W)
viewerNama.grid(row=0, column=1, sticky=tk. N +tk. E +tk. S +tk.W)
tk.Label(master, text="NIM: ").grid(row=1, column=0, sticky=tk.W)
viewerNIM.grid(row=1, column=1, sticky=tk. N +tk. E +tk. S +tk.W)

tk.Button(master, text="Masukkan Nama", command=jendelaInput).grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky=tk. E +tk.W)

viewerNama.config(state='readonly')
viewerNIM.config(state='readonly')
tk.mainloop()