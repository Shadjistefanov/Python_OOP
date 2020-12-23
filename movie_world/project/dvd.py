class DVD:
    is_rented = False
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction

    _months_by_number = {
        '1': 'January',
        '2': 'February',
        '3': 'March',
        '4': 'April',
        '5': 'May',
        '6': 'June',
        '7': 'July',
        '8': 'August',
        '9': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December',
    }

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {self.is_rented}"
    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        day, month, year, *rest = date.split('.')

        creation_month = cls._months_by_number[month]
        return cls(name, id, int(year), creation_month, age_restriction)
