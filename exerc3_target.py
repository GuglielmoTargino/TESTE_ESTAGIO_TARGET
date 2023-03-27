
#Exercício para se calcular o maior faturamento de uma distribuidora. 

bandeira='s'
menor=maior=0
ctor=soma=media=ctor2=0

while bandeira!='N':

    nr=float(input('Informe o valor do faturamento'))
    bandeira=str(input('Deseja continuar?_ [S/N]_')).upper().strip()[0]
    if ctor==0:
        menor=nr
    if nr>maior:
        maior=nr
    if nr<menor:
        menor=nr
    ctor+=1
    soma+=nr
    media=soma/ctor
    if nr>media:# linha para se testar quantos dias o faturamento ultrapassou a média;
        ctor2+=1

print('O menor valor de faturamento foi R$={:.2f}. O maior valor de faturamento foi R$={:.2f}'.format(menor,maior))
print(f"media{media}")
print(f"O faturamento diário ultrapassou a média {ctor2} vezes este mês")



