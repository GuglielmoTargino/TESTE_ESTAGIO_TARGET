#programa para se calciular o valor de representação de uma distribuidora.
print(" O faturamento de uma distribuidora está detalhado nos estados abaixo:")
print("Estado SP=R$67.836,43.\nEstado RJ=R$36.679,66.\nEstado MG=R$29.229,88.\nEstado ES=R$27.165,48.\nOutros=19.849,53.")
sp=67836.43
rj=36679.66
mg=29229.89
es=27165.48
outros=19849.53

total=sp+rj+mg+es+outros

repsp=(sp/total)*100
reprj=(rj/total)*100
repmg=(mg/total)*100
repes=(es/total)*100
repoutros=(outros/total)*100
tot=repsp+reprj+repmg+repes+repoutros


print(f"representação sp é {repoutros:.2f}%")
print(f" total é {tot}")




