# programa para se inverter os caracteres de uma string;

palavra=str(input("Digite uma palavra_"))
dado=palavra.split() # separa os elementos da string e colo em dado
junto=''.join(dado) # junta os elementos sem espaços e coloca em junto
trocado=""# variável para receber os elemntos um por vez, do último para primeiro.

for letra in range(len(junto) -1,-1,-1): # coloca os caracteres da frente para trás.
    trocado+=junto[letra]



print(f"{trocado}")




