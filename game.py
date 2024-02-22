import csv
import os

from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    print("Seja muito bem-vindo :)")
    print("Este é um jogo para testar suas habilidades matemáticas.")
    nome = input("Por favor informe seu nome: ")

    print(f'{"-"*40}\nA'
          f'tualmente existem 4 dificuldades nele:\n'
          f'1 - Básico\n'
          f'2 - Médio\n'
          f'3 - Difícil\n'
          f'4 - Impossível\n'
          f'{"-"*40}')
    print("Observação importante sobre o jogo: Caso cair a operação de divisão, usar o . ao invés da vírgula como separador de números\n"
          "decimais e inteiros. Vale também ressaltar que o jogo aceita apenas o valor aproximado das cadas decimais, por exemplo\n"
          "se for 1.5191 o resultado será 1.52, se for 0.49998 o resultado sera 0.5 e se for 0.111111 o resultado será 0.11")
    while True:
        dificuldade: int = int(input('Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: '))
        print(f"{dificuldade}, {type(dificuldade)}")

        calc: Calcular = Calcular(dificuldade)

        print('Informe o resultado para a seguinte operação: ')
        calc.mostrar_operacao()

        resultado: float = float(input())

        if calc.checar_resultado(resultado):
            pontos += 1*dificuldade
            print(f'Você tem {pontos} ponto(s).')

        continuar: int = int(input('Deseja continuar no jogo? [1 - sim, 0 - não] : '))
        if not continuar:
            break

    print(f'Você finalizou com {pontos} ponto(s).')
    print('Até o próximo jogo :)')

    pontuacoes = load_points()
    pontuacoes.append((pontos, nome))
    pontuacoes.sort(key=lambda x: x[0], reverse=True)  # Ordenando decrescentemente as pontuações
    pontuacoes = pontuacoes[:5]  # Salvando as 5 maiores pontuações
    save_points(pontuacoes)  # Salvando no arquivo de pontuações
    print("\n --- As 5 maiores pontuações nesta máquina são ---")
    for i, (pontuacao, nome) in enumerate(pontuacoes,1):
        print(f"{i} - Nome: {nome}, Pontuação: {pontuacao}")


def load_points() -> list:
    pontuacoes = []
    if os.path.exists('pontuacoes.csv'):
        with open('pontuacoes.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for linha in reader:
                pontuacoes.append((int(linha[0]), linha[1]))
    return pontuacoes


def save_points(pontuacoes: list) -> None:
    with open('pontuacoes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for pontuacao in pontuacoes:
            writer.writerow(pontuacao)


if __name__ == '__main__':
    main()
