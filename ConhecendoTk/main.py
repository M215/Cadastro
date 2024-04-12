from customtkinter import *

set_appearance_mode('dark')
set_default_color_theme('blue')

def Autenticar():
    if email.get() == 'querino--matheus@outlook.com' and senha.get() == 'querino789' :
        tela.quit()
    else:
        texto.configure(text='Acesso Negado',text_color='red')

tela  = CTk()
tela.title('Minha Janela')
tela.geometry('300x150')

email = CTkEntry(tela,width=200,placeholder_text='Seu Email:')
email.pack(pady = 5)

senha = CTkEntry(tela,width=200,placeholder_text='Sua Senha:',show = '*')
senha.pack(pady = 5)

botao = CTkButton(tela,width=200,text='Entrar',command=Autenticar)
botao.pack(pady=5)

texto = CTkLabel(tela,text='')
texto.pack()

tela.mainloop()

