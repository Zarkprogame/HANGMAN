def divisors(numero):
    divisors = []
    for i in range(1, numero +1):
        if numero % i == 0:
            divisors.append(i)
    return divisors

def run():
    numero= input("Ingrese un Numero: ")
    assert numero.isnumeric(), "Debes colocar un NUMERO positivo"
    print(divisors(int(numero)))

if __name__ == "__main__":
    run()