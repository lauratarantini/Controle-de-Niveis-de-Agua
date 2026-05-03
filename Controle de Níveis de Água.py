from colorama import init, Fore, Style

# Inicia o colorama
init()

# Lista com as mensagens de cada nível
niveis = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]

# Função que retorna a cor conforme o nível
def pegar_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE

# Exibe todos os níveis com suas cores
for i in range(len(niveis)):
    cor = pegar_cor(i + 1)
    print(cor + niveis[i])

# Restaura o estilo padrão do terminal
print(Style.RESET_ALL)