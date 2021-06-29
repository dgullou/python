import re

line = '127.0.0.1 - rj [13/Nov/2019:14:43:30 -0800] "GET HTTP/1.0" 200 2326'
#?P可以幫GROUP命名
m = re.search(r'(?P<ip>\d+.\d+.\d+.\d+)',line)
print(m.group('ip'))
r = r'(?P<time>\[\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2} -\d{4}\])'


r1 = r' - (?P<user>\w+) '
m1 = re.search(r,line)
m2 = re.search(r1, line)
print(m1.group('time'))

print(m2.group('user'))
m3 = re.search(r'(?P<request>".+")',line)
print(m3.group('request'))