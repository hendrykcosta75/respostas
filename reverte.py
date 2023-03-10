def inverte(s):
    qtd = len(s)
    string = ""
    if qtd == 0:
        return s
    else:
        while qtd > 0:
            qtd -= 1
            string += s[qtd]
        return string

def main():
    string = input("Digite uma string: ")
    print(inverte(string))

main()