#01

'''Ao final do processamento, o valor da variável SOMA será 91.

Isso ocorre porque o laço "enquanto" adiciona o valor de K à SOMA a cada iteração, começando com K=1 e
incrementando K a cada iteração até que K seja igual a INDICE (13, neste caso). Portanto, a soma será 1+2+3+...+13, que é igual a 91.'''








#02
'''2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.'''


n =  int(input('Informe um número: '))
def Fibonacci(n):
    seque_fib = [0]*n
    a = 0
    b = 1
    seque_fib[0]=0
    for i in range (1,n-1):
        prox = a + b
        a = b
        seque_fib[i] = a
        b = prox
        seque_fib[i+1] = b
        if n == prox:
            print('O número está presente na sequência')
        else:
            pass
    return seque_fib
print(Fibonacci(n))


#Também poderia ser assim:
num = int(input('Informe um número:'))

fibonacci = [0, 1]
while fibonacci[-1] < num:
    proximo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo)

if num in fibonacci:
    print(f"{num} está na sequência de Fibonacci!")
else:
    print(f"{num} não está na sequência de Fibonacci.")

print("A sequência de Fibonacci até", num, "é:",fibonacci)











#3
'''3) Descubra a lógica e complete o próximo elemento:



a) 1, 3, 5, 7, _9__

b) 2, 4, 8, 16, 32, 64, __128__

c) 0, 1, 4, 9, 16, 25, 36, __49__

d) 4, 16, 36, 64, __100__

e) 1, 1, 2, 3, 5, 8, __13__

f) 2,10, 12, 16, 17, 18, 19, __200__
'''


'''
a) O próximo elemento é 9, pois a lógica é somar 2 a cada número.

b) O próximo elemento é 128, pois a lógica é multiplicar o número anterior pelo número por 2.

c) O próximo elemento é 49, Cada número é igual ao anterior acrescido de um número ímpar que segue a sequência (+1, +3, +5, +7, +9, +11, +13). 
Assim, devemos acrescentar 13, obtendo 36 + 13 = 49.

d) Cada número é igual ao quadrado dos números pares. Com isso, temos que 64 = 8^2. Então, o próximo número par é 10, e o seu quadrado é 10^2 = 100.

e) O próximo elemento é 13, pois a lógica é somar os dois números anteriores para obter o 
próximo número na sequência (exemplo: 1+1=2, 1+2=3, 2+3=5, 3+5=8, etc).

f) O próximo elemento é 200, pois a lógica é a sequencia de números que se iniciam com a letra D.
'''











#4
'''4 - Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. O carro de Ribeirão Preto em direção a Franca, 
a uma velocidade constante de 110 km/h e o caminhão de Franca em direção a Ribeirão Preto a uma velocidade constante de 80 km/h. 
Quando eles se cruzarem na rodovia, qual estará mais próximo a cidade de Ribeirão Preto?



IMPORTANTE:

a) Considerar a distância de 100km entre a cidade de Ribeirão Preto <-> Franca.

b) Considerar 2 pedágios como obstáculo e que o caminhão leva 5 minutos a mais para passar em cada um deles e o carro possui tag de pedágio (Sem Parar)

c) Explique como chegou no resultado.
'''

'''
O carro e o caminhão estão se aproximando um do outro em velocidades opostas, então sua velocidade relativa é a soma de suas velocidades. Portanto, a velocidade relativa é:

110 km/h + 80 km/h = 190 km/h

A distância entre as duas cidades é de 100 km, e quando os dois veículos se encontram na estrada, eles terão percorrido juntos uma distância igual a 100 km.

Para encontrar o tempo que eles levam para se encontrarem, podemos usar a fórmula:

tempo = distância / velocidade

Substituindo os valores, obtemos:

tempo = 100 km / 190 km/h ≈ 0,5263 h ≈ 31,58 minutos

Portanto, os dois veículos se encontrarão na rodovia após cerca de 31,58 minutos.

O carro está viajando em direção a Franca, então ele está mais próximo de Franca quando eles se encontram. Ele terá percorrido uma distância igual a:

distância percorrida pelo carro = 110 km/h x 0,5263 h ≈ 57,89 km

Portanto, quando os dois veículos se encontrarem na estrada, o carro estará a uma distância de aproximadamente 42,11 km da cidade de Ribeirão Preto.

O caminhão, por outro lado, está viajando em direção a Ribeirão Preto e estará mais próximo dessa cidade quando eles se encontrarem. No entanto, 
o caminhão levará mais tempo para percorrer a mesma distância, devido aos pedágios. 
Supondo que cada pedágio leve 5 minutos para passar, o caminhão levará 10 minutos adicionais (ou 0,1667 horas) para chegar ao ponto de encontro.

Assim, a distância percorrida pelo caminhão até o ponto de encontro será:

distância percorrida pelo caminhão = 80 km/h x (0,5263 h + 0,1667 h) ≈ 60 km

Portanto, quando os dois veículos se encontrarem na estrada, o caminhão estará a uma distância de aproximadamente 40 km da cidade de Ribeirão Preto.

Concluindo, quando os dois veículos se encontrarem na rodovia, o caminhão estará mais próximo da cidade de Ribeirão Preto, a cerca de 40 km, 
enquanto o carro estará mais próximo de Franca, a cerca de 57,89 km.'''












5#
'''5) Escreva um programa que inverta os caracteres de um string.



IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

'''

palavra = "Estágio dos sonhos"
palavra_invertida = ""

for letra in palavra:
    palavra_invertida = letra + palavra_invertida

print(palavra_invertida)