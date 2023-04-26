"""
Autor: Angel Fernandez Ariza.
Fecha: 17/10/2022.

13. Escribir un programa que calcule el desglose mínimo en billetes y monedas de una cantidad exacta de euros.
Hay billetes de 500, 200, 100, 50, 20, 10 y 5 € y monedas de 2 y 1 €.

Por ejemplo, si deseamos conocer el desglose de 434 €, el programa mostrará por pantalla el siguiente resultado:

2 billetes de 200 euros.
1 billete de 20 euros.
1 billete de 10 euros.
2 monedas de 2 euros.
"""
money = int(input("Dime una cantidad de dinero en euros: "))

if money >= 0:
    if money == 0:
        print("tienes 0 €")
    if money >= 500:
        print(f"Tienes {money // 500} billetes de 500€")
        money = money - (money // 500 * 500)
    if money >= 200:
        print(f"Tienes {money // 200} billetes de 200€")
        money = money - (money // 200 * 200)
    if money >= 100:
        print(f"Tienes {money // 100} billetes de 100€")
        money = money - (money // 100 * 100)
    if money >= 50:
        print(f"Tienes {money // 50} billetes de 50€")
        money = money - (money // 50 * 50)
    if money >= 20:
        print(f"Tienes {money // 20} billetes de 20€")
        money = money - (money // 20 * 20)
    if money >= 10:
        print(f"Tienes {money // 10} billetes de 10€")
        money = money - (money // 10 * 10)
    if money >= 5:
        print(f"Tienes {money // 5} billetes de 5€")
        money = money - (money // 5 * 5)
    if money >= 2:
        print(f"Tienes {money // 2} monedas de 2€")
        money = money - (money // 2 * 2)
    if money >= 1:
        print(f"Tienes {money // 1} monedas de 1€")
else:
    print("Has introducid una cantidad negativa")
