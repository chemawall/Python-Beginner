def fizz_buzz():
    for i in range(1,101):
        if i%5 == 0 and i%3 == 0:
            print("FizzBuzz")
        elif i%5 == 0: 
            print("Buzz")
        elif i%3 == 0:
            print("Fizz")
        else:
            print(i)


fizz_buzz()

#errores: el orden importa, primero los mas restrictivos
#vigilar el rango, el cero tb se cuenta si no empieza desde el 1