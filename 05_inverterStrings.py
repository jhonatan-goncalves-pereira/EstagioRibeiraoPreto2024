def inverte_string(string):
    tamanho = len(string)
    string_invertida = ''
    for i in range(tamanho - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

# String para inverter
texto = input("Digite uma string para inverter: ")
print("String invertida:", inverte_string(texto))
