# JKP_THEGAME
#um simples jogo de pedra, papel e tesoura.
# jokenpo/GAME_JKP.py

# JOGO MARAVILHOSO :D ----------------------------------------

# BIBLIOTECAS ----------- 
import random
import time 

# opções de mões draws ------------- 
def mao_opcao(opcao):
    if opcao == 'PEDRA':
        return '''\r
PEDRADA!!
    ______
---'  (____)
      (______)
      (_______)
      (______)
---.__(_____)
'''
    if opcao == 'PAPEL':
        return '''\r
PAPELADA!!
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
    if opcao == 'TESOURA':
        return '''\r 
TESOURADA!!
    _______
---'   ____)____
          ______)
          |______
       __________)
      (____)
---.__(___)
'''

# inicio de tudo ---------------------------------------------------------- 
def jogo_JKP(): 
    print('₊‧.°.⋆✮⋆.°.‧₊ ⛧°。 ⋆༺✮༻⋆。 °⛧ ₊‧.°.⋆✮⋆.°.‧₊')
    print('''✧₊⁺Que tal um JoKenPô??⁺₊✧
          ''') 
    escolha_jogador = input('⋆.˚✮ PEDRA, PAPEL ou TESOURA!! ✮˚.⋆\n').strip().upper()
    
    # time ------------------------------------------------    
    print("JO")
    time.sleep(0.5)
    print("KEN")
    time.sleep(0.5)
    print("PÔ!!")
    time.sleep(0.5)
    
    # escolhas pc -------------------------------------------------    
    opcao = ['PEDRA', 'PAPEL', 'TESOURA']
    escolha_pc = random.choice(opcao)          
    
    # Verificação de resposta ------------------------------------ 
    if escolha_jogador not in opcao:
        print('''essa opção não existe pilantra! (╭ರ_•́)??''')    
        print('''aqui não é terra sem lei (ᴗ˳ᴗ)ᶻ𝗓𐰁''')
                
    else:  
        print(f"Você escolheu:{escolha_jogador}")
        print(mao_opcao(escolha_jogador))

        print(f"PC escolheu:{escolha_pc}")
        print(mao_opcao(escolha_pc))  
        
        # escolhas jogador ----------------------------------------- 
        if escolha_jogador == escolha_pc:
            print("DEU EMPATEEE!! ✧｡٩(ˊᗜ ˋ )و✧*｡!! ")
        elif (
            (escolha_jogador == 'PEDRA' and escolha_pc == 'TESOURA') or
            (escolha_jogador == 'PAPEL' and escolha_pc == 'PEDRA') or
            (escolha_jogador == 'TESOURA' and escolha_pc == 'PAPEL')
        ):
            print("AEHH GANHASSE!! (˵ •̀ ᴗ - ˵) ✧!!")
        else:
            print("Foi triste pra tu... kk (¬_¬')") 
            
# Opção de continuar ou sair d JKP ------------------------------------ 
while True:
    jogo_JKP()
    print('₊‧.°.⋆✮⋆.°.‧₊ ⛧°。 ⋆༺✮༻⋆。 °⛧ ₊‧.°.⋆✮⋆.°.‧₊')
    print('''✧₊⁺Que tal ir mais uma, hein??⁺₊✧
          ''')
    resposta = input("digite s ou n:\n").strip().lower()
    if resposta == 's':
        print('''✩₊˚.⋆☾⋆⁺₊✧ (ᵔ ᗜ ᵔ) simbora ++1 jogatina!! ✩₊˚.⋆☾⋆⁺₊✧
              ''') 
        continue
    elif resposta == 'n':
        print('''✩₊˚.⋆☾⋆⁺₊✧ Adeus!! (ᵔ ᗜ ᵔ) valeu pela jogatina!! ✩₊˚.⋆☾⋆⁺₊✧
              ''') 
        print(
        r'''
    |\__/,|   (`\
  _.|o o  |_   ) )
-(((---(((-------- Gatinho de ASCII pra alegrar o dia :D
            ''')
        print('₊‧.°.⋆✮⋆.°.‧₊ ⛧°。 ⋆༺✮༻⋆。 °⛧ ₊‧.°.⋆✮⋆.°.‧₊')
        break
    else:
        print('''essa opção não existe! (ᵕ•᷄_•᷅ ) engraçadão
               ''')
        break
# um jogo bastante interessante 
# chamado JoKenPô :O (JKP pro mais íntimos)
