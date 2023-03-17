
from tkinter import *
from tkinter import ttk
import tkinter as ttk

raiz = Tk()

raiz.title("interface ejercicio 2")
raiz.config(bg="black")

mainFramearriba = ttk.Frame(raiz,bg="gray40",width=300)
mainFramearriba.grid(pady=5)

mainFramefondo = ttk.Frame(raiz,bg="black")
mainFramefondo.grid()
#mainFramefondo.config(bg="black")

mainFrameprincipal = ttk.Frame(mainFramefondo,bg="#54312f")
mainFrameprincipal.grid()

mainFrame1 = ttk.Frame(mainFrameprincipal,bg="#54312f")
mainFrame1.grid(sticky=W,padx=5)

mainFrame2 = ttk.Frame(mainFrameprincipal,bg="#54312f")
mainFrame2.grid(column=1,row=0,sticky=E,padx=30)

mainFramefondotabla = ttk.Frame(mainFramefondo,bg="#54312f")
mainFramefondotabla.grid()

mainFrametabla = ttk.Frame(mainFramefondotabla)
mainFrametabla.grid(padx=42,pady=20)

#mainFramearriba
ttk.Label(mainFramearriba, text="Product management",background="gray40",foreground="white",font=("Arial",40,"bold"),width=19).grid(column=1,row=0,sticky=W)
#padx=50
imagen2 = PhotoImage(file="Carrito.png")

btnImagen = ttk.Button(mainFramearriba,borderwidth=0)
btnImagen.grid(column=0,row=0)
btnImagen.configure(background="gray40")
btnImagen['image']=imagen2

#mainFrame1
#primer linea
ttk.Label(mainFrame1, text="Id product:",font=("Arial",14),background="#54312f",fg="white").grid(column=0, row=0,sticky=W,pady=5,padx=25)
idEntry = ttk.Entry(mainFrame1,width=30,font=("Arial", 12, "bold"),background="#54312f", fg="white", justify=CENTER )
idEntry.config(borderwidth=0,highlightthickness=0) # Configura los atributos para hacer el marco invisible
idEntry.grid(column=1,row=0)
ttk.Label(mainFrame1, text="_____________________", bg="#54312f", font=("Arial", 12, "bold"), fg="white").grid(column=1, row=0, padx=10)
#segunda linea
ttk.Label(mainFrame1, text="Name:",font=("Arial",14),background="#54312f",fg="white").grid(column=0, row=1,sticky=W,pady=5,padx=25)
nameEntry = ttk.Entry(mainFrame1,width=30,font=("Arial", 12, "bold"),background="#54312f", fg="white", justify=CENTER)
nameEntry.grid(column=1,row=1)
nameEntry.config(borderwidth=0,highlightthickness=0)
ttk.Label(mainFrame1, text="_____________________", bg="#54312f", font=("Arial", 12, "bold"), fg="white").grid(column=1, row=1, padx=10)
#tercer linea
ttk.Label(mainFrame1, text="Description:",font=("Arial",14),background="#54312f",fg="white").grid(column=0,row=2,sticky=W,pady=5,padx=25)
descripcionEntry = ttk.Entry(mainFrame1,width=30,font=("Arial", 12, "bold"),background="#54312f", fg="white", justify=CENTER)
descripcionEntry.grid(column=1,row=2)
descripcionEntry.config(borderwidth=0,highlightthickness=0)
ttk.Label(mainFrame1, text="_____________________", bg="#54312f", font=("Arial", 12, "bold"), fg="white").grid(column=1, row=2, padx=10)
#cuarta linea
ttk.Label(mainFrame1,text="quantity:",font=("Arial",14),background="#54312f",fg="white").grid(column=0,row=3,sticky=W,pady=5,padx=25)
quantityEntry = ttk.Entry(mainFrame1,width=30,font=("Arial", 12, "bold"),background="#54312f", fg="white", justify=CENTER)
quantityEntry.grid(column=1,row=3)
quantityEntry.config(borderwidth=0,highlightthickness=0)
ttk.Label(mainFrame1, text="_____________________", bg="#54312f", font=("Arial", 12, "bold"), fg="white").grid(column=1, row=3, padx=10)
#quinta linea
ttk.Label(mainFrame1, text="Price:",font=("Arial",14),background="#54312f",fg="white").grid(column=0,row=4,sticky=W,pady=5,padx=25)
priceEntry = ttk.Entry(mainFrame1,width=30,font=("Arial", 12, "bold"),background="#54312f", fg="white", justify=CENTER)
priceEntry.grid(column=1,row=4)
priceEntry.config(borderwidth=0,highlightthickness=0)
ttk.Label(mainFrame1, text="_____________________", bg="#54312f", font=("Arial", 12, "bold"), fg="white").grid(column=1, row=4, padx=10)
#mainFrame2
ttk.Button(mainFrame2,text="Back",width=4,foreground="slate blue",font=("Arial",14),borderwidth=0,background="#54312f").grid(column=0,row=0,sticky=E)
ttk.Button(mainFrame2,text="Save",background="green",foreground="white",font=("Arial",14),width=15).grid(column=0,row=1,pady=10)
ttk.Button(mainFrame2,text="Delete",background="red",foreground="white",font=("Arial",14),width=15).grid(column=0,row=2,pady=3)
ttk.Button(mainFrame2,text="Update",background="orange",foreground="white",font=("Arial",14),width=15).grid(column=0,row=3,pady=17)

imagen = PhotoImage(file="buscar.png")
btnImagen = ttk.Button(mainFrame2,borderwidth=0)
btnImagen.grid(column=0,row=0,sticky=W)
btnImagen.configure(background="#54312f")
btnImagen['image']=imagen

#mainFrametabla
ttk.Label(mainFrametabla, text="idproduit", width=10, bg="gray", fg="white").grid(row=0, column=0)
ttk.Label(mainFrametabla, text="namep", width=20, bg="gray", fg="white").grid(row=0, column=1)
ttk.Label(mainFrametabla, text="description", width=30, bg="gray", fg="white").grid(row=0, column=2)
ttk.Label(mainFrametabla, text="quantity", width=10, bg="gray", fg="white").grid(row=0, column=3)
ttk.Label(mainFrametabla, text="unite_price", width=10, bg="gray", fg="white").grid(row=0, column=4)

data = [
    ("1", "Condia", "lait", "24", "100.0"),
    ("2", "la vache quirit", "fromage", "200", "300.0"),
    ("3", "hamound boualam", "boisson gaseuse", "98", "90.0"),
    ("4", "Mina", "Chocolat", "80", "50.0"),
    ("5", "Aroma", "cafe", "60", "80.0"),
    ("6", "Facto", "Facto", "7000", "600.0"),
    ("", "", "", "", ""),
    ("", "", "", "", ""),
    ("", "", "", "", "")
]

for i, row in enumerate(data):
    for j, item in enumerate(row):
        ttk.Label(mainFrametabla, text=item, width=10 if j == 0 else 20 if j == 1 else 30 if j == 2 else 10 if j == 3 else 10, bg="white").grid(row=i+1, column=j, sticky=(W))

raiz.mainloop()