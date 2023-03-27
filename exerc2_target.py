#programa para verificar se um numero informado pelo usuário 
#pertence a sequencia de Fibonacci.




ref=int(input("Informe um número inteiro para saber se ele pertence à sequencia de Fibonacci_"))
 #variável <ref> criada para receber o número digitado pelo usário e limitar a sequência Fibonacci.

nr1=0 # <nr0> é o primeiro numero da sequência
nr2=1 # <nr1> é o segundo número da sequência.
nr3=0 # variável criada para receber o último número da sequência. Começa zerada.
sinal=0 # variavel para sinalizar se o número digitado faz parte da sequencia. 1 sim, 0 não. começa zerado.



while nr3<=ref:   
    nr3=nr1+nr2
    if nr3==ref:  # testa se o número faz parte da sequência.     
       sinal=1
       nr3+=1
       
    elif ref==0:
         sinal=1
         nr3+=1

    elif ref==1:
        sinal=1
        nr3+=1

    elif ref==2:
        sinal=1
        nr3+=1

    else:         
        nr1=nr2
        nr2=nr3
        nr3+=1 

if sinal==1:   
   print(f"Número {ref} digitado não pertence a sequência Fibonacci")  
else:
   print(f" Número {ref} não pertence a sequência Fibonacci")


 
    
   




    
    

    







