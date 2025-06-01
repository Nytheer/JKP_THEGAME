## Falta colocar algumas coisas hehe
Como funciona o cod do jogo "JKP" no PYTHON??

PARTE 1) importar bibliotecas:
import random
import time
random(sistema de escolha) 
time(para ter uma interação divertida com o jogador)


2) primeira função:
serve para armazenar ASCII desenhos com caracteres
e definir se vão ser utilizados ou não.

se forem:
def mao_opcao(opcao):
if opcao == 'PEDRA': (se opcão igual PEDRA)
	return '''
PEDRA!!
("MÃO ASCII PEDRA") {retorne}
'''

if opcao == 'PAPEL': (se opcão igual PAPEL)
	return ''' 
PAPEL!!
("MÃO ASCII PAPEL") {retorne}
'''

if opcao == 'TESOURA': (se opcão igual TESOURA)
	return '''
TESOURA!!
("MÃO ASCII TESOURA") {retorne}
'''

se não:
    elif opcao != 'PEDRA' != 'PAPEL' != 'TESOURA':
        return "opção invalida (ᵕ•᷄_•᷅ )" 

!= serve para comparação, 
só será 'true' se os itens forem diferentes.


PARTE 2) def jogo_JKP(): {onde o jogo cria vida}

1) input 
escolha_jogador = input('✧₊⁺Que tal um Jokenpô??⁺₊✧ 
⋆.˚✮escolha PEDRA, PAPEL ou TESOURA!!✮˚.⋆\n').upper()

\n serve para quebra de linha
.upper() serve para manter o texto/spring maiusculo

2) time
time.sleep(0.5)
serve para pausar a execução um codigo 
a partir de um tempo determinado
entre os --> () parenteses 

3) lista boba
opcao = ['PEDRA', 'PAPEL', 'TESOURA']
serve para armazenar mais de um item 
q nesse caso são springs/texts

4) condicional
if escolha_jogador != 'PEDRA' != 'PAPEL' != 'TESOURA':
   print('essa opção não existe pilantra! 
   (╭ರ_•́) tentando quebrar o código né??') 
