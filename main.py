from tkinter import *
import random
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from math import sqrt
import matplotlib.pyplot as plt
GrafBI=[]
GrafT=[]
GrafXi=[]
GrafYi=[]
ControlBi=[]
ControlT=[]
ControlB=[]
EstaticoB=0
Campo=1
varPart=0
Zn=0
varEspec=0
verdadZN=0
Interacion=0
varZn=0
varV=random.random()
vargb=0
def Determina_colicion():
    varMo= float(textMo.get("1.0","end"))
    varQ=  float(textQ.get("1.0","end"))
    varb = float(textb.get("1.0", "end"))
    global vargb
    global Control
    global Campo
    if (Campo==varb):
        vargb = varb
        varXi = random.uniform(-10, 10)
        varYi = random.uniform(-10 - (varb / 2), 10 + (varb / 2))
        # LAbels
        labelV = tk.Label(root, text=varV)
        labelV.pack()
        labelV.place(x=70, y=160, width=150, height=30)
        labelXiR = tk.Label(root, text=varXi)
        labelXiR.pack()
        labelXiR.place(x=70, y=200, width=150, height=30)
        labelYiR = tk.Label(root, text=varYi)
        labelYiR.pack()
        labelYiR.place(x=70, y=240, width=150, height=30)
        global Zn
        Zn += 1
        textZn = tk.Label(root, text=Zn)
        textZn.pack()
        textZn.place(x=150, y=440, width=150, height=30)
        global varPart
        global varEspec
        global GrafT
        global GrafBI
        global GrafXi
        global GrafYi
        if (varXi ** 2 + ((varYi - (varb / 2)) ** 2) <= 100):
            if (varXi ** 2 + ((varYi + (varb / 2)) ** 2) <= 100):
                #print("participante")
                varPart += 1
                labelPartR = tk.Label(root, text=varPart)
                labelPartR.pack()
                labelPartR.place(x=150, y=400, width=150, height=30)
                GrafXi.append(varXi)
                GrafYi.append(varYi)
                grafica_colicion()
            else:
                #print("espectador")
                Moqv = varMo * varQ * varV
                div = (1 - varV ** 2) / ((1 + varV ** 2) ** (3 / 2))
                XiYi = (1) / (((varXi * (10 ** -15)) ** 2) + ((varYi * (10 ** -15)) ** 2))
                varBi = Moqv * div * XiYi * (3 * 10 ** 8)
                GrafBI.append(varBi)
                GrafT.append(sqrt((varXi) ** 2 + (varYi) ** 2) / varV)
                print(GrafBI)
                print(GrafT)
                grafica()
                labelBiR = tk.Label(root, text=varBi)
                labelBiR.pack()
                labelBiR.place(x=70, y=280, width=150, height=30)
                varEspec += 1
                labelEspR = tk.Label(root, text=varEspec)
                labelEspR.pack()
                labelEspR.place(x=150, y=360, width=150, height=30)

                GrafXi.append(varXi)
                GrafYi.append(varYi)
                grafica_colicion()
        if (varXi ** 2 + ((varYi + (varb / 2)) ** 2) <= 100):
            if (varXi ** 2 + ((varYi - (varb / 2)) ** 2) <= 100):
                print("r")
            else:
                #print("Espectador")
                Moqv = varMo * varQ * varV
                div = (1 - varV ** 2) / ((1 + varV ** 2) ** (3 / 2))
                XiYi = (1) / (((varXi * (10 ** -15)) ** 2) + ((varYi * (10 ** -15)) ** 2))
                varBi = Moqv * div * XiYi * (3 * 10 ** 8)
                GrafBI.append(varBi)
                GrafT.append(sqrt((varXi) ** 2 + (varYi) ** 2) / varV)
                print(GrafBI)
                print(GrafT)
                grafica()
                labelBiR = tk.Label(root, text=varBi)
                labelBiR.pack()
                labelBiR.place(x=70, y=280, width=150, height=30)
                varEspec += 1
                labelEspR = tk.Label(root, text=varEspec)
                labelEspR.pack()
                labelEspR.place(x=150, y=360, width=150, height=30)
                GrafXi.append(varXi)
                GrafYi.append(varYi)
                grafica_colicion()
        else:
            print("No Entro")
        global verdadZN
        verdadZN=varPart+varEspec
        labelPartR = tk.Label(root, text=verdadZN)
        labelPartR.pack()
        labelPartR.place(x=70, y=320, width=150, height=30)
    else:
        global ControlBi
        global ControlT
        global ControlB
        global EstaticoB
        EstaticoB=Campo
        Campo=varb
        ControlBi.append(sum(GrafBI))
        ControlT.append(sum(GrafT))
        ControlB.append(EstaticoB*5)
        GrafT.clear()
        GrafBI.clear()
        GrafXi.clear()
        GrafYi.clear()
        Zn=0
        verdadZN=0
        varEspec=0
        varPart=0
        labelEspR = tk.Label(root, text=varEspec)
        labelEspR.pack()
        labelEspR.place(x=150, y=360, width=150, height=30)
        labelPartR = tk.Label(root, text=varPart)
        labelPartR.pack()
        labelPartR.place(x=150, y=400, width=150, height=30)
        textZn = tk.Label(root, text=Zn)
        textZn.pack()
        textZn.place(x=150, y=440, width=150, height=30)
        labelPartR = tk.Label(root, text=verdadZN)
        labelPartR.pack()
        labelPartR.place(x=70, y=320, width=150, height=30)
        grafica_Perfil_colicion()
        grafica_Porcentaje_colicion()


def salir():
    root.destroy()
