import time
import random
import os
import platform

# Lista de frases engraçadas
frases = [
    "🚰 Beba água, seu rim tá contando com você!",
    "💧 Sua planta interna está pedindo socorro!",
    "🥤 Hidratação é vida, hein!",
    "⚠️ Você bebeu café... Agora é a vez da água!",
    "👀 Ainda não bebeu água hoje? Tô te vigiando!"
]

# Função para notificar o usuário
def notificar(frase):
    sistema = platform.system()

    if sistema == "Windows":
        os.system(f"msg * {frase}")
    elif sistema == "Darwin":  # macOS
        os.system(f"osascript -e 'display notification \"{frase}\" with title \"Hora da água!\"'")
    elif sistema == "Linux":
        os.system(f'notify-send "Hora da água!" "{frase}"')
    else:
        print(frase)

# Configuração do tempo (em minutos)
intervalo_minutos = 30

print("🚨 Iniciando o alarme de hidratação! (CTRL+C para sair)")
try:
    while True:
        time.sleep(intervalo_minutos * 60)
        frase = random.choice(frases)
        notificar(frase)
except KeyboardInterrupt:
    print("\n⛔ Alarme encerrado. Beba água mesmo assim, viu?")
