'''Modle for aircraft flights.'''

class Flight:


    def __init__(self,number,aircraft):

        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")

        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")

        if not (number[2:].isdigit() and int(number[2:]) <=9999):
            raise ValueError(f"Invalid route Number '{number}'")

        self.number2= number
        self._aircraft = aircraft

    def number(self):
        return self.number2


    def airline(self):
        return self.number2[:2]

    def aircraftDetails(self):
        return (f"Regsitration: {self._aircraft.registration()}, modle: {self._aircraft.model()}, seating: {self._aircraft.seatingArrangement()}")

class Aircraft:

    def __init__(self,registration,model,numberOfRows,numberOfSeats):
        self._registration= registration
        self._model=model
        self._numberOfRows=numberOfRows
        self._numberOfSeats=numberOfSeats

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seatingArrangement(self):
        return (range(1,self._numberOfRows+1),"ABCDEFHG"[:self._numberOfSeats])


name = 123
print(f"My name is {name}")
'''
Obj = Flight("WE9999")
print(Obj.number())
print(f"flight is '{Obj.airline()}'")
'''

aircraft = Aircraft("ADF-DD","Model2",12,3)
Obj = Flight("WE9999",aircraft)
print(Obj.number())
print(Obj.aircraftDetails())






