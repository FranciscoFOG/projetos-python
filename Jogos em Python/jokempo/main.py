# jogo Pedra Papel e Tesoura

from tkinter import *
from tkinter import ttk

# importando o pillow
from PIL import Image, ImageTk

import random


# cores ----------------------
co0 = "#FFFFFF" # white / branca
co1 = "#333333" # black / preto
co2 = "#fcc058" # orange / laranja
co3 = "#fff873" # yellow / amarelo
co4 = "#34eb3d" # greem / verde
co5 = "#e85151" # red / vermelho
co6 = "#fcc058" # orenge / laranja                       
fundo = "#3b3b3b"

# configurando a janela
janela = Tk()
janela.title('')
janela.geometry('360x380')
janela.configure(bg=fundo)


# dividindo a janela

frame_cima = Frame(janela, width=360, height=160, bg=co1, relief='raised')
frame_cima.grid(row = 0, column = 0, sticky=NW)
frame_baixo = Frame(janela, width=360, height=200, bg=co0, relief='flat')
frame_baixo.grid(row = 1, column = 0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# configurando o frame cima

app_1 = Label(frame_cima, text="Player 1", height=5, anchor='center', font=('Ivy 15 bold'), bg=co1, fg=co0)
app_1.place(x=25, y=70)
app_1_linha = Label(frame_cima, text="", height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_1_linha.place(x=0, y=0)

app_1_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('Ivy 50 bold'), bg=co1, fg=co0)
app_1_pontos.place(x=40, y=20)

app_ = Label(frame_cima, text=":", height=1, anchor='center', font=('Ivy 50 bold'), bg=co1, fg=co0)
app_.place(x=170, y=20)

app_2_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('Ivy 50 bold'), bg=co1, fg=co0)
app_2_pontos.place(x=260, y=20)

app_2 = Label(frame_cima, text="CPU", height=3, anchor='center', font=('Ivy 15 bold'), bg=co1, fg=co0)
app_2.place(x=275, y=95)
app_2_linha = Label(frame_cima, text="", height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_2_linha.place(x=355, y=0)

app_linha = Label(frame_cima, text="", width=360, anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co0)
app_linha.place(x=0, y=155)

app_cpu = Label(frame_baixo, text="", height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_cpu.place(x=260, y=10)


global player1
global cpu
global rodadas
global pontos_player1
global pontos_cpu

pontos_player1 = 0
pontos_cpu = 0
rodadas = 5

# função lógica do jogo

def jogar(i):
    global rodadas
    global pontos_player1
    global pontos_cpu

    if rodadas >0:
        print(rodadas)
        opcoes = ['Pedra', 'Papel', 'Tesoura']
        cpu = random.choice(opcoes)
        player1 = i

        app_cpu['text'] = cpu
        app_cpu['fg'] = co1

        # caso jogue igual
        if player1 == 'Pedra' and cpu == 'Pedra':
            print('empate')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3
        
        elif player1 == 'Papel' and cpu == 'Papel':
            print('empate')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3

        elif player1 == 'Tesoura' and cpu == 'Tesoura':
            print('empate')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3

        # jogando na sequência
        elif player1 == 'Pedra' and cpu == 'Papel':
            print('CPU ganhou')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co4
            app_linha['bg'] = co3

            pontos_cpu += 10

        elif player1 == 'Pedra' and cpu == 'Tesoura':
            print('Voce ganhou')
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3

            pontos_player1 += 10

        elif player1 == 'Papel' and cpu == 'Tesoura':
            print('CPU ganhou')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co4
            app_linha['bg'] = co3

            pontos_cpu += 10

        # jogando sequência inversa

        elif player1 == 'Tesoura' and cpu == 'Papel':
            print('Voce ganhou')
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3

            pontos_player1 += 10

        elif player1 == 'Tesoura' and cpu == 'Pedra':
            print('CPU ganhou')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co4
            app_linha['bg'] = co3

            pontos_cpu += 10

        elif player1 == 'Papel' and cpu == 'Pedra':
            print('Voce ganhou')
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3

            pontos_player1 += 10

        # atualizando a pontuação
        app_1_pontos['text'] = pontos_player1
        app_2_pontos['text'] = pontos_cpu

        # atualizando numero de rodadas

        rodadas -= 1

    else:
        app_1_pontos['text'] = pontos_player1
        app_2_pontos['text'] = pontos_cpu

        # chamando a função terminar
        fim_do_jogo()

# função iniciar jogo
def iniciar_jogo():
    global icon_1
    global icon_2
    global icon_3
    global b_icon_1
    global b_icon_2
    global b_icon_3

    b_jogar.destroy()

    icon_1 = Image.open('imagens/pedra.png')
    icon_1 = icon_1.resize((60,60), Image.Resampling.LANCZOS)
    icon_1 = ImageTk.PhotoImage(icon_1)
    b_icon_1 = Button(frame_baixo, command=lambda: jogar('Pedra'), width=50, image=icon_1, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_1.place(x=30, y=60)

    icon_2 = Image.open('imagens/papel.png')
    icon_2 = icon_2.resize((60,60), Image.Resampling.LANCZOS)
    icon_2 = ImageTk.PhotoImage(icon_2)
    b_icon_2 = Button(frame_baixo, command=lambda: jogar('Papel'), width=50, image=icon_2, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_2.place(x=150, y=60)

    icon_3 = Image.open('imagens/tesoura.png')
    icon_3 = icon_3.resize((60,60), Image.Resampling.LANCZOS)
    icon_3 = ImageTk.PhotoImage(icon_3)
    b_icon_3 = Button(frame_baixo, command=lambda: jogar('Tesoura'), width=50, image=icon_3, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_3.place(x=270, y=60)

# função terminar o jogo

def fim_do_jogo():
    global rodadas
    global pontos_player1
    global pontos_cpu
    
    # reiniciando as variáveis para zero
    pontos_player1 = 0
    pontos_cpu = 0
    rodadas = 5

    # destruindo os botões de opção
    b_icon_1.destroy()
    b_icon_2.destroy()
    b_icon_3.destroy()

    # definindo o vencedor
    jogador_player1 = int(app_1_pontos['text'])
    jogador_cpu = int(app_2_pontos['text'])

    if jogador_player1 > jogador_cpu:
        app_vencedor = Label(frame_baixo, text="Parabéns você ganhou !!!", height=1, anchor='center', font=('Ivy 15 bold'), bg=co0, fg=co4)
        app_vencedor.place(x=40, y=60)
    elif jogador_player1 < jogador_cpu:
        app_vencedor = Label(frame_baixo, text="Infelizmente você perdeu !!!", height=1, anchor='center', font=('Ivy 15 bold'), bg=co0, fg=co5)
        app_vencedor.place(x=40, y=60)
    else:
        app_vencedor = Label(frame_baixo, text="Foi um empate !!!", height=1, anchor='center', font=('Ivy 15 bold'), bg=co0, fg=co1)
        app_vencedor.place(x=40, y=60)

    # jogar novamente
    def jogar_novamente():
        app_1_pontos['text'] = '0'
        app_2_pontos['text'] = '0'
        app_vencedor.destroy()

        b_jogar_novamente.destroy()

        iniciar_jogo()

    b_jogar_novamente = Button(frame_baixo, command=jogar_novamente, width=30, text='Jogar novamente', bg=fundo, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
    b_jogar_novamente.place(x=50, y=150)    


# configurando botão jogar
b_jogar = Button(frame_baixo, command=iniciar_jogo, width=30, text='Jogar', bg=fundo, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
b_jogar.place(x=50, y=150)

janela.mainloop()