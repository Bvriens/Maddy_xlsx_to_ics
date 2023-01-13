import openpyxl
import datetime
from handlers import EventHandler, FileHandler, DateHandler, InputHandler

# Set up logging
import logging

logging.basicConfig(level=logging.ERROR)


event_handler = EventHandler()
file_handler = FileHandler()

morning_start_time = datetime.time(8, 35)
morning_end_time = datetime.time(12, 25)
afternoon_start_time = datetime.time(13, 5)
afternoon_end_time = datetime.time(16, 55)

# read xlsx file
try:
    filename = file_handler.select_file()
    workbook = openpyxl.load_workbook(filename)
    worksheet = workbook.active
except Exception as e:
    print("couldn't load xlsx file!")
    raise e

# loop through rows and add events to eventhandler
for idx, row in enumerate(worksheet.iter_rows(values_only=True)):
    try:
        if row[0]:
            date = DateHandler.check_date(row[0]).date()
        else:
            print("no date pass")
            continue

        morning_course = row[1]
        afternoon_course = row[2]

        if morning_course:
            print("morning", morning_course, date, morning_start_time, morning_end_time)
            event_handler.addEvent(morning_course, date, morning_start_time, morning_end_time)

        if afternoon_course:
            print("afternoon", afternoon_course, date, afternoon_start_time, afternoon_end_time)
            event_handler.addEvent(afternoon_course, date, afternoon_start_time, afternoon_end_time)
    except Exception as e:
        raise Exception(e, "on row " + idx)

logging.debug("*** printEvents *******************")
logging.debug(event_handler.printEvents)
logging.debug("***********************************")

# print all the courses and ask to select the courses
course_list = event_handler.getCourses()
selected_courses = InputHandler.select_courses(course_list)

# create new calendar with only the selected events
(calendar, number_of_events) = event_handler.generateCalendar(selected_courses)

# write ics file
with open("courses.ics", "wb") as f:
    f.write(calendar.to_ical())

print(f"Successfully written {number_of_events} events to courses.ics")
