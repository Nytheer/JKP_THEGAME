## Documentação do game!!
Como funciona o cod do jogo "JKP" no PYTHON??

JKP_THEGAME: Guia do Jogador e Documentação do Código
Um simples e divertido jogo de Pedra, Papel e Tesoura feito em Python!

🕹 Como Jogar 🕹

1. Quando o jogo iniciar, ele vai perguntar:

   ✧₊⁺Que tal um JoKenPô??⁺₊✧  
   ⋆.˚✮ PEDRA, PAPEL ou TESOURA!! ✮˚.⋆

2. Digite sua escolha (não se preocupe com letras maiúsculas/minúsculas).

3. O jogo vai exibir: JO... KEN... PÔ (o famoso suspense)!

4. Em seguida, o jogo mostra:

   - Sua mão (em ASCII e texto)
   - Escolha do computador (em ASCII e texto)
   - Resultado (Vitória, Derrota ou Empate)

5. Depois, você decide se quer jogar de novo.

Algo bem simples, porém, divertido!!

🤓 Organização do Código 🤓

1. Bibliotecas Importadas:
import random — sorteio do PC
import time — pausas para suspense

2. Função mao_opcao(opcao)
Retorna os desenhos ASCII de PEDRA, PAPEL ou TESOURA.

3. Função jogo_JKP()
Executa o jogo:
- Recebe escolha do jogador (input + .upper()+ .strip() +.lower())
- Suspense com time.sleep 
- Escolha aleatória do PC (random.choice)
- Mostra os resultados com desenhos e mensagens brabas

4. Loop principal
while True:
    jogo_JKP()
    Pergunta se quer jogar de novo (s ou n) (.strip()+.lower())
    Se 'n', o jogo termina com uma despedida em ASCII Art
    Se for uma opção diferente de "n ou s" exibe:
    "essa opção não existe! (ᵕ•᷄_•᷅ ) engraçadão"

🎁 ASCII final 🎁
    |\__/,|   (`\
  _.|o o  |_   ) )
-(((---(((--------
Divirta-se!

