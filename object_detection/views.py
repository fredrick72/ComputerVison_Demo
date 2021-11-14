from django.shortcuts import render
from datetime import date
import calendar
from calendar import HTMLCalendar

def default(request, year = date.today().year, month = date.today().month):
    year = int(year)
    month = int(month)
    if year < 1900 or year > 2099: year = date.today().year
    month_name = calendar.month_name[month]
    title = "Date - %s %s" % (month_name, year)
    cal = HTMLCalendar().formatmonth(year, month)
    # return HttpResponse("<h1>%s</h1><p>%s</p>" % (title, cal))
    return render(request, 'object_detection/base.html', {'title': title, 'cal': cal})