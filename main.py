import random
import csv

# Función para generar un número aleatorio entre 1 y 100
def generate_number():
    return random.randint(1, 100)

# Función para pedir al usuario que adivine el número
def ask_user():
    return int(input("Adivina el número (entre 1 y 100): "))

# Función para actualizar el archivo CSV con el resultado actual
def update_csv(attempts, result):
    with open('results.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([attempts, result])

# Función para imprimir los resultados anteriores
def print_results():
    with open('results.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Función principal del programa
def main():
    while True:
        number = generate_number()
        attempts = 0

        while True:
            guess = ask_user()
            attempts += 1

            if guess == number:
                print(f"¡Correcto! Adivinaste el número en {attempts} intentos.")
                update_csv(attempts, 'ganado')
                break
            elif guess < number:
                print("El número es mayor.")
            else:
                print("El número es menor.")

        play_again = input("¿Quieres jugar otra vez? (s/n): ")
        if play_again.lower() != "s":
            break

    print_results()

if __name__ == '__main__':
    main()
