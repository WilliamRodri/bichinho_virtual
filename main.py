import time
import os

class Pet:
    def __init__(self, nome):
        self.nome = nome
        self.idade = 1
        self.vida = 100
        self.fome = 50
        self.sono = 35
        self.alegria = 70
    
    #metodos padroes
    def nascer(self):
        print(f"{self.nome} está vivo!")
    def morreu(self):
        print(f"{self.nome} infelizmente faleceu!")
    def brincar(self):
        print(f"{self.nome} está brincando e seu nivel de felicidade estar aumentando!")
        print(f"Estado Atual:\nVida: {self.vida}% | Fome: {self.fome}% | Alegria: {self.alegria}% | Sono: {self.sono}%")
        self.alegria += 15
    def cansado(self):
        print(f"Como o {self.nome} está brincando muito ele está ficando com sono!")
        print(f"Estado Atual:\nVida: {self.vida}% | Fome: {self.fome}% | Alegria: {self.alegria}% | Sono: {self.sono}%")
        self.sono += 20
        self.fome += 20
    def faminto(self):
        print(f"{self.nome} esta faminto alimente ele para que ele não venha ficar adoentado!")
        print(f"Estado Atual:\nVida: {self.vida}% | Fome: {self.fome}% | Alegria: {self.alegria}% | Sono: {self.sono}%")
        self.fome += 20
    def triste(self):
        print(f"{self.nome} ultimamente está muito triste leve o para brincar ou ele pode acabar morrendo de depressão!")
        print(f"Estado Atual:\nVida: {self.vida}% | Fome: {self.fome}% | Alegria: {self.alegria}% | Sono: {self.sono}%")
        self.alegria -= 15
    def doente(self):
        print(f"{self.nome} está muito doente de comida a ele e o leve para brincar!")
        print(f"Estado Atual:\nVida: {self.vida}% | Fome: {self.fome}% | Alegria: {self.alegria}% | Sono: {self.sono}%")
        self.alegria -= 15
        self.vida -= 15
        self.fome -= 5
    def feliz(self):
        print(f"{self.nome} está muito feliz!")
        print(f"Estado Atual:\nVida: {self.vida}% | Fome: {self.fome}% | Alegria: {self.alegria}% | Sono: {self.sono}%")
    #metodos caso um atributo chegue ao minino ou no maximo possivel!
    def idadeMinMax(self):
        if self.idade == 100:
            os.system('cls')
            print(f"{self.nome} infelizmente faleceu ao chegar aos 100 anos de idade")
            print("Teve um vida longa!")
            self.idade = 100
            self.morreu()
        elif self.idade == 0:
            os.system('cls')
            self.idade = 0
            self.morreu()
    def fomeMinMax(self):
        if self.fome == 100:
            os.system('cls')
            print(f"{self.nome} está satisfeito")
            print("Não precisa ser alimentado no momento!")
            self.fome = 100
        elif self.fome == 0:
            os.system('cls')
            self.fome = 0
            self.vida = 0
            self.morreu()
    def sonoMinMax(self):
        if self.sono == 100:
            os.system('cls')
            print(f"{self.nome} dormiu o bastante já!")
            print(f"{self.nome} está pronto para brincar!")
            self.sono = 100
        elif self.sono == 0:
            os.system('cls')
            print(f"{self.nome} está caindo no sono, ele precisa dormi ou ele pode ficar doente!")
            self.vida -= 5
            self.sono = 0
    def alegriaMinMax(self):
        if self.alegria == 100:
            os.system('cls')
            self.cansado()
            self.alegria = 100
        elif self.alegria == 0:
            os.system('cls')
            self.triste()
            self.triste = 0
    #metodos para informa o usuario de algo para que ele realize uma ação com o pet
    def vidaBaixa(self):
        if self.vida <= 85 and self.vida == 75:
            print(f"{self.nome} está com o nivel de vida baixo! | Vida: {self.vida}")
            print(f"{self.nome} fique atento!")
        elif self.vida <= 65 and self.vida == 50:
            print(f"{self.nome} está com o nivel de vida baixo da metade! | Vida: {self.vida}")
            print(f"{self.nome} leve ele para brincar, comer ou dormi para mudar isso!")
        elif self.vida <= 35 and self.vida <= 15:
            print(f"{self.nome} está com o nivel de vida muito baixo! | Vida: {self.vida}")
            print(f"{self.nome} leve ele para brincar, comer ou dormi para resolver isso ou ele podera morrer!")
        elif self.vida <= 10 and self.vida <= 5:
            print(f"{self.nome} está preste a morrer! | Vida: {self.vida}")
            print(f"{self.nome} leve o urgentemente para brincar e comer!")
        elif self.vida == 0:
            self.morreu()
    def fomeBaixa(self):
        if self.fome <= 85 and self.fome == 75:
            print(f"{self.nome} está com o nivel de fome baixo! | Vida: {self.vida}")
            print(f"{self.nome} fique atento!")
        elif self.fome <= 65 and self.fome == 50:
            print(f"{self.nome} está com o nivel de fome baixo da metade! | Vida: {self.vida}")
            print(f"{self.nome} leve ele para comer para mudar isso!")
        elif self.fome <= 35 and self.fome <= 15:
            print(f"{self.nome} está com o nivel de fome muito baixo! | Vida: {self.vida}")
            print(f"{self.nome} leve ele para comer para resolver isso ou ele podera morrer de fome!")
        elif self.fome <= 10 and self.fome <= 5:
            print(f"{self.nome} está preste a morrer! | Vida: {self.vida}")
            print(f"{self.nome} leve o urgentemente para comer!")
        elif self.fome == 0:
            self.morreu()
    def sonoAlto(self):
        if self.sono == 100:
            self.morreu()
        elif self.sono <= 95 and self.sono == 85:
            print(f"{self.nome} está com muito sono leve ele urgentemente para dormi | Vida: {self.vida}")
        elif self.sono <= 65 and self.sono == 50:
            print(f"{self.nome} esta ficando mais cansando leve-o para descansar! | Vida: {self.vida}")
        elif self.sono <= 35 and self.sono <= 15:
            print(f"{self.nome} esta se cansando mais continua ativo para brincar! | Vida: {self.vida}")
        elif self.sono >= 5 and self.sono <= 10:
            print(f"{self.nome} esta bem ativo para brincar! | Vida: {self.vida}")
        elif self.sono == 0:
            self.feliz()
    def alegriaBaixa(self):
        if self.alegria <= 85 and self.alegria == 75:
            print(f"{self.nome} está com o nivel de alegria se abaixando! | Vida: {self.vida}")
            print(f"{self.nome} fique atento!")
        elif self.alegria <= 65 and self.alegria == 50:
            print(f"{self.nome} está com o nivel de alegria baixo da metade! | Vida: {self.vida}")
            print(f"{self.nome} leve ele para comer para mudar isso!")
        elif self.alegria <= 35 and self.alegria <= 15:
            print(f"{self.nome} está com o nivel de alegria muito baixo! | Vida: {self.vida}")
            print(f"{self.nome} leve ele para brincar para resolver isso ou ele podera morrer!")
        elif self.alegria <= 10 and self.alegria <= 5:
            print(f"{self.nome} está preste a morrer! | Vida: {self.vida}")
            print(f"{self.nome} leve o urgentemente para brincar!")
        elif self.alegria == 0:
            self.morreu()
    #Ações
    def comer(self):
        os.system('cls')
        print(f"{self.nome} esta se alimentado")
        self.fome -= 10
        time.sleep(1)
        self.hud()
    def brincar(self):
        os.system('cls')
        print(f"{self.nome} estar brincando!")
        self.alegria += 15
        self.sono += 20
        self.fome += 25
        time.sleep(1)
        self.hud()
    def dormi(self):
        os.system('cls')
        print(f"{self.nome} estar dormindo!")
        self.alegria += 5
        self.sono -= 90
        self.fome += 35
        time.sleep(1)
        self.hud()
    #Opções de ações
    def hud(self):
        while True:
            print(f"Pet: {self.nome}\nEstado Atual:\nVida: {self.vida}% | Fome: {self.fome}% | Alegria: {self.alegria}% | Sono: {self.sono}%")
            print(f"Escolha oque deseja fazer")
            hud = int(input("[1]Comer\n[2]Brincar\n[3]Dormi\n"))
            try:
                if hud == 1:
                    self.comer()
                    break
                elif hud == 2:
                    self.brincar()
                    break
                elif hud == 3:
                    self.dormi()
                    break
                else:
                    print("Escolha uma das ações apresentadas!")
                    continue
            except Exception as Error:
                print(Error)
    def start(self):
        self.hud()
        self.idadeMinMax()
        self.fomeMinMax()
        self.sonoMinMax()
        self.alegriaMinMax()
        self.vidaBaixa()
        self.fomeBaixa()
        self.sonoAlto()
        self.alegriaBaixa()


print("Seja bem vindo ao simulador de Pet")
nome = input("Informe o nome do seu Pet: ")    
petStart = Pet(nome)
os.system('cls')
petStart.nascer()
petStart.start()