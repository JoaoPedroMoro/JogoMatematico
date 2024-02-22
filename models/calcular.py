from random import randint


class Calcular:

    def __init__(self: object, dificuldade: int, /) -> None:
        self.__dificuldade: int = dificuldade
        self.__operacao: int = randint(1, 4)  # 1-soma/2-subtração/3-multiplicação/4-divisão
        if self.__operacao == 4:
            val1, val2 = self._gerar_valor_divisao
            self.__valor1 = val1
            self.__valor2 = val2
            res = round(val1 / val2, 2)
            self.__resultado = res
        else:
            self.__valor1: float = self._gerar_valor
            self.__valor2: float = self._gerar_valor
            self.__resultado: float = self._gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def resultado(self: object) -> int:
        return self.__resultado

    def __str__(self: object) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Diminuir'
        elif self.operacao == 3:
            op = 'Multiplicar'
        elif self.operacao == 4:
            op = 'Dividir'
        else:
            op = 'Operação desconhecida'
        return f'Valor 1: {self.valor1}\nValor 2: {self.valor2}\nDificuldade: {self.dificuldade}\nOperação: {op}'

    @property
    def _gerar_valor(self: object) -> int:
        if self.dificuldade == 1:
            return randint(1, 10)
        if self.dificuldade == 2:
            return randint(1, 100)
        if self.dificuldade == 3:
            return randint(1, 1000)
        elif self.dificuldade == 4:
            return randint(1, 10000)
        else:
            return randint(1, 50)

    @property
    def _gerar_valor_divisao(self: object) -> tuple[int, int]:
        if self.dificuldade == 1:
            print(f"Dificuldade 1")
            val1 = randint(1, 10)
            val2 = randint(1, 10)
            return val1, val2
        if self.dificuldade == 2:
            print(f"Dificuldade 2")
            val1 = randint(1, 100)
            val2 = randint(1, 100)
            return val1, val2
        if self.dificuldade == 3:
            print(f"Dificuldade 3")
            val1 = randint(1, 1000)
            val2 = randint(1, 1000)
            return val1, val2
        if self.dificuldade == 4:
            print(f"Dificuldade 4")
            val1 = randint(1, 10000)
            val2 = randint(1, 10000)
            return val1, val2
        else:
            print(f"Dificuldade 0")
            val1 = randint(1, 50)
            val2 = randint(1, 50)
            return val1, val2

    @property
    def _gerar_resultado(self: object) -> int:
        if self.operacao == 1:  # Somar
            return self.valor1 + self.valor2
        elif self.operacao == 2:  # Diminuir
            return self.valor1 - self.valor2
        elif self.operacao == 3:  # Multiplicar
            return self.valor1 * self.valor2
        else:  #elif self.operacao == 4:  # Divisão
            return self.valor1 / self.valor2

    @property
    def _op_simbolo(self: object) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        elif self.operacao == 3:
            return '*'
        else:  # elif self.operacao == 4:
            return '/'

    def checar_resultado(self: object, resposta: float) -> bool:
        certo: bool = False

        if self.resultado == resposta:
            print('Resposta correta!')
            certo = True
        else:
            print('Resposta errada!')
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        return certo

    def mostrar_operacao(self: object) -> None:
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ?')
