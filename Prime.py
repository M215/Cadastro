from tkinter import *

def btn():
    if (nome.get() != 'matheus') or (senha.get() != 'querino789'):
        lbl3.configure(text='Não pode Entrar',foreground='Red')
    else:
        tela.quit()

tela = Tk()
tela.title('Resgistro')
lbl = Label(tela,text='Ecreva seu nome abaixo:')
lbl.grid(column=0,row=0)

nome = Entry(tela)
nome.grid(column=0,row=1)

lbl2 = Label(tela,text='Ecreva sua senha abaixo:')
lbl2.grid(column=0,row=2)

senha = Entry(tela)
senha.grid(column=0,row=3,pady=10)

bt = Button(tela,text='Enter',command=btn)
bt.grid(column=0,row=4,pady=5)

lbl3 = Label(tela,text='')
lbl3.grid(column=0,row=5)
tela.mainloop()

# no console digite auto-py-to-exe e configure para janela sem console.
# para executar o codigo no sublime ctrl + shift + b