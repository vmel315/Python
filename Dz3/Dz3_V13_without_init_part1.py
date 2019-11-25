class Bus:
    def __setattr__(self, attr, value):
        if attr == 'driverName':
            self.__dict__[attr] = value
        elif attr == 'busNum':
            self.__dict__[attr] = value
        elif attr == 'routeNum':
            self.__dict__[attr] = value
        elif attr == 'model':
            self.__dict__[attr] = value
        elif attr == 'year':
            self.__dict__[attr] = value
        elif attr == 'milage':
            self.__dict__[attr] = value
        else:
            raise AttributeError

    def get_driverName(self):
        return self.driverName
    def get_busNum(self):
        return self.busNum
    def get_routeNum(self):
        return self.routeNum
    def get_model(self):
        return self.model
    def get_year(self):
        return self.year
    def get_milage(self):
        return self.milage

    def busAge(self,currYear=2019):
        return currYear - self.get_year()


def busInfoOut(i):
    print str(busPark[i].busAge()) + ' years old bus'
    print 'Driver name: ' + busPark[i].get_driverName()
    print 'Bus Num: ' + busPark[i].get_busNum()
    print 'Bus Year: ' + str(busPark[i].get_year())
    print '---------------'

i=0

driverNameArr=['Ivanov I.I.','Andreev A.D','Nikitin M.D','Sergeev S.S.','Pavlov A.P','Artemov B.B','Denisov I.T.','Artemov R.A','Nastasieva N.C','Natalieva I.O.','Vodilov F.A']
busNumArr=['1234 AA-7','1221 MA-7','3244 OP-7','5435 AC-7','0210 PP-7','2313 TO-7','4323 EB-7','5688 TC-7','2322 MP-7','9930 PE-7','1121 IK-7',]
routeNum=[1,73,91,1,1,29,1,91,29,100,100]
model=['MAZ216','MAZ103','MAZ105','MAZ216','MAZ216','MAZ103','MAZ105','MAZ216','MAZ103','MAZ216','MAZ105']
year=[2010,2008,2002,2011,2016,2001,2019,2017,2009,2011,2013]
milage=[40000,72000,240000,40000,72000,440000,40000,272000,640000,30000,732000]

busPark =  [Bus(),Bus(),Bus(),Bus(),Bus(),Bus(),Bus(),Bus(),Bus(),Bus(),Bus()]
while i < len(busPark):
    busPark[i].driverName = driverNameArr[i]
    busPark[i].busNum = busNumArr[i]
    busPark[i].routeNum = routeNum[i]
    busPark[i].model = model[i]
    busPark[i].year = year[i]
    busPark[i].milage = milage[i]
    i+=1
i=0

routeNum=0
termNum=0

routeNum = int(input('Vvedite nomer marshruta \n'))

while i < len(busPark):
    if busPark[i].get_routeNum() == routeNum:
        busInfoOut(i)
    i+=1
i=0
termNum = int(input('Vvedite cpok ekspluatacii \n'))
while i < len(busPark):
    if busPark[i].busAge() > termNum:
        busInfoOut(i)
    i+=1