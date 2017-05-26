from tkinter import *
from tkinter import ttk
import time
import random

#Se importa tkinter y asignamos a la variable "ventana" el TK, asignandole con
#.geometry, .title, .configure, las medidas, titulo de la ventana y color de tal,
#respectivamente.

#Para subir la imagen del menu, se usa "PhotoImage" y llamamos a la imagen con
#su respectivo formato ".png" y lo pegamos como una etiqueta. Además con place
#se asigna su ubicación en el plano cartesiano.

ventana= Tk()
ventana.geometry("1300x700")
ventana.title("Turtle Fighter")
ventana.configure(bg="light blue")

imagenmenu=PhotoImage(file="menu.png")
Imagen=Label(ventana,image=imagenmenu).place(x=0,y=0)


#Asignamos dos variables con "Stringvar" y con el entry creamos las barras
#de texto para que cada usuario pueda escribir su nombre. Con la respectiva
#ubicación.


jugador1=StringVar()
txtjugador1= Entry(ventana,text=jugador1, width=20).place(x=450,y=300)

jugador2=StringVar()
txtjugador2= Entry(ventana,text=jugador2, width=20).place(x=740,y=300)


#Botones de niveles, para cada boton se asigna una imagen para que se
#vea más estetico, para cada imagen su respectiva ubicacion en el menú

nivel1=PhotoImage(file="nivel1.png")
primernivel=Button(ventana, image=nivel1).place(x=460,y=350)

nivel2=PhotoImage(file="nivel2.png")
segundonivel=Button(ventana, image=nivel2).place(x=460,y=420)

nivel3=PhotoImage(file="nivel3.png")
tercernivel=Button(ventana, image=nivel3).place(x=460,y=490)

nivel4=PhotoImage(file="nivel4.png")
cuartonivel=Button(ventana, image=nivel4).place(x=460,y=560)

nivel5=PhotoImage(file="nivel5.png")
quintonivel=Button(ventana, image=nivel5).place(x=460,y=630)

jugar=PhotoImage(file="jugar.png")
empezar=Button(ventana, image=jugar).place(x=670,y=390)

reanudar=PhotoImage(file="continuar.png")
continuar=Button(ventana, image=reanudar).place(x=678,y=540)


#Ventana toplevel (nivel 1) la cual se define globalizando las posiciones de las imagenes de los personajes
#(ya que se usaran para permitir que se moviera. Se asigna el topleves a la variable "empezar", con ella
# tambien se asigna su tamaño, color y nombre del titulo.

#Se crea un Canvas con la variable "c", en la nueva ventana creada y se le asigna el tamaño, y con .pack()
#permitimos que se mueva.

H=StringVar()
D=StringVar()
Distancia=0
tiempo=100
H2=StringVar()
D2=StringVar()
Distancia2=0
tiempo2=100
def empezar():
    global c,img1,imag1s,img2,imag2s,img3,imag3s,img4,imag4s,img5,imag5s,k,m,comb,tibu,k2,manta2,comb2,tibu2,tiempo,H,Distancia,D, H2,Distancia2,D2,tiempo2
    empezar= Toplevel()
    empezar.geometry("1300x700")
    empezar.configure(bg="light blue")
    empezar.title("NIVEL 1")
    c= Canvas(empezar, width=1300, height= 700)
    c.pack()
    empezar.update()


#ETIQUETAS DE LOS NOMBRES DE LOS JUGADORES
    
#   Se crean las etiquetas respectivas en las cuales llamamos a los "stringVar" para permitir que por
#   medio de una etiqueta se muestre en la ventana hija.

    primerjugador=Label(empezar,textvariable=jugador1,bg='light blue').place(x=620,y=176)
    segundojugador=Label(empezar,textvariable=jugador2,bg='light blue').place(x=620,y=490)
#TIEMPO
    tiempojug1= Label(empezar,textvariable=H,bg='light blue').place(x=640,y=270)
    tiempojug2= Label(empezar,textvariable=H2,bg='light blue').place(x=640,y=580)
#PUNTAJE
    punt1= Label(empezar,textvariable=D,bg='light blue').place(x=640,y=370)
    punt2= Label(empezar,textvariable=D2,bg='light blue').place(x=640,y=670)


#ETIQUETAS DEL CONTADOR DE LA ENERGIA
    contadorenergia=Label(empezar,textvariable=100,bg='light blue').place(x=620,y=270)
    
