import re
import datetime
import os


d1 = datetime.datetime.strptime('2020-06-17', "%Y-%m-%d")
today = datetime.datetime.now().strftime("%Y-%m-%d")
d2 = datetime.datetime.strptime(today, '%Y-%m-%d')
delta = d2 - d1
delta = delta.days

os.system('echo \'- [Day %d (%s)](./diary/%s.md)\' >> README.md' %
          (delta, today, today))

os.system('echo \'# Day %d\n\' >> ./diary/%s.md' % (delta, today))
os.system('echo \'> %s\' >> ./diary/%s.md' % (today, today))
