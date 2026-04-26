import datetime
x = datetime.datetime.now()
print(x) # 2026-02-27 19:17:48.623531

import datetime
x = datetime.datetime.now()
print(x.year) # 2026
print(x.strftime("%A")) # Friday

x = datetime.datetime(2020, 5, 17)
print(x) # 2020-05-17 00:00:00
print(x.strftime("%B")) # May

'''
%a	Weekday, short version	        | Wed	
%A	Weekday, full version	        | Wednesday	
%w	Weekday as a number 0-6, 	    | 3	
%d	Day of month 01-31	            | 31	
%b	Month name, short version	    | Dec	
%B	Month name, full version	    | December	
%m	Month as a number 01-12	        | 12	
%y	Year, short version             | 18	
%Y	Year, full version	            | 2018	
%H	Hour 00-23	                    | 17	
%I	Hour 00-12	                    | 05	
%p	AM/PM                       	| PM	 
%M	Minute 00-59	                | 41	
%S	Second 00-59	                | 08	
%f	Microsecond 000000-999999	    | 548513	
%z	UTC offset	                    | +0100	
%Z	Timezone	                    | CST	
%j	Day number of year 001-366	    | 365	
%c	Local version of date and time	| Mon Dec 31 17:41:00 2018	
%C	Century	                        | 20	
%x	Local version of date	        | 12/31/18	
%X	Local version of time          	| 17:41:00
'''