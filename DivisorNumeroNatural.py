def NumeroNatural():
    while True:
        try:
            numero = int(input("Ingrese un número natural: "))
            if numero <= 0:
                raise ValueError("El número debe ser un natural y positivo.")
            return numero
        except ValueError as e:
            print(f"Entrada inválida: {e}. Intente nuevamente.")

def CalcularDivisores(numero):
    divisores = [i for i in range(1, numero + 1) if numero % i == 0]
    return divisores

def main():
    numero_natural = NumeroNatural()
    divisores = CalcularDivisores(numero_natural)
    print(f"Los divisores de {numero_natural} son: {divisores}")

if __name__ == "__main__":
    main()
