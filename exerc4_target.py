#programa para se calciular o valor de representação de uma distribuidora.
print(" O faturamento de uma distribuidora está detalhado nos estados abaixo:")
print(">> Estado SP=R$67.836,43.\n>> Estado RJ=R$36.679,66.\n>> Estado MG=R$29.229,88.\n> Estado ES=R$27.165,48.\n>> Outros=19.849,53.")
sp=67836.43 # valor arrecadado em SP
rj=36679.66 # valor arrecadado em RJ
mg=29229.89 # valor arrecadado em MG
es=27165.48 # valor arrecadado em ES
outros=19849.53 # valor arrecadado em OUTROS

total=sp+rj+mg+es+outros

repsp=(sp/total)*100 # oercentual de representatividade induvudual.
reprj=(rj/total)*100
repmg=(mg/total)*100
repes=(es/total)*100
repoutros=(outros/total)*100


print("")
print(f" > O percentual de representação de São Paulo é {repoutros:.2f}%")
print(f" > O percentual de representação do Rio de Janeiro é {reprj:.2f}%")
print(f" > O percentual de representação de Minas Gerais é {repmg:.2f}%")
print(f" > O percentual de representação do Espírito Santo é {repes:.2f}%")
print(f" > O percentual de representação de Outros é {repoutros:.2f}%")




