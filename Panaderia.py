class Panaderia:
    def __init__(self, panes, pastas):
        self.panes=panes
        self.pastas=pastas
        print(" la panaderia tiene {} panes y {} pastas pero no se venden".format(self.panes,self.pastas))
    
    def vender(self):
        if self.panes>0 :
            print('pan vendido')
            self.panes-=1
        else:
            print('no hay mas panes lo sentimos')
    def cocinnar(self,piezas):
        self.panes+=piezas
        print('quedan {} panes'.format(self.panes))

panaderia1=Panaderia(3,4)
panaderia2=Panaderia(1,3)

panaderia1.vender()
panaderia1.vender()

panaderia1.cocinnar(1)
panaderia1.vender() 