class MagicCal:

    def __init__(self,x,y):
        self.x=x
        self.y=y
        #self.z=z

    def add(self):
        rslt=int(self.x) + int(self.y)
        return rslt

    def subract(self):
        rslt=int(self.x) - int(self.y)
        return rslt

    def doublenum(self):
        rslt=str(self.x) + str(self.x)
        return rslt

    def precentage(self):
        rslt=int(self.x)/100
        return rslt