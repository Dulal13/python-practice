class Train:

    def __init__(self , name,fare,seats):

        self.name = name
        self.fare = fare
        self.seats = set(range(1,301))
    
    lst = []

    def getInfo(self):

        print(f"The name of the train is :{self.name}")
        print(f"The total seats of the trian is : {self.seats}")

    def fareInfo(self):

        print(f"The price of the ticket is : Tk.{self.fare}")
    
    def bookTicket(self):

        if(len(self.seats) > 0):
            print(f'Your ticket is booked.Seat number:{list(self.seats)[-1 ]}')
            a = list(self.seats).pop()
            self.seats.remove(list(self.seats)[-1])
            self.lst.append(a)
            
           
        else:
            print('Try another train.')
    
    def cancelTicket(self):
        self.seats.add(self.lst.pop())

bongo = Train('Bongo Express 101' , 100 , 300)

# bongo.fareInfo()
bongo.bookTicket()
# bongo.getInfo()
# print(bongo.lst)
bongo.bookTicket()
bongo.cancelTicket()
bongo.bookTicket()