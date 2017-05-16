#KIZZA MARVIN JOHN
#16/U/6260/PS
#BSc ELECTRICAL ENGINEERING
import datetime,calendar

cur_year = int(datetime.date.today().strftime('%Y'))

date = input("Enter birth date (1-31)\n")#This prompts the user to input his birth date ranging from 1-31

endings = ["st", "nd", "rd"]+ 17*["th"] + ["st", "nd", "rd"] + 7*["th"] + ["st"]

days = ['Monday','Tuesday','Wednesday',
        'Thursday','Friday','Saturday',
        'Sunday']

month = int(input("Enter month you were born in(1-12)\n"))#This prompts the user to input his birth month ranging from 1-12

month_names = ['January','February','March',
                'April','May','June',
                'July','August','September',
                'October','November','December']

age = int(input("How old are you now? \n"))#This prompts the user to input his age 

vari1 = month_names[month-1]
vari2 = int(date)
vari3 = (cur_year-age)
vari4 = date+endings[vari2-1]
vari5 = calendar.weekday(vari3,month,vari2)
vari6 = days[vari5]

print("You were born on",vari6 ,vari4, vari1,"of the year " ,vari3)#returns the day of the month one was born and the year of birth.
