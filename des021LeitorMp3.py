print('='*6, 'Leitor Mp3', '='*6)
print('')
import pygame # Biblioteca para ler Mp3
pygame.mixer.init()
pygame.init() # Inicia a biblioteca
pygame.mixer.music.load("des021.mp3") # Carrega o arquivo no formato
pygame.mixer.music.play() # Para iniciar o arquivo
pygame.event.wait() # Finaliza o arquivo






