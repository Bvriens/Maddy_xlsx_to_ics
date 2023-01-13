import icalendar
import datetime


class EventHandler:
    def __init__(self):
        self.course_events = {}

    def generateEvent(self, event_summary, date, event_start, event_end):
        event = icalendar.Event()
        event.add("summary", event_summary)
        event.add("dtstart", datetime.datetime.combine(date, event_start))
        event.add("dtend", datetime.datetime.combine(date, event_end))

        return event

    def addEvent(self, course, date, event_start, event_end):
        event = self.generateEvent(course, date, event_start, event_end)
        eventlist = self.course_events.get(course, [])
        eventlist.append(event)
        self.course_events[course] = eventlist

    def getCourses(self):
        return list(self.course_events.keys())

    def getEventsList(self, selected_courses):
        event_list = []
        for course in selected_courses:
            event_list.extend(self.course_events[course])

        return event_list

    def printEvents(self):
        for key in self.course_events.keys():
            print(key)
            print(self.course_events[key])
