#RETURN DATE IN THE DESIRED FORMAT (FOR PACKAGE EXAMPLE)
#Santiago Garcia Arango
#One of the modules to show how to create a simple package in python.

import datetime

class date:
    def __init__(self):
        #We use the datetime library to obtain a format of the current moment (when class is created)
        now_info = datetime.datetime.now()
        self.year = now_info.strftime( "%Y" )
        self.month = now_info.strftime( "%B" )
        self.day = now_info.strftime( "%d" )
        self.date = now_info.strftime( "%d/%B/%Y" )

    def return_day(self):
        return( self.day )

    def return_month(self):
        return( self.month )

    def return_year(self):
        return( self.year )

    def return_date(self):
        return( self.date )



#SIMPLE TESTS TO VERIFY FUNCTIONALITY
#------------------------------------------------------
# TEST = date()
# print( TEST.return_day() )
# print( TEST.return_month() )
# print( TEST.return_year() )
# print( TEST.return_date() )