def grafica():
    global GrafT
    global GrafBI
    figura=Figure(figsize=(5, 2), dpi=100)
    figura.add_subplot(111).plot(GrafT, GrafBI, "o")
    figura.add_subplot(111).plot(0, 0, "white")
    figura.suptitle("Perfil De Campo Magnético (T)")
    ax = figura.add_subplot(111)
    ax.set_xlabel('t(fm/c)')
    ax.set_ylabel('Bi(T)')
    canvas = FigureCanvasTkAgg(figura, root)
    canvas.get_tk_widget().place(x=450, y=50, width=1000, height=850)
def grafica_colicion():
    global GrafT
    global GrafBI
    figura = Figure(figsize=(5, 2), dpi=100)
    figura.add_subplot(111).plot(0, 0, "white")
    figura.add_subplot(111).plot(GrafXi, GrafYi, "o")
    figura.suptitle("Colisión")
    ax=figura.add_subplot(111)
    ax.set_xlabel('Xi(fm)')
    ax.set_ylabel('Yi(fm)')

    circulo=plt.Circle((0,vargb/2),10 ,color="r",fill=False)
    circulo2 = plt.Circle((0, -vargb/2), 10, color="g",fill=False)
    figura.gca().add_artist(circulo)
    figura.gca().add_artist(circulo2)

    canvas = FigureCanvasTkAgg(figura, root)
    canvas.get_tk_widget().place(x=1475, y=500, width=400, height=400)

def grafica_Perfil_colicion():
    global GrafT
    global GrafBI
    figura = Figure(figsize=(5, 2), dpi=100)
    figura.add_subplot(111).plot(0, 0, "white")
    figura.add_subplot(111).plot(ControlT, ControlBi, "o")
    figura.suptitle("Campo Magnético Respecto al Parámetro")
    ax = figura.add_subplot(111)
    ax.set_xlabel('t(fm/c)')
    ax.set_ylabel('Bi(T)')
    canvas = FigureCanvasTkAgg(figura, root)
    canvas.get_tk_widget().place(x=1475, y=50, width=400, height=400)

def grafica_Porcentaje_colicion():
    global GrafT
    global GrafBI
    figura = Figure(figsize=(5, 2), dpi=100)
    figura.add_subplot(111).plot(0, 0, "white")
    figura.add_subplot(111).plot(ControlB, ControlBi, "o")
    figura.suptitle("Porcentaje de Colisión")
    ax = figura.add_subplot(111)
    ax.set_xlabel('b(%)')
    ax.set_ylabel('Bi(T)')
    canvas = FigureCanvasTkAgg(figura, root)
    canvas.get_tk_widget().place(x=20, y=500, width=400, height=400)
    print("control BI", ControlBi)
    print("Control t", ControlT)
    print("Control b", ControlB)

    #diseño de frame
root = Tk()
root.title("Campo Magnetico")
root.attributes('-fullscreen', True)
root.resizable(1,1)
root.iconbitmap('icono.png')

grafica()
grafica_colicion()
grafica_Perfil_colicion()
grafica_Porcentaje_colicion()
print(GrafBI)
frame = Frame(root, width=1200, height=400)

frame.config(cursor="arrow")
frame.config(bg="blue")
frame.config(bd=20)
root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")

#label
labelMo=tk.Label(root,text="Mo:")
labelMo.pack()
labelMo.place(x=20, y=40, width=30, height=30)

labelQ=tk.Label(root,text="q:")
labelQ.pack()
labelQ.place(x=20, y=80, width=30, height=30)

labelb=tk.Label(root,text="b:")
labelb.pack()
labelb.place(x=20, y=120, width=30, height=30)

labelV=tk.Label(root,text="V:")
labelV.pack()
labelV.place(x=20, y=160, width=30, height=30)


labelXi=tk.Label(root,text="Xi:")
labelXi.pack()
labelXi.place(x=20, y=200, width=30, height=30)


labelYi=tk.Label(root,text="Yi:")
labelYi.pack()
labelYi.place(x=20, y=240, width=30, height=30)

labelBi=tk.Label(root,text="Bi:")
labelBi.pack()
labelBi.place(x=20, y=280, width=30, height=30)

labelZn=tk.Label(root,text="Zn:")
labelZn.pack()
labelZn.place(x=20, y=320, width=30, height=30)

labelEsp=tk.Label(root,text="Espectadores:")
labelEsp.pack()
labelEsp.place(x=20, y=360, width=100, height=30)

labelPart=tk.Label(root,text="Participadores:")
labelPart.pack()
labelPart.place(x=20, y=400, width=100, height=30)

labelPart=tk.Label(root,text="Total de intentos:")
labelPart.pack()
labelPart.place(x=20, y=440, width=100, height=30)

#cajas de texto
textMo=tk.Text(root, height=3, width=40,)
textMo.insert(tk.INSERT,10**-7)
textMo.pack()
textMo.place(x=70, y=40, width=150, height=30)

textQ=tk.Text(root, height=3, width=40)
textQ.insert(tk.INSERT,1.6*10**-19)
textQ.pack()
textQ.place(x=70, y=80, width=150, height=30)

textb=tk.Text(root, height=3, width=40)
textb.insert(tk.INSERT,1)
textb.pack()
textb.place(x=70, y=120, width=150, height=30)



#botones
btnRead=tk.Button(root, height=1, width=10, text="Iniciar",command=Determina_colicion,bg="green",fg="white")
btnRead.pack()
btnRead.place(x=800, y=950, width=100, height=100)

btnSalir=tk.Button(root, height=1, width=10, text="Salir",command=salir,bg="red",fg="white")
btnSalir.pack()
btnSalir.place(x=1000, y=950, width=100, height=100)
root.mainloop()
