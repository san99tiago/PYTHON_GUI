#SIMPLE SCRIPT TO CALL MY OWN PYTHON PACKAGE
#Santiago Garcia Arango

#We import our own created package modules (located in the same directory)
from my_package.my_dates.date_now import date
from my_package.my_names.names import name_generator


#We test the first package with the corresponding methods of class "date"
CURRENT_DATE = date()

print( "\n\nTESTING <MY_DATES> PACKAGE WITH MODULE [DATE_NOW]:")
print( "--> DAY: ", CURRENT_DATE.return_day() )
print( "--> MONTH: ", CURRENT_DATE.return_month() )
print( "--> YEAR: ", CURRENT_DATE.return_year() )
print( "--> DATE: ", CURRENT_DATE.return_date() )


#We test the second package with the corresponding methods of class "name_generator"
COOL_NAMES = name_generator()

print( "\n\nTESTING <MY_NAMES> PACKAGE WITH MODULE [NAMES]:")
print( "--> FIRST_NAME = ", COOL_NAMES.return_first_name() )
print( "--> LAST_NAME = ", COOL_NAMES.return_last_name() )
