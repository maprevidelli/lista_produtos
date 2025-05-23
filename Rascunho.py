from datetime import datetime

# Data e hora atuais
agora = datetime.now()

# Formato padrão
print("Data e hora atuais:", agora)

# Formatando a saída
print("Data e hora formatadas:", agora.strftime("%d/%m/%Y %H:%M:%S"))
print("Data:", agora.strftime("%d/%m/%Y"))
print("Hora:", agora.strftime("%H:%M:%S"))