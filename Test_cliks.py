import tkinter as tk 
from tkinter import *
windows = tk.Tk()

def contador ():
    global clicks
    clicks += 1
    etiqeta1.config(text= f"Clicks {clicks}")
   





def Corretiempo():
   global tiempo, clicks
      
   Empezar.config(state=tk.DISABLED)
   contador.config(state=tk.NORMAL)
   if tiempo > 0:
      tiempo -= 1
      etiquetatiempo.config(text = f"Tiempo Restante: {tiempo}s " )
      windows.after(1000, Corretiempo)
   else:
      
      etiqeta1.config(text = f"Clicks Totales: {clicks}")
      Empezar.config(state =tk.NORMAL)
      contador.config(state=tk.DISABLED)
      clicks = 0

      



    
windows.title("Lista de tarea")
anchoventana = 700
altoventana = 500
anchopantalla = windows.winfo_screenwidth()//3
largopantalla = windows.winfo_screenheight()//8
windows.geometry(f"{anchoventana}x{altoventana}+{anchopantalla}+{largopantalla}")

etiqeta = Label (windows, text="Test de Velocidad de Cliqueo",fg ="black",font= ("Arial",20))
etiqeta.pack(pady=15,fill="x")

etiqeta1 = Label (windows, text=f"Total de clicks: 0",fg ="black",font= ("Arial",15))
etiqeta1.pack(pady=15,fill="x")

etiquetatiempo = Label (windows, text= "Tiempo Restante 30s",fg ="black", font = ("Arial", 13))
etiquetatiempo.pack(pady=15,fill="x")

contador = Button (windows, text="Clikea los mas rapido que puedas",fg= "black",font= ("Arial",14),width=28,height=1,command = contador, state = tk.DISABLED)
contador.place(x=200,y=180)

Empezar = Button (windows, text = "Empezar", fg = "black", font= ("Arial",14), command= Corretiempo)
Empezar.place(x=300,y=250)

clicks = 0
tiempo = 30


windows.mainloop()