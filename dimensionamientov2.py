class getConsume():

  def __init__(self):
    self.number_bim = 7

  def consumo1(self):
    list_ = []
    for i in range(1, self.number_bim):
      consumo = float(input(f"Ingrese el consumo del bimestre {i}:"))
      list_.append(consumo)
    tot_consume = sum(list_)
    return tot_consume


class CalculoSolar():
  def __init__(self, total_consume):
    self.total_consume = total_consume

  def getAvgProm(self):
    self.b_number = 6
    self.avgConsume = self.total_consume / self.b_number
    return self.avgConsume

  def getenergy(self):
    self.c_number = 60
    self.energy = self.avgConsume/self.c_number
    return self.energy

  def getpfv(self):
    self.fp = 0.77
    self.hourpi = float(input("Horas pico:"))
    self.pfv = self.energy/(self.hourpi*self.fp)
    return self.pfv

  def getmodule(self):
    self.d_number = 1000
    self.module = float(input("Potencia del modulo:"))
    self.n_module = self.pfv/(self.module/self.d_number)
    return self.n_module


  def printOutputData(self):
    print("Consumo:", self.total_consume)
    print("Total:",self.avgConsume)
    print("Energia requerida:",self.energy)
    print("PFV:", self.pfv)
    print("Numero de modulos:",self.n_module)

#### First class used
consume = getConsume()
tot_con = consume.consumo1()

###Second Object Used
c = CalculoSolar(tot_con)
c.getAvgProm()
c.getenergy()
c.getpfv()
c.getmodule()
c.printOutputData()

  
   