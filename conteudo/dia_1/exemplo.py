# def showOficina(lista):
#     for item in lista:
#         print(item)  


# oficina = ['codespace', 'python', 'git', 'Django', 'SQL']
# showOficina(oficina)

def verifica_palindromo(palavra):
    lowCase = palavra.lower()
    print(lowCase[::-1])
    return lowCase == lowCase[::-1] 
 

print(verifica_palindromo("HAHAH"))
print(verifica_palindromo("Python"))