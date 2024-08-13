import random

def adivinanza_matematica():
    operaciones = ["+", "-", "*", "/"]
    operacion = random.choice(operaciones)
    numero1 = random.randint(1, 10)
    numero2 = random.randint(1, 10)
    
    if operacion == "/":
        numero1 = numero1 * numero2  # Aseguramos que la división sea exacta

    print("¡Bienvenido al juego de Adivinanza Matemática!")
    print(f"Resuelve el siguiente problema: {numero1} {operacion} {numero2}")
    
    if operacion == "+":
        respuesta_correcta = numero1 + numero2
    elif operacion == "-":
        respuesta_correcta = numero1 - numero2
    elif operacion == "*":
        respuesta_correcta = numero1 * numero2
    elif operacion == "/":
        respuesta_correcta = numero1 // numero2

    intentos_restantes = 3

    while intentos_restantes > 0:
        respuesta = int(input(f"Introduce tu respuesta (Te quedan {intentos_restantes} intentos): "))

        if respuesta == respuesta_correcta:
            print("¡Correcto! Has resuelto el problema.")
            break
        else:
            intentos_restantes -= 1
            if intentos_restantes > 0:
                print("Incorrecto. Intenta de nuevo.")
            else:
                print(f"Incorrecto. La respuesta correcta era {respuesta_correcta}. Has perdido.")

adivinanza_matematica()
