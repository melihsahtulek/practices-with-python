import random
# OYUN KURALLARI BU SAYFADAN ALINMIŞTIR...: http://www.csystem.org/calisma-sorulari/craps-oyunu
class CrapsGame:
    def __init__(self,ad):
        self.ad = ad

    def gameLogin(self):
        print('Oyuna Hoşgeldin...:', self.ad)
        print('Oyun Başlıyor...')

    def dice(self):
        n1 = 0 ; n2 = 0
        for i in range(1, 2 + 1):
            n1 = random.randint(1,6)
            n2 = random.randint(1,6)
        return n1 , n2

    def play(self):
        gameAgain = int(input('OYUNU KAÇ DEFA OYNAMAK İSTERSİN...:'))
        print('-----------------------------------')
        winN = 0
        for a in range(1, gameAgain + 1):
            self.gameLogin() ; control = True ; continueGame = []
            while True:
                diceNumbers = [] ; diceSum = 0  
                for i in self.dice():
                    diceNumbers.append(i)
                
                for j in range(len(diceNumbers)):
                    diceSum += diceNumbers[j]

                if diceSum == 7 or diceSum == 11:
                   print('Oyunu Kazandın...' , diceNumbers , "=" , diceSum)
                   winN += 1
                   break
                    
                elif diceSum == 2 or diceSum == 3 or diceSum == 12:
                    print('Oyunu Kaybettin...' , diceNumbers , "=" , diceSum)
                    break
                else:
                    # oyuna devam et.
                    continueGame.append(diceSum)
                    print('Oyun Devam Ediyor...')

                    for i in range(len(continueGame)):
                        if 7 in continueGame:
                            print('Sonradan Kaybettin...:', diceNumbers , "=" , diceSum)
                            control = False
                        elif diceSum in continueGame:
                            print('Sonradan Kazandın...', diceNumbers , "=" , diceSum)
                            winN += 1
                            control = False
                            
                if control == False:
                    break
                
            print('--------------------------------')
        
        print('')        
        print('TEKRAR SAYISI',gameAgain, 'KAZANILAN OYUN SAYISI...:', winN)
        print('KAZANMA OLASILIĞI...: %',(winN / gameAgain) * 100)      
                        
            

player_1 = CrapsGame('Player One')
player_1.play()


