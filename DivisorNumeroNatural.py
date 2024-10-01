def obtener_numero_natural():
    while True:
        try:
            numero = int(input("Ingrese un número natural: "))
            if numero <= 0:
                raise ValueError("El número debe ser un natural positivo.")
            return numero
        except ValueError as e:
            print(f"Entrada inválida: {e}. Intente nuevamente.")

def calcular_divisores(numero):
    divisores = [i for i in range(1, numero + 1) if numero % i == 0]
    return divisores

def main():
    numero_natural = obtener_numero_natural()
    divisores = calcular_divisores(numero_natural)
    print(f"Los divisores de {numero_natural} son: {divisores}")

if __name__ == "__main__":
    main()
