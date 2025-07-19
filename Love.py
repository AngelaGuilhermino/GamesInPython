import turtle # Permite desenhar na tela

def draw_heart(turtle, size, color): # Função para desenhar coração
    turtle.begin_fill()
    turtle.color(color)
    ''' O cursor gira 140° e se desloca para frente, desenhando metade 
    de um circulo curvado para a esquerda e formando metade do coração
    '''
    turtle.left(140) 
    turtle.forward(size)
    turtle.circle(-size // 2, 200)

    # Forma a outra metade do coração
    turtle.left(120)
    turtle.circle(-size // 2, 200)

    turtle.forward(size) # Termina o desenho
    turtle.end_fill() # Conclui o preenchimento
    turtle.setheading(0) # Reseta a direção do cursor para 0°

def draw_hearts(): # Função para definir plano de fundo
    turtle.bgcolor('lightpink') # Cor do fundo
    turtle.speed(3) # Velocidade média
    turtle.width(3) # Espessura do traço

    # Tamanhos e cores dos corações 
    sizes = [250, 200, 150, 100, 50]
    colors = ['#E57582', '#E793A2', '#DCB7BB', '#E47381', '#E793A2']

    for size, color in zip(sizes, colors): # Combina os elementos das duas listas.  Ex.: 250 e '#E57582'
        turtle.penup() # 'Levanta' o cursor, impedindo que ele desenhe linhas indesejadas ao se mover
        turtle.goto(0, -size // 2) # Centralizar e ajustar a altura
        turtle.pendown() # O cursor volta a desenhar
        draw_heart(turtle, size, color) # Chamada da função que desenha o coração

    turtle.hideturtle() # Esconde o cursor
    turtle.done() # Finaliza o desenho      

draw_hearts()
    