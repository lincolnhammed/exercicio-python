import pygame
import sys
import random

# Inicializa o pygame
pygame.init()

# Configurações da tela
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jogo da Velha")

# Cores
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
X_COLOR = (0, 0, 0)  # Cor preta para o X
O_COLOR = (0, 0, 0)  # Cor preta para o O
BG_COLOR = (255, 255, 255)  # Cor do fundo do tabuleiro (branca)

# Definindo a grade do jogo
GRID_SIZE = 3
cell_size = screen_width // GRID_SIZE

# Criando o tabuleiro
board = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Função para desenhar o tabuleiro
def draw_board():
    screen.fill(BG_COLOR)
    
    # Linhas horizontais
    pygame.draw.line(screen, LINE_COLOR, (0, cell_size), (screen_width, cell_size), 5)
    pygame.draw.line(screen, LINE_COLOR, (0, 2*cell_size), (screen_width, 2*cell_size), 5)
    
    # Linhas verticais
    pygame.draw.line(screen, LINE_COLOR, (cell_size, 0), (cell_size, screen_height), 5)
    pygame.draw.line(screen, LINE_COLOR, (2*cell_size, 0), (2*cell_size, screen_height), 5)

# Função para desenhar X e O no tabuleiro
def draw_marks():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == 'X':
                pygame.draw.line(screen, X_COLOR, (col * cell_size + 20, row * cell_size + 20), 
                                 (col * cell_size + cell_size - 20, row * cell_size + cell_size - 20), 15)
                pygame.draw.line(screen, X_COLOR, (col * cell_size + 20, row * cell_size + cell_size - 20), 
                                 (col * cell_size + cell_size - 20, row * cell_size + 20), 15)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, O_COLOR, (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2), 50, 15)

# Função para verificar vitória
def check_win():
    # Verificando linhas, colunas e diagonais
    for row in range(GRID_SIZE):
        if board[row][0] == board[row][1] == board[row][2] != '':
            return board[row][0]
    
    for col in range(GRID_SIZE):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    
    return None

# Função para verificar se há espaços vazios no tabuleiro
def available_moves():
    moves = []
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == '':
                moves.append((row, col))
    return moves

# Função para o algoritmo Minimax (IA)
def minimax(board, depth, maximizing_player):
    winner = check_win()
    if winner == 'X':
        return -10 + depth
    elif winner == 'O':
        return 10 - depth
    elif not available_moves():
        return 0
    
    if maximizing_player:
        max_eval = float('-inf')
        for move in available_moves():
            board[move[0]][move[1]] = 'O'
            eval = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = ''
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in available_moves():
            board[move[0]][move[1]] = 'X'
            eval = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = ''
            min_eval = min(min_eval, eval)
        return min_eval

# Função para a IA fazer sua jogada
def ai_move():
    best_move = None
    best_value = float('-inf')
    for move in available_moves():
        board[move[0]][move[1]] = 'O'
        move_value = minimax(board, 0, False)
        board[move[0]][move[1]] = ''
        if move_value > best_value:
            best_value = move_value
            best_move = move
    board[best_move[0]][best_move[1]] = 'O'

# Função para reiniciar o tabuleiro
def reset_board():
    global board
    board = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Função principal
def main():
    player = 'X'
    game_over = False
    
    while True:
        draw_board()
        draw_marks()
        
        if game_over:
            winner = check_win()
            font = pygame.font.Font(None, 50)
            if winner:
                text = font.render(f'Jogador {winner} ganhou!', True, (255, 0, 0))
            else:
                text = font.render('Empate!', True, (255, 0, 0))
            screen.blit(text, (screen_width // 3, screen_height // 3))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over and player == 'X':
                x, y = pygame.mouse.get_pos()
                row, col = y // cell_size, x // cell_size
                
                if board[row][col] == '':
                    board[row][col] = player
                    if check_win():
                        game_over = True
                    player = 'O'
        
        if player == 'O' and not game_over:
            ai_move()
            if check_win():
                game_over = True
            player = 'X'

        if game_over:
            pygame.time.wait(2000)  # Espera 2 segundos antes de reiniciar
            reset_board()
            game_over = False

        pygame.time.Clock().tick(30)

if __name__ == "__main__":
    main()
