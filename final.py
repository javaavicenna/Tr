#Nama   : Taufiqul Hakim
#Nim    : 20507334028

from tkinter import *

def jendelaInput():
    second = Tk()
    second.title("Kontrol Temperatur")
    second.geometry("250x120")
    layar_second = Entry(second, justify="center", width=40)
    layar_second.insert(END, "----")
    layar_second.grid(row=0, column=0,columnspan=2 ,padx=2, pady=5,sticky=E +W)

    def tambah():
        suhu = layar_main.get()
        if suhu == "27":
            layar_second.delete(0, END)
            layar_second.insert(0, "Maximum is 27"+"\u00B0")
        else:
            suhu1 = int(suhu) + 1
            layar_main.delete(0, END)
            layar_main.insert(0, suhu1)
            layar_second.delete(0, END)
            layar_second.insert(0, "Temperatur UP")

    def kurang():
        suhu = layar_main.get()
        if suhu == "16":
            layar_second.delete(0, END)
            layar_second.insert(0, "Minimum is 16"+"\u00B0")
        else:
            suhu1 = int(suhu) - 1
            layar_main.delete(0, END)
            layar_main.insert(0, suhu1)
            layar_second.delete(0, END)
            layar_second.insert(0, "Temperatur DOWN")
    Button(second, text="+", command=tambah).grid(row=2, column=0, sticky=E + W)
    Button(second, text="-", command=kurang).grid(row=2, column=1, sticky=E + W)


main=Tk()
main.title("Pengontrol AC")
main.geometry("250x120")
layar_main=Entry(main, justify="center")
layar_main.grid(row=0, column=2, sticky=W+E)
Label(main, text="\u00B0"+"C").grid(row=0, column=3)
layar_main.insert(END, 24)
Label(main, text="Temperatur: ").grid(row=0, column=0, sticky=W)
Button(main, text="Buka Panel", command=jendelaInput, width=30).grid(row=2, column=0, columnspan=5, padx=20, pady=5, sticky=E)

jendelaInput()
mainloop()
