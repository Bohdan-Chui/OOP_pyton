from Tickets import *
import json
from  datetime import datetime


class TicketManager:
    def __init__(self):
        self.data = {'ticket': []}

    def __get_tickets_number(self):
        number = 0
        with open('tickets.json') as file:
            data = json.load(file)
            for p in data['ticket']:
                number+=1
            return  number

    def __get_ticket(ticket):
        type = ticket['type']
        number = ticket['number']
        visitor = ticket['visitor']
        event_date = datetime.strptime(ticket['event_date'], '%Y-%m-%d').date()
        price = ticket['price']

        if type == 'regular':
            return RegularTicket(number, visitor,  event_date, price)
        elif type == 'advance':
            return AdvanceTicket(number, visitor,  event_date, price)
        elif type == 'late':
            return LateTicket(number, visitor,  event_date, price)
        elif type == 'student':
            return StudentTicket(number, visitor,  event_date, price)
        else:
            raise ValueError('unknown ticket')

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @staticmethod
    def __encoder(ticket):
        return {
            'type': ticket.type,
            'number': ticket.number,
            'visitor': ticket.visitor,
            'event_date': ticket.event_date.isoformat(),
            'price': ticket.price
        }

    def save_ticket(self, ticket):
        if not isinstance(ticket, RegularTicket):
            TypeError('not Ticket type')
        self.__data['ticket'].append(self.__encoder(ticket))
        with open('tickets.json', 'w') as file:
            json.dump(self.__data, file, indent = 4)

    def get_ticket_by_number(self,  number):
        with open('tickets.json') as file:
            data = json.load(file)
            for p in data['ticket']:
                if p['number'] == number:
                    return TicketManager.__get_ticket(p)

    def __buy_ticket(self, type,number, visitor, event_date, price):
        if type == 'regular':
            ticket =  RegularTicket(number, visitor,  event_date, price)
        elif type == 'advance':
            ticket = AdvanceTicket(number, visitor,  event_date, price)
        elif type == 'late':
            ticket = LateTicket(number, visitor,  event_date, price)
        elif type == 'student':
            ticket = StudentTicket(number, visitor,  event_date, price)
        else:
            raise ValueError('unknown ticket')
        print('good choise')
        self.save_ticket(ticket)


    def buy_ticket(self, event):
        difference = (event.date_event-date.today()).days
        print('Hello, my customer\n Your event: \n' + str(event))
        name = input(f"Enter your name: ")
        if input(f"Would you like to buy ticket Y/N ?").lower() == "y":
            if input(f"Are you a student? Y/N ?").lower() == "y":
                self.__buy_ticket('student', self.__get_tickets_number()+1,name,event.date_event, event.regular_price )
                return
            if difference > 60 :
                if input(f"Would you like to buy advance ticket? Y/N ?").lower() == "y":
                    self.__buy_ticket('advance', self.__get_tickets_number() + 1, name, event.date_event, event.regular_price)
                    return
            else:
                if difference < 10:
                    if input(f"Would you like to buy late ticket? Y/N ?").lower() == "y":
                        self.__buy_ticket('late', self.__get_tickets_number()+1, name, event.date_event, event.regular_price )
                        return
            if input(f"Would you like to buy regular ticket? Y/N ?").lower() == "y":
                self.__buy_ticket('regular', self.__get_tickets_number() + 1, name, event.date_event, event.regular_price)
                return
        print('goodbye')
        return






