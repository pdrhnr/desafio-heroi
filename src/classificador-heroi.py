#Variável para o nome do herói
nome_heroi = ""

#Variável para a experiência do herói
exp_heroi = 0

#Variável para o nível do herói
level_heroi = ""

#Funções para guardar nome e experiência do herói
nome_heroi = input("Insira o nome do seu herói: ")

while True:
    entrada_usuario = (input("Digite a quantidade da experiência do herói(Lembrando que precisa ser um número inteiro positivo): "))

    if entrada_usuario.isdigit() and int(entrada_usuario) > 0:
        exp_heroi = int(entrada_usuario)
        break
    else:
        print("O número precisa ser um inteiro positivo!")

#Classificação do herói
    
if exp_heroi < 1000:
    level_heroi = "Ferro"
elif exp_heroi >= 1001 and exp_heroi <= 2000:
    level_heroi = "Bronze"
elif exp_heroi >= 2001 and exp_heroi <= 5000:
    level_heroi = "Prata"
elif exp_heroi >= 5001 and exp_heroi <= 7000:
    level_heroi = "Ouro"
elif exp_heroi >= 7001 and exp_heroi <= 8000:
    level_heroi = "Platina"
elif exp_heroi >= 8001 and exp_heroi <= 9000:
    level_heroi = "Ascendente"
elif exp_heroi >= 9001 and exp_heroi <= 10000:
    level_heroi = "Imortal"
else:
    level_heroi = "Radiante"

print(f"O herói de nome {nome_heroi} está no nível de {level_heroi}")