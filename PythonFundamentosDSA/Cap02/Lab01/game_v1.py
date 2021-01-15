# Game Ping-Pong

# Importação dos modulos tkinter, random e time

from tkinter import *
import random
import time

# Variavel recebendo o valor antes do jogo iniciar

level = int(input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n"))

# Variavel que define o tamanho da barra pela resposta do usuário a variável level
length = 500/level


# Variaveis que recebem objetos do módulo Tk() 

# Recebe o pacote Tk()
root = Tk()

# Recebe o objeto título
root.title("Ping Pong")

# Recebe o objeto de redimencionamento
root.resizable(0,0)

# Recebe o objeto para os atributos.
root.wm_attributes("-topmost", -1)

# Variaveis que recebem o resultado de funções canvas

canvas = Canvas(root, width=800, height=600, bd=0, highlightthickness=0)
canvas.pack()

root.update()

# Variável

count = 0

# Outra Variável
lost = False

# Classe para criação de funções da Bola

class Bola:

    # Função
    def __init__(self, canvas, Barra, color):

        # Variáveis
        self.canvas = canvas
        self.Barra = Barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)

        # Listas
        starts_x = [-3, -2, -1, 1, 2, 3]

        # Função random para embaralhar a lista
        random.shuffle(starts_x)

        # Variaveis recebendo de outras variaves
        self.x = starts_x[0]
        self.y = -3

        # Mais variaveis recebendo de outras variaveis
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    # Função
    def draw(self):

        # Variável
        self.canvas.move(self.id, self.x, self.y)

        # Variável
        pos = self.canvas.coords(self.id)

        # Condicional IF
        if pos[1] <= 0:

            # Variável menor ou igual do objeto y
            self.y = 3

        # Condicional IF
        if pos[3] >= self.canvas_height:

            # Variável maior ou igual altura do objeto y
            self.y = -3

        # Condicional IF
        if pos[0] <= 0:
            
            # Variável menor ou igual do objeto x
            self.x = 3
        
        # Condicional IF
        if pos[2] >= self.canvas_width:
            
            # Variável maior ou igual da largura do objeto x
            self.x = -3
        
        # Variável que recebe as coordenadas
        self.Barra_pos = self.canvas.coords(self.Barra.id)

        # Condicional IF aninhado para a variavel do objeto da variável anterior
        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:

                # Variaveis de contagem
                self.y = -3
                global count
                count +=1

                # Intância de chamada a função
                score()

        # Condicional IF
        if pos[3] <= self.canvas_height:

            # Variável 
            self.canvas.after(10, self.draw)
        
        # Condicional ELSE
        else:

            # Chamada a Função abaixo
            game_over()

            # Variaveis da chamada a função game_over()
            global lost
            lost = True


# Classe para criação de funções Barra

class Barra:

    # Função 
    def __init__(self, canvas, color):

        # Variaveis para criação da barra
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)
        self.canvas.move(self.id, 200, 400)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    # Função
    def draw(self):

        # Chamada ao método de movimentação
        self.canvas.move(self.id, self.x, 0)

        # Variável
        self.pos = self.canvas.coords(self.id)

        # Condicional IF
        if self.pos[0] <= 0:

            # Variável
            self.x = 0
        
        # Condicional IF
        if self.pos[2] >= self.canvas_width:
            
            # Variável
            self.x = 0
        
        # Variável global
        global lost
        
        # Condicional IF para operação a variável global
        if lost == False:
            self.canvas.after(10, self.draw)

    # Função de movimentação para esquerda
    def move_left(self, event):

        # Condicional IF
        if self.pos[0] >= 0:

            # Variável
            self.x = -3

    # Função de movimentação para direita
    def move_right(self, event):

        # Condicional IF
        if self.pos[2] <= self.canvas_width:

            # Variável
            self.x = 3

# Função
def start_game(event):

    # Variaveis
    global lost, count
    lost = False
    count = 0

    # Função de Pontos no jogo
    score()

    # Variável do resultado de outra função
    canvas.itemconfig(game, text=" ")

    # Métodos herdados
    time.sleep(1)
    Barra.draw()
    Bola.draw()

# Função de Pontos no game
def score():
    canvas.itemconfig(score_now, text="Pontos: " + str(count))

# Função de Fim de Jogo no game

def game_over():
    canvas.itemconfig(game, text="Game over!")

# Variável recebendo o objeto bola
Barra = Barra(canvas, "orange")

# Variável recebendo o objeto barra
Bola = Bola(canvas, Barra, "purple")

# Variável recebendo uma função
score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill = "green", font=("Arial", 16))

# Variável recebendo uma função
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))

# Variável recebendo uma função
canvas.bind_all("<Button-1>", start_game)

# Objeto de execução do game.
root.mainloop()
