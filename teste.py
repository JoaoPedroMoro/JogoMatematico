from models.calcular import Calcular
from random import randint

# calc: Calcular = Calcular(1)
#
# print(calc)

while True:
    val1 = randint(1, 10)
    val2 = randint(1, 10)

    res = val1 / val2
    valor_decimal = round(res - int(res), 2)
    print(f"{val1}/{val2}={res}/{valor_decimal}")