#Mapa izquierda
    img1= PhotoImage(file="pista1.png")
    imag1s=c.create_image(350,100,image=img1)

#Mapa derecho
    img2= PhotoImage(file="pista1.1.png")
    imag2s=c.create_image(950,100,image=img2)

#Centro
    img3= PhotoImage(file="pistaestatica.png")
    imag3s=c.create_image(650,351,image=img3)

    c.bind("<KeyPress>",tortuga1)
    c.focus_set()

    c.bind("<KeyRelease>",tortuga2)
    c.focus_set()


#PARTES DEL JUGADOR1
    energia_c= PhotoImage(file="energia1.png")
    comb=c.create_image(120,60,image=energia_c)

    img4= PhotoImage(file="jugador1.png")
    imag4s = c.create_image(300,630,image=img4)

    enemigo1= PhotoImage(file="medusa.png")
    num_ale = 125
    k=c.create_image(num_ale,60,image=enemigo1)

    enemigom= PhotoImage(file="manta.png")
    m=c.create_image(120,60,image=enemigom)

    enemigot= PhotoImage(file="tiburon.png")
    tibu=c.create_image(120,60,image=enemigot)



#PARTES DEL JUGADOR2

    img5= PhotoImage(file="jugador2.png")
    imag5s=c.create_image(1000,630,image=img5)

    enemigo12= PhotoImage(file="medusa.png")
    k2=c.create_image(820,60,image=enemigo12)

    enemigom2= PhotoImage(file="manta.png")
    manta2=c.create_image(830,60,image=enemigom2)

    enemigot2= PhotoImage(file="tiburon.png")
    tibu2=c.create_image(820,60,image=enemigot2)

    energia_c2= PhotoImage(file="energia1.png")
    comb2=c.create_image(820,60,image=energia_c2)

    
#MOVIMIENTO MAPA
    while True:
        h()
        enemigo2()
        enemigo3()
        energia()
        Distancia+=1
        D.set(Distancia)
        tiempo-=.1
        H.set(round(tiempo))
        if(tiempo<=0):
            break

        Distancia2+=1
        D2.set(Distancia2)
        tiempo2-=.1
        H2.set(round(tiempo2))
        if (tiempo2<=0):
            break
        h2()
        enemigotib2()
        enemigomant2()
        energia2()

        m1= c.move(imag1s,0,1)
        m2= c.move(imag2s,0,1)
        empezar.update_idletasks()
        empezar.update()
        
        time.sleep(0.0001)
  
#Botón de nivel 1            
nivel1=PhotoImage(file="nivel1.png")
empezar=Button(ventana, image=nivel1, command= empezar).place(x=460,y=350)


#_______________


#_______________


#JUGADOR1

presiono= False
posicionjugx= 0
posicionjugy= 0

def derecha():
    """
    """
    global presiono, imag4s, posicionjugx, posicionjugy
    c.delete(imag4s)
    posicionjugx= posicionjugx + 10
    imag4s=c.create_image(300+posicionjugx,630+posicionjugy,image=img4)

def izquierda():
    """
    """
    global presiono, imag4s, posicionjugx, posicionjugy
    c.delete(imag4s)
    posicionjugx= posicionjugx - 10
    imag4s=c.create_image(300+posicionjugx,630+posicionjugy,image=img4)

def tortuga1(event):
    """
    """
    global imag4s, posicionjugx, posicionjugy
    tecla= repr(event.char)
    if(tecla == "'d'"):
        if(posicionjugx < 170):
            c.delete(imag4s)
            posicionjugx= posicionjugx+10
            imag4s= c.create_image(300+posicionjugx,630+posicionjugy,image=img4)
        else:
            c.delete(imag4s)
            posicionjugx= -170
            imag4s= c.create_image(300+posicionjugx,630+posicionjugy,image=img4)            
    if(tecla == "'a'"):
        if(posicionjugx > -170):
            c.delete(imag4s)
            posicionjugx = posicionjugx - 10
            imag4s = c.create_image(300+posicionjugx,630+posicionjugy,image=img4)
        else:
            c.delete(imag4s)
            imag4s = c.create_image(300+posicionjugx,630+posicionjugy,image=img4)           

#JUGADOR 1________________

#JUGADOR 2_______________

