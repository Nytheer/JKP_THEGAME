# 💻😴 JKP - JoKenPô em Python

Um jogo simples de **Pedra, Papel e Tesoura** desenvolvido em Python para execução no terminal.
O projeto foi criado com o objetivo de praticar conceitos fundamentais de programação, 
como estruturas condicionais, funções, loops, entrada de dados e geração de escolhas aleatórias.

---

## 📌🤔 Funcionalidades

* Escolha entre Pedra, Papel ou Tesoura
* Escolha automática do computador
* Sistema de vitória, derrota e empate
* Exibição das mãos utilizando ASCII Art
* Efeito de suspense/pausa dramática com "JO... KEN... PÔ"
* Opção de jogar novamente
* Tratamento básico de entradas inválidas

## 🎮 Fluxo 🎮

### 1. Início ✈️

Ao executar o programa, o jogador recebe a mensagem:

```text
₊‧.°.⋆✮⋆.°.‧₊ ⛧°。 ⋆༺✮༻⋆。 °⛧ ₊‧.°.⋆✮⋆.°.‧₊
✧₊⁺Que tal um JoKenPô??⁺₊✧
⋆.˚✮ PEDRA, PAPEL ou TESOURA!! ✮˚.⋆
```

O sistema aguarda a escolha do usuário.

---

### 2. Entrada do Jogador 🤓

O jogador escolhe:

* Pedra
  
ou

* Papel

ou

* Tesoura

É utilizado um método que padroniza o texto:

```python
.strip().upper()
```
Isso permite que o jogador escreva: 

```text
PEDRA
pedra
PeDrA
```
E todas serão interpretadas da mesma forma. Ou seja, o método ajusta a entrada do usuário para evitar problemas com letras minúsculas ou espaços extras.

---

### 3. Suspense 😱

Após a escolha do jogador, o jogo exibe:

```text
JO
KEN
PÔ!!
```

Utilizando:

```python
print("JO")
time.sleep(0.5)
print("KEN")
time.sleep(0.5)
print("PÔ!!")
time.sleep(0.5)
```

para criar pequenas pausas entre as mensagens.

---

### 4. Escolha do Computador 💻

O computador realiza uma escolha aleatória entre:

* Pedra
ou
* Papel
ou
* Tesoura

Utilizando:

```python
opcao = ['PEDRA', 'PAPEL', 'TESOURA']
escolha_pc = random.choice(opcao)  
```

---

### 5. Design do Jogo

O programa mostra:

#### Sua Escolha

```text
PEDRADA!!
    ______
---'  (____)
      (_____)
      (_____)
      (____)
---.__(___)
```

#### Escolha do Computador

```text
TESOURADA!!
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
```

Os desenhos são obtidos pela função:

```python
mao_opcao()
```

Responsável por retornar o ASCII correspondente a cada opção.

---

### 6. Resultado da Partida

O sistema compara as escolhas.

#### Vitória

```text
AEHH GANHASSE!! (˵ •̀ ᴗ - ˵) ✧!!
```

#### Derrota

```text
foi triste pra tu... kk (¬_¬')
```

#### Empate

```text
DEU EMPATEEE!! ✧｡٩(ˊᗜ ˋ )و✧*｡!!
```

A decisão é feita através de estruturas condicionais.

---

### 7. Jogar Novamente

Ao final da partida:

```text
Deseja jogar novamente? (s/n)
```

### Se responder:

```text
s
```

Uma nova partida começa.

```text
✩₊˚.⋆☾⋆⁺₊✧ (ᵔ ᗜ ᵔ) simbora ++1 jogatina!! ✩₊˚.⋆☾⋆⁺₊✧
```

### Se responder:

```text
n
```

O jogo encerra exibindo uma mensagem de despedida.

```text
✩₊˚.⋆☾⋆⁺₊✧ Adeus!! (ᵔ ᗜ ᵔ) valeu pela jogatina!! ✩₊˚.⋆☾⋆⁺₊✧
```

E novamente é utilizado o método:

```python
.strip().lower()
```

para padronizar a entrada do usuário e evitar erros de interpretação.

### Se responder qualquer outra coisa diferente de S/N:

```text
essa opção não existe! (ᵕ•᷄_•᷅ ) engraçadão
```

---

## 🕹🦴 Estrutura do Código

### Bibliotecas

```python
import random
import time
```

### random

Responsável pela escolha aleatória do computador.

### time

Responsável pelas pausas de suspense.

---

## Função

Responsável por retornar o desenho ASCII correspondente à opção escolhida.

```python
def mao_opcao(opcao):
```

Dependendo da entrada (`pedra`, `papel` ou `tesoura`), a função exibe a arte ASCII adequada.

Função principal do jogo.

```python
def jogo_JKP(): 
```

Responsável por:

1. Receber a entrada do jogador
2. Criar o suspense
3. Sortear a escolha do computador
4. Exibir os desenhos
5. Calcular o resultado

---

## Loop Principal

```python
while True:
```

Mantém o jogo em execução até que o usuário escolha sair.

---

## 💻 Tecnologias Utilizadas 💻

* Python
* Terminal/Console
* Biblioteca Random
* Biblioteca Time

---

## 📚 Conceitos Praticados 📚

* Variáveis
* Funções
* Estruturas condicionais
* Loops
* Entrada e saída de dados
* Manipulação de strings
* Geração aleatória (Random)
* Organização de código

---

## 📜 Descrição Simples 📜

**Jogo Pedra, Papel e Tesoura (Python)**

* Desenvolvimento de jogo para execução em terminal.
* Implementação de lógica de programação e estruturas condicionais.
* Criação de sistema automático de resultados.
* Utilização de escolhas aleatórias com a biblioteca Random.
* Desenvolvimento de interação com usuário via console.
* Organização do código utilizando funções e repetição.

