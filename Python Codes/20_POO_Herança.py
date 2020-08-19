class NPC: 
    def __init__(self,nome,time,forca,municao):
        self.nome=nome
        self.time=time
        self.forca=forca
        self.municao=municao
        self.vivo=True
        self.energia=100
    def info(self):
        print("Nome...:" + self.nome)
        print("Time...:" + str(self.time))
        print("força..:" + str(self.forca))
        print("munição:" + str(self.municao))
        print("vivo...:" + ("sim" if self.vivo else "Não"))
        print("energia:" + str(self.energia))
        print("-----------------------------------")

class Soldado(NPC):
    def __init__(self,nome,time):
        self.forca=200
        self.municao=200
        super().__init__(nome,time,self.forca,self.municao)

class Guarda(NPC):
    def __init__(self,nome,time):
        self.forca=150
        self.municao=100
        super().__init__(nome,time,self.forca,self.municao)

class Elite(NPC):
    def __init__(self,nome,time):
        self.forca=300
        self.municao=500
        super().__init__(nome,time,self.forca,self.municao)
    def inf(self):
        super().info()

s1=Guarda("Olho vivo", 1)
s2=Soldado("Bala de Agulha", 1)
s3=Elite("Ninja", 1)
s4=Guarda("Super Atento", 2)
s5=Soldado("Tiro Certo", 2)
s6=Elite("Samurai", 2)

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.info()

