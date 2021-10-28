import datetime
class Dates:

    monthStr =['січень', 'лютий', 'березень', 'квітень', 'травень', 'червень',
            'липень', 'серпень', 'вересень', 'жовтень','листопад', 'грудень']
    intForStr =['01','02','03','04','05','06','07','08','09','10', '11', '12','13',
                '14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    @day.setter
    def day(self, day):
        if not isinstance(day, int):
            raise TypeError('day should be int type')
        if not(0 < day < 32):
            raise ValueError('only 31 day in month and more then 0')
        self.__day = day

    @month.setter
    def month(self, month):
        if not isinstance(month, int):
            raise TypeError('day should be int type')
        if not(0 < month < 12):
            raise ValueError('more than 0 but less than 13 month')
        self.__month = month

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError('year must be int type')
        self.__year = year

    def get_day(self):
        return self.__day

    def get_month(self):
        return self.__month

    def get_year(self):
        return self.__year

    def date_with_word(self) -> str:
        return f'{self.intForStr[int(self.day-1)]}.' \
               f'{self.monthStr[int(self.month-1)]}.' \
               f'{self.year}'

    def date_with_int(self)-> str:
        return f'{self.intForStr[int(self.day-1)]}.' \
               f'{self.intForStr[self.month-1]}.' \
               f'{self.year}'

    def date_with_datetime(self):
        return datetime.datetime(self.year,  self.month, self.day).strftime("%d.%B.%Y")

if __name__ == '__main__':
    date = Dates(10, 1, 2020)
    print(date.date_with_word())
    print(date.date_with_int())
    print(date.date_with_datetime())

