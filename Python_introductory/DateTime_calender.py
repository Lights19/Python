import calendar 
cal=calendar.TextCalendar(calendar.SUNDAY) # TextCalendar outputs a calendar as a simple lain text
print(cal.formatyear(2018,2,1,1,3))

print(cal.formatmonth(2017,8)) #formatmonth


'''output:
August 2017
Su Mo Tu We Th Fr Sa
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31'''

cmonth = calendar.TextCalendar(calendar.SUNDAY)
#output: <calendar.TextCalendar object at 0x02AAC030>

cmonth.prmonth(2017, 8)

c = calendar.HTMLCalendar(calendar.SUNDAY)  # HTMLCalendar
#output: <calendar.HTMLCalendar object at 0x02AAC270>

print(c.formatmonth(2017,8))

'''output:
<table border="0" cellpadding="0" cellspacing="0" class="month">\n<tr><th colspan="7" class="month">August 2017</th></tr>\n<tr><th class="sun">Sun</th>
<th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th></tr>\n
<tr><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="tue">1</td><td class="wed">2</td><td class="thu">3</td><td class="fri">4</td>
<td class="sat">5</td></tr>\n<tr><td class="sun">6</td><td class="mon">7</td><td class="tue">8</td><td class="wed">9</td><td class="thu">10</td>
<td class="fri">11</td><td class="sat">12</td></tr>\n<tr><td class="sun">13</td><td class="mon">14</td><td class="tue">15</td><td class="wed">16</td>
<td class="thu">17</td><td class="fri">18</td><td class="sat">19</td></tr>\n<tr><td class="sun">20</td><td class="mon">21</td><td class="tue">22</td>
<td class="wed">23</td><td class="thu">24</td><td class="fri">25</td><td class="sat">26</td></tr>\n<tr><td class="sun">27</td><td class="mon">28</td>
<td class="tue">29</td>
<td class="wed">30</td><td class="thu">31</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td></tr>\n</table>\n'  '''

import pprint
pprint.pprint(calendar.monthcalendar(2017, 7))
