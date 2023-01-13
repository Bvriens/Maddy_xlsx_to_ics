import icalendar
import datetime


class EventHandler:
    def __init__(self):
        self.course_events = {}

    def addEvent(self, course, date, event_start, event_end):
        event = self._generateEvent(course, date, event_start, event_end)
        eventlist = self.course_events.get(course, [])
        eventlist.append(event)
        self.course_events[course] = eventlist

    def getCourses(self):
        return list(self.course_events.keys())

    def generateCalendar(self, selected_courses):
        # Get events according to selected courses
        events_to_save = self._getEventsList(selected_courses)
        number_of_events = len(events_to_save)

        calendar = icalendar.Calendar()
        calendar.add("prodid", "-//My calendar product//mxm.dk//")
        calendar.add("version", "2.0")

        for event in events_to_save:
            calendar.add_component(event)

        return calendar, number_of_events

    def _getEventsList(self, selected_courses):
        event_list = []
        for course in selected_courses:
            event_list.extend(self.course_events[course])

        return event_list

    def _generateEvent(self, event_summary, date, event_start, event_end):
        event = icalendar.Event()
        event.add("summary", event_summary)
        event.add("dtstart", datetime.datetime.combine(date, event_start))
        event.add("dtend", datetime.datetime.combine(date, event_end))

        return event

    def printEvents(self):
        for key in self.course_events.keys():
            print(key)
            print(self.course_events[key])
