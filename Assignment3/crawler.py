from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

html = urlopen("https://www.cpp.edu/sci/computer-science/faculty-and-staff/permanent-faculty.shtml")
bs = BeautifulSoup(html,'html.parser')
# print(bs.body.prettify())
# print(bs.h1)
faculty_count = 0
print("The permanent CS faculty pages are: ")
for link in bs.find_all('a'):
    new_link = link.get('href')
    if ("http://www.cpp.edu/faculty/") in new_link:
        faculty_count += 1
        print(new_link)
    elif "https://www.cpp.edu/faculty/" in new_link:
        faculty_count += 1
        print(new_link)
print("There are",faculty_count,"permanent faculty in the CS department.")
    