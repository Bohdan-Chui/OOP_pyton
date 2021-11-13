import json
from Event import Event
from datetime import datetime


class EventManager:
    def __init__(self):
        self.data = {'event':[]}

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @staticmethod
    def __encoder(event):
        return {"name": event.name,
                "date":event.event_date.isoformat(),
                "regular_price": event.regular_price}

    def add_event(self, event):
        if not isinstance(event, Event):
            TypeError('not Event type')
        self.__data['event'].append(self.__encoder(event))
        print(self.data)
        with open('event.json', 'w') as file:
            json.dump(self.__data, file, indent = 4)

    def get_event_by_name(self, name):
        with open('event.json') as file:
            data = json.load(file)
            for p in data['event']:
                if p['name'] == name:
                    return Event(p['name'], datetime.strptime(p['date'], '%Y-%m-%d').date(), p['regular_price'])
                else:
                    ValueError('no such event')
