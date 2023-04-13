texto = input('Digite uma palavra: ')
textoInverso = ''
tamanhoTexto = len(texto)

#criei esse código para fazer o reverso, mas também pode ser apenas utilizado o [::-1] na frente
# da variável    
for x in range(tamanhoTexto):
    letra = texto[-(x+1)]
    textoInverso = textoInverso+letra

print(textoInverso)
