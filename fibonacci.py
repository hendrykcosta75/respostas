def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        while fib[-1] < n:
            fib.append(fib[-1] + fib[-2])
        if n in fib:
            print(f"O número {n} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {n} não pertence à sequência de Fibonacci.")
        return fib[:-1]
    

"""Diz todos os números da sequência de Fibonacci até o número informado pelo usuário."""

def main():
    num = int(input("Informe um número: "))
    array_fib = fibonacci(num)
    print(f"A sequência de Fibonacci até {num} é: {array_fib}")

main()
