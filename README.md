# Jogo Matemático
Jogo utilizando Python para treinar o conhecimento em operações matemáticas. É jogado via linha de comando.
Para jogá-lo é necessário informar a dificuldade do jogo como parâmetro ao iniciá-lo. Ao indicar a dificuldade serão gerados valor(es) aleatórios. Ao rodar o código, será informado a conta que você deve calcular, você deve respondê-la para ganhar 1 ponto. Ao responder, você saberá se respondeu certo ou não e o jogo perguntará se você vai querer continuar a jogar ou não. O jogo acrescenta pontos por acerto de conta, iniciando com 0.

## Versão 1
O jogo possui 3 operações disponíveis: soma, subtração e multiplicação. É acrescentado 1 ponto por acerto e não há limite de jogadas.
As dificuldades são as seguintes:
### 1
- Os valores a serem calculados são escolhidos aleatoriamente entre 0 e 10.
### 2
- Os valores a serem calculados são escolhidos aleatoriamente entre 0 e 100.
### 3
- Os valores a serem calculados são escolhidos aleatoriamente entre 0 e 1000.
### 4
- Os valores a serem calculados são escolhidos aleatoriamente entre 0 e 10000.
### Outros valores
- Caso a dificuldade não estiver no intervalo entre 1 e 4, os valores que devem ser calculados serão escolhidos aleatoriamente entre 0 e 50.

## Versão 2
O jogo possui uma nova operação, a divisão. Com isso, deve ser alterado o intervalo de escolha dos números, pois não pode ocorrer divisão por 0.
As dificuldades são as seguintes:
### 1
- Os valores a serem calculados são escolhidos aleatoriamente entre 1 e 10.
### 2
- Os valores a serem calculados são escolhidos aleatoriamente entre 1 e 100.
### 3
- Os valores a serem calculados são escolhidos aleatoriamente entre 1 e 1000.
### 4
- Os valores a serem calculados são escolhidos aleatoriamente entre 1 e 10000.
### Outros valores
- Caso a dificuldade não estiver no intervalo entre 1 e 4, os valores que devem ser calculados serão escolhidos aleatoriamente entre 0 e 50.

## Versão 3
O jogo foi modificado para guardar as 5 maiores pontuações obtidas na máquina e salvar o nome de cada usuário que registrou essa pontuação.
Também foi modificado a lógica do jogo quando a operação é de divisão, sendo necessário informar apenas as 2 primeiras casas decimais aproximadas do número obtido.
Também ocorreu a adição da pasta jogo-matematico, a qual possui um arquivo executável que pode ser utilizado em ambientes que não possuem python, assim, tornando fácil a divulgação e a diversão do jogo.
As dificuldades são as seguintes:
### 1
- Os valores a serem calculados são escolhidos aleatoriamente entre 1 e 10.
### 2
- Os valores a serem calculados são escolhidos aleatoriamente entre 1 e 100.
### 3
- Os valores a serem calculados são escolhidos aleatoriamente entre 1 e 1000.
### 4
- Os valores a serem calculados são escolhidos aleatoriamente entre 1 e 10000.
### Outros valores
- Caso a dificuldade não estiver no intervalo entre 1 e 4, os valores que devem ser calculados serão escolhidos aleatoriamente entre 0 e 50.

## Versão 4
Há uma alteração na saída da lista de pontuações e agora também é informado a data no formato dd/mm/aaaa e o horário que o jogador terminou de jogar no formato HH:MM. 
Para a operação de divisão, haverá uma mudança. O jogador pode ter a divisão inteira ou a não inteira, para a não inteira, a lógica segue a mesma que a da versão anterior, porém, para a divisão inteira, o intervalo de valores da dificuldade será apenas obedecido para o divisor, podendo o dividendo ser até 100 vezes maior que o dividor.
As dificuldades são as seguintes:
### 1
- Os valores a serem calculados são escolhidos aleatoriamente entre 1 e 10.
### 2
- Os valores a serem calculados são escolhidos aleatoriamente entre 1 e 100.
### 3
- Os valores a serem calculados são escolhidos aleatoriamente entre 1 e 1000.
### 4
- Os valores a serem calculados são escolhidos aleatoriamente entre 1 e 10000.
### Outros valores
- Caso a dificuldade não estiver no intervalo entre 1 e 4, os valores que devem ser calculados serão escolhidos aleatoriamente entre 0 e 50.
Vale ressaltar que na operação de divisão inteira o valor do divisor respeita esse intervalo, enquanto o valor do dividendo pode ser até 100 vezes maior.