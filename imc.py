import tkinter
from tkinter import *

root = Tk()


class App():
    def __init__(self):

        self.root = root
        self.tela()
        self.frame()
        self.botao()
        self.texto()
        self.grid()
        self.tela2
        self.calculo
        self.framert
        self.botao2
        self.rimc = None

        root.mainloop()

    def tela(self):

        self.root.title("Calculadora de Imc")
        self.root.geometry("450x250+610+153")
        self.root.configure(background="#2e2d2b")
        self.root.resizable(True, True)
        self.root.maxsize(width=625, height=450)
        self.root.minsize(width=375, height=150)

    def tela2(self):

        self.root1 = Tk()
        self.root1.title("Resultado do IMC")
        self.root1.geometry("300x180+610+153")

        self.root1.configure(background="#DCDCDC")
        self.root1.resizable(False, False)
        self.framert()
        self.calculo()
        self.botao2()

    def frame(self):
        self.frame1 = Frame(self.root, bd=4, background="#DCDCDC")
        self.frame1.place(relx=0.02, rely=0.25, relheight=0.96, relwidth=0.96)



        self.frame3 = Frame(self.root, bd=4, background="#2e2d2b")
        self.frame3.place(relx=0.10, rely=0.05, relheight=0.02, relwidth=0.80)

    def framert(self):
        self.frame4 = Frame(self.root1, bd=4, background="#DCDCDC")
        self.frame4.place(relx=0.02, rely=0.02, relheight=0.96, relwidth=0.96)

    def botao(self):
        self.bot1 = Button(self.root, text="Calcular", command=self.tela2)
        self.bot1.place(relx=0.4, rely=0.75, relheight=0.10, relwidth=0.12)

    def botao2(self):
        self.bot2 = Button(self.root1, text="finalizar", command="exit")
        self.bot2.place(relx=0.4, rely=0.75, relheight=0.15, relwidth=0.17)

    def texto(self):
        self.tex = tkinter.Label(self.root, text="CALCULADORA DE IMC", font=('Gotham', 20), bg="#2e2d2b",foreground="#feffff")
        self.tex.place(relx=0.14, rely=0.0)

        self.tex2 = tkinter.Label(self.root, text="Digite sua altura em Metros: ", font=('Gotham', 12), bg="#DCDCDC")
        self.tex2.place(relx=0.10, rely=0.35)

        self.tex3 = tkinter.Label(self.root, text="Digite sua massa em Kg: ", font=('Gotham', 12), bg="#DCDCDC")
        self.tex3.place(relx=0.10, rely=0.55)

    def grid(self):
        self.gd = float
        self.gd = tkinter.Entry(self.root, bd=2, font=("Gotham", 12))
        self.gd.place(relx=0.55, rely=0.35, relwidth=0.20)

        self.gd2 = float
        self.gd2 = tkinter.Entry(self.root, bd=2, font=("Gotham", 12))
        self.gd2.place(relx=0.55, rely=0.55, relwidth=0.20)

    def calculo(self):
        try:
            self.altura = float(self.gd.get())
            self.peso = float(self.gd2.get())

        except:
            erro = tkinter.Label(self.root1, text="erro, digite numeros inteiros", font=('Gotham', 12), bg="#DCDCDC")
            erro.place(relx=0.18, rely=0.30)
            erro2 = tkinter.Label(self.root1, text=" tente '.' no lugar de ','", font=('Gotham', 12), bg="#DCDCDC")
            erro2.place(relx=0.18, rely=0.50)
        else:
            self.resultado = self.peso / self.altura ** 2
            self.resultado1 = "{:.{}f}".format(self.resultado, 2)

            if self.resultado < 18.5:
                self.rimc = "Abaixo do peso"

            elif self.resultado <= 24.9:
                self.rimc = "Peso normal"

            elif self.resultado <= 29.9:
                self.rimc = "Sobrepeso"

            elif self.resultado <= 34.9:
                self.rimc = "Obesidade I"

            elif self.resultado <= 39.9:
                self.rimc = "Obesidade II"

            else:
                self.rimc = "Obesidade III"

            self.txt = tkinter.Label(self.root1, text="Resultado do Imc:", font=('Gotham', 12), bg="#DCDCDC")
            self.txt.place(relx=0.18, rely=0.12)

            self.imc = tkinter.Label(self.root1, text=self.resultado1, font=('Gotham', 12), bg="#DCDCDC")
            self.imc.place(relx=0.18, rely=0.30)

            self.imc = tkinter.Label(self.root1, text=self.rimc, font=('Gotham', 12), bg="#DCDCDC")
            self.imc.place(relx=0.18, rely=0.50)


App()
