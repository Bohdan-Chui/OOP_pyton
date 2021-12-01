from Tickets import *
from Event import Event
from TicketManager import TicketManager
from datetime import date
from EventManager import EventManager

def main():
    event = Event('2event', date(2021, 12, 12), 120)
    ticketmanaget = TicketManager()
    # eventmanager = EventManager()
    ticketmanaget.buy_ticket(event)
main()