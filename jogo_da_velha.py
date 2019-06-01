def show_board(estado):    
    saved_output =("1|2|3\n"
                   "-----\n"
                   "4|5|6\n"
                   "-----\n"
                   "7|8|9")
                            
    for index in range(0,9):
        posicao = str(index + 1)
        if estado[index] == 1:
             saved_output = saved_output.replace(posicao,'X')
        elif estado[index] == 2:
            saved_output = saved_output.replace(posicao,'O')

    print(saved_output)

def is_p1_turn(estado):
    number_of_1 = 0
    number_of_2 = 0
    for i in range(0,9):
        if estado[i] == 1:
            number_of_1 += 1
        if estado[i] == 2:
            number_of_2 += 2
    if number_of_1 == number_of_2:
        return True 
    else: 
        return False

# def is_p1_turn_v2(estado):
#     number_of_1 = 0
#     number_of_2 = 0
#     for pos in estado:
#         if pos == 1:
#             number_of_1 += 1
#         if pos == 2:
#             number_of_2 += 2

#     return number_of_1 == number_of_2


def play():
    game_state = [0] * 9

    def update(pos):
        # ve se dap ra converter para inteiro
        index = 0
        try:
            index = int(pos)
        except:
            return
        # converte indice baseado em 1 para baseado em 0
        index -= 1
        # checa se esta em um itervalo valido
        if index < 0 or index > 8:
            return
    
        if game_state[index] != 0:
            return
        game_state[index] = 1 if is_p1_turn(game_state) else 2
        
    p1_name = 'p1'
    p2_name = 'p2'

    print('Bem vindo!')
    
    # print('Qual o seu nome jogador 1?\n')
    # p1_name = input()
    # print('Qual o seu nome jogador 2?\n')
    # p2_name = input()
    

    # print('O jogo acabou.')
    def is_game_over(game_state):
        for pos in game_state:
            if pos == 0:
                return False
        return True

    while not is_game_over(game_state):
        print((p1_name if is_p1_turn(game_state) else p2_name) + ', é a sua vez de jogar!')
        print(game_state)
        show_board(game_state)
        update(input('Selecione a posição: '))

play()
