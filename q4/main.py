from a_star import *
from bfs import *
from puzzle import *

print("Iniciando...")

x = start(16)
y = start(8)

print("Teste para o jogo dos 8:\n")

bfs(y, 8)
a_star_search(y, 8)

print("\n\nTeste para o jogo dos 15:\n")

a_star_search(x, 16)
#bfs(x, 16)
