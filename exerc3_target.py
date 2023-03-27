
#Exercício para se calcular o maior faturamento de uma distribuidora. 

bandeira='s' # variável para sinalizar se o usuario deseja continuar com o cadastro
menor=maior=0 # variáveis para guardar o maior e o menor valor registrado
ctor=soma=media=ctor2=0 # variáveis para contar os dias e calcular a média

while bandeira!='N':

    nr=float(input('Informe o valor do faturamento'))
    bandeira=str(input('Deseja continuar?_ [S/N]_')).upper().strip()[0]
    if ctor==0: # mantem o menor valor no inicio.
        menor=nr
    if nr>maior: # guarda o maior valor
        maior=nr
    if nr<menor:# guarda o menor valor 
        menor=nr
    ctor+=1 #registra quntas vezes foram teve faturamento
    soma+=nr
    media=soma/ctor
    if nr>media:# linha para se testar quantos dias o faturamento ultrapassou a média;
        ctor2+=1

print('O menor valor de faturamento foi R$={:.2f}. O maior valor de faturamento foi R$={:.2f}'.format(menor,maior))

print(f"O faturamento diário ultrapassou a média {ctor2} vezes este mês")



