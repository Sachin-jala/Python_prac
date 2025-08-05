from random import randint
class Train:
    def __init__(self, trainno, name=None, seats=None):
        self.trainno = trainno
        
    def bookticket(self, fro, to):
        print(f"Ticket booked train no: {self.trainno} from {fro} to {to}")

    def getstaous(self):
        print(f"Status of train no: {self.trainno} is running")

    def getfare(self, fro, to):
        print(f"fare in train no: {self.trainno} from {fro} to {to} is {randint(100, 555)}")

t = Train(12399)
t.bookticket("delhi", "mumbai")
t.getstaous()
t.getfare("delhi", "mumbai")