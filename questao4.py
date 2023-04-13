fatSp = 67836.43
fatRj = 36678.66
fatMg = 29229.88
fatEs = 27165.48
fatOutros = 19849.53

fatTotal = fatSp + fatRj + fatMg + fatEs + fatOutros

repSp = (fatSp * 100) / fatTotal
repRj = (fatRj * 100) / fatTotal
repMg = (fatMg * 100) / fatTotal
repEs = (fatEs * 100) / fatTotal
repOutros = (fatOutros * 100) / fatTotal

print(f'A representatividade de SP é de {round(repSp, 2)}%')
print(f'A representatividade de RJ é de {round(repRj, 2)}%')
print(f'A representatividade de MG é de {round(repMg, 2)}%')
print(f'A representatividade de ES é de {round(repEs, 2)}%')
print(f'A representatividade de OUTROS é de {round(repOutros, 2)}%')

