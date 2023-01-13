import datetime


# function to check the date
class DateHandler:
    @staticmethod
    def check_date(excel_date):
        if isinstance(excel_date, datetime.date):
            return excel_date
        else:
            raise Exception("This is not a date!")
