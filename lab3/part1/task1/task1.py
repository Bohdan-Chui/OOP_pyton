from Tickets import *
from Event import Event
from TicketManager import TicketManager
from datetime import date
from EventManager import EventManager

def main():
    event = Event('1event', date(2002, 12, 12), 120)
    ticketmanaget = TicketManager()
    eventmanager = EventManager()
    ticketmanaget.buy_ticket(event)
    print(ticketmanaget.get_ticket_by_number(2))
main()