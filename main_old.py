import openpyxl
import icalendar
import datetime

# function to convert excel date to python datetime
def excel_to_python_datetime(excel_date):
   # return datetime.datetime(1899, 12, 30) + datetime.timedelta(days=excel_date)
    return excel_date

# read xlsx file
workbook = openpyxl.load_workbook('test.xlsx')
worksheet = workbook.active

# create ics calendar
calendar = icalendar.Calendar()
calendar.add('prodid', '-//My calendar product//mxm.dk//')
calendar.add('version', '2.0')

# loop through rows and add events to calendar
all_courses = set()
for row in worksheet.iter_rows(values_only=True):
    if row[0]:
        date = excel_to_python_datetime(row[0]).date()
    else:
        print('no date pass')
        pass
    morning_course = row[1]
    afternoon_course = row[2]
    if morning_course:
        # create event for morning course
        event = icalendar.Event()
        event.add('summary', morning_course)
        event.add('dtstart', datetime.datetime.combine(date, datetime.time(8, 35)))
        event.add('dtend', datetime.datetime.combine(date, datetime.time(12, 25)))
        calendar.add_component(event)
        all_courses.add(morning_course)
    if afternoon_course:
        # create event for afternoon course
        event = icalendar.Event()
        event.add('summary', afternoon_course)
        event.add('dtstart', datetime.datetime.combine(date, datetime.time(13, 5)))
        event.add('dtend', datetime.datetime.combine(date, datetime.time(16, 55)))
        calendar.add_component(event)
        all_courses.add(afternoon_course)

#print all the courses and ask to select the courses
for i, course in enumerate(all_courses, 1):
    print(f'{i}. {course}')
selected_courses = input("Enter the numbers of the courses you want to save, separated by commas: ").split(',')
selected_courses = [int(course.strip()) for course in selected_courses]

#Filter events according to courses
events_to_save = [event for i, event in enumerate(calendar.subcomponents) if i+1 in selected_courses]

#create new calendar with only the selected events
filtered_calendar = icalendar.Calendar()
filtered_calendar.add('prodid', '-//My calendar product//mxm.dk//')
filtered_calendar.add('version', '2.0')
for event in events_to_save:
    filtered_calendar.add_component(event)

# write ics file
with open('courses.ics', 'wb') as f:
    f.write(filtered_calendar.to_ical())

print(f'Successfully written {len(events_to_save)} events to courses.ics')