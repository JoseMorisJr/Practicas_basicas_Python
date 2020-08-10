"""
Lanzar 4 dados y quedarme con la suma de los 3 mejores. 
"""

# Importando módulos
from random import randint
from tkinter import Tk, mainloop,Canvas,Frame,Label,Button,W,E


# Lógica del PROGRAMA

## Definir las cualidades del personaje
Qualities = {
            "Fuerza":0,
            "Destreza":0,
            "Constitución":0,
            "Inteligencia":0,
            "Sabiduría":0,
            "Carisma":0
            }

## Función para sumar 3 dados
def launch_dice():
    """" 
    Función que genera números aleatorios, 
    los ordena y suma los primeros 3 valores 
    """    
    dice = [randint(1,6) for _ in range(4)]
        
    dice.sort(reverse=True)
    return sum(dice[:3])

## Función para asignar la suma de dados a la cualidad 

def quality():
    for quality in Qualities:
        Qualities[quality] = launch_dice()
        
quality() #Ejecutamos la función asignandole los puntos a la cualidad

# Interfaz gráfica

## Características de la interfaz
interface = Tk()
interface.title("Conoce tus cualidades")
interface['bg'] = '#f06260'
interface.geometry("300x200")

## Etiqueta dentro de la interfaz
label = Label(interface, text = " Tus cualidades son:")
label.grid()

## Creación de bloques para las cualidades
frame0 = Frame()
frame0.place(relx = 0.2, 
            rely = 0.2)

frame1 = Frame()
frame1.place(relx = 0.6,
             rely = 0.2)

## Función que escribe las cualidades y sus puntos en los bloques
def write():
    for quality,row in zip(Qualities,range(8,56,8)):
        label0 = Label(frame0,
                text=quality)
        label0.grid(row=row, column=0)
        
        label1 = Label(frame1,
                       text=Qualities[quality])
        label1.grid(row=row, column=0)

write() #Ejecutamos la función escribiendo en los bloques

## Creamos una función que sirva para refrescar los puntos
def refresh():
    quality()
    write()

## Creamos el botón para refrescar  
button = Button(frame0, text = "Nuevas cualidades",command=lambda:refresh())
button.grid(row=60,column=0,sticky=W+E)

## Mostramos la interfaz
interface.mainloop()