soma=0
faturamentos = {'sp': 67836.43,'rj': 36678.66,'mg':29229.88,'es':27165.48,'outros': 19849.53}
for estado in faturamentos:
    soma += faturamentos[estado]
for estado in faturamentos:
    print(f'Faturamento de {estado}: {(faturamentos[estado]/soma)*100:.2f}%')


