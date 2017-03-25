# Hint:  use Google to find python function

from datetime import date, datetime

def diff_dates(date1, date2):
	print(abs(date2-date1).days)


####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'  
date_start = datetime.strptime(date_start, '%m-%d-%Y')
date_stop = datetime.strptime(date_stop, '%m-%d-%Y')

diff_dates(date_start, date_stop) 


####b)  
date_start = '12312013'  
date_stop = '05282015'  

date_start = datetime.strptime(date_start, '%m%d%Y')
date_stop = datetime.strptime(date_stop, '%m%d%Y')

diff_dates(date_start, date_stop) 



####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

date_start = datetime.strptime(date_start, '%d-%b-%Y')
date_stop = datetime.strptime(date_stop, '%d-%b-%Y')

diff_dates(date_start, date_stop) 