presiono2= False
posicionjugx2= 0
posicionjugy2= 0

            
def derecha():
    """
    """
    global presiono2, imag5s, posicionjugx2, posicionjugy2
    c.delete(imag5s)
    posicionjugx2= posicionjugx2 + 10
    imag5s=c.create_image(300+posicionjugx2,630+posicionjugy2,image=img5)

def izquierda():
    """
    """
    global presiono2, imag4s, posicionjugx2, posicionjugy2
    c.delete(imag5s)
    posicionjugx= posicionjugx - 10
    imag5s=c.create_image(300+posicionjugx2,630+posicionjugy2,image=img5)

def tortuga2(event):
    """
    """
    global imag5s, posicionjugx2, posicionjugy2
    tecla= repr(event.char)
    
    if(tecla == "'l'"):
        if(posicionjugx2 < 170):
            c.delete(imag5s)
            posicionjugx2= posicionjugx2+10
            imag5s= c.create_image(1000+posicionjugx2,630+posicionjugy2,image=img5)
        else:
            c.delete(imag5s)
            posicionjugx2= -1
            imag5s= c.create_image(1000+posicionjugx2,630+posicionjugy2,image=img5)            
    if(tecla == "'j'"):
        if(posicionjugx2 > -170):
            c.delete(imag5s)
            posicionjugx2 = posicionjugx2 - 10
            imag5s = c.create_image(1000+posicionjugx2,630+posicionjugy2,image=img5)
        else:
            c.delete(imag5s)
            imag5s = c.create_image(1000+posicionjugx2,630+posicionjugy2,image=img5)    


def h():
    global num_ale,k
    c.move(k,0,3)
    if(c.coords(k)[1]>1000):
        d=c.coords(k)[0]
        z=random.randint(170,340)
        c.move(k,z-d,-1000)   
   
def enemigo2(): 
    global m
    c.move(m,1,6)
    if(c.coords(m)[1]>1000):
        e=c.coords(m)[0]
        f=random.randint(170,340)
        c.move(m,f-e,-1000)


def enemigo3():
    global tibu,imag4s
    if(c.coords(tibu)[0]>c.coords(imag4s)[0]):
        c.move(tibu,-2,4)
    else:
        c.move(tibu,2,4)
    if(c.coords(tibu)[1]>1000):
        g=c.coords(tibu)[0]
        h=random.randint(170,340)
        c.move(tibu,h-g,-1000)    

def energia():
    global comb
    c.move(comb,0,2)
    if(c.coords(comb)[1]>1000):
        j=c.coords(comb)[0]
        u=random.randint(170,350)
        c.move(comb,u-j,-1000)



def h2():
    global k2
    c.move(k2,0,3)
    if(c.coords(k2)[1]>1000):
        d2=c.coords(k2)[0]
        z2=random.randint(790,1080)
        c.move(k2,z2-d2,-1000)

def enemigomant2():
    global manta2
    c.move(manta2,1,6)
    if(c.coords(manta2)[1]>1000):
        e2=c.coords(manta2)[0]
        f2=random.randint(780,1080)
        c.move(manta2,f2-e2,-1000)


def enemigotib2():
    global tibu2
    if(c.coords(tibu2)[0]>c.coords(imag5s)[0]):
        c.move(tibu2,-2,4)
    else:
        c.move(tibu2,2,4)
    if(c.coords(tibu2)[1]>1000):
        g=c.coords(tibu2)[0]
        h=random.randint(780,1080)
        c.move(tibu2,h-g,-1000)   


def energia2():
    global comb2
    c.move(comb2,0,2)
    if(c.coords(comb2)[1]>1000):
        j2=c.coords(comb2)[0]
        u2=random.randint(780,1080)
        c.move(comb2,u2-j2,-1000)


#Se define la funcion instrucciones, la cual tomá de forma global "imageninstru"

def instrucciones():
    global canvasins,Imageninstru
    ins= Toplevel()
    ins.geometry("1300x700")
    ins.configure(bg="light blue")
    ins.title("INSTRUCCIONES")
    ins.update()

    imagenins=PhotoImage(file="instrucciones.png")
    Imageninstru=Label(ins,image=imagenins).place(x=0,y=0)

    cerrar=PhotoImage(file="cerrar.png")
    destruir=Button(ins, image=cerrar, command=ins.destroy).place(x=420,y=550)
    
    ins.mainloop()
jugar1=PhotoImage(file="jugar.png")
instrucciones1=Button(ventana, image=jugar1, command= instrucciones).place(x=670,y=390)


ventana.mainloop()







