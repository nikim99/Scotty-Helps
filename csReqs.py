import requests
from bs4 import BeautifulSoup

url = 'https://csd.cmu.edu/content/bachelors-curriculum-admitted-fall-2012-and-2013'
urlH = 'https://csd.cmu.edu/undergraduate/bscs-humanities-and-arts-requirements'
page = requests.get(url)
pageH = requests.get(urlH)
text = page.text
textH = pageH.text
soup = BeautifulSoup(text, 'html.parser')
soupH = BeautifulSoup(textH, 'html.parser')
c = soup.find_all(class_='bd')
cH = soupH.find_all('strong')
cHb = soupH.find_all('b')
ctext = [celem.get_text() for celem in c]
cHtext = [cHelem.get_text() for cHelem in cH]
cHbtext = [cHbelem.get_text() for cHbelem in cHb]
cHtext += cHbtext
splitCs=0
splitMath=0
strElem = []
for i in range(0, len(ctext)):
    if " " in ctext[i]:
        ctext[i]=''
delS = 0
delE = 0
for i in range(0, len(cHtext)):
    if cHtext[i] == "36-xxx":
        delS = i
    if cHtext[i] == "88-372":
        delE = i
cHtext1=[]
cHtext = cHtext[:delS] + cHtext[delE+1:]
[cHtext1.append(x) for x in cHtext if not(x=="" or x=="\xa0")]

noDup = [] 
[noDup.append(x) for x in ctext if x not in noDup] 
for i in range(0, len(noDup)):
    if noDup[i] == '15-441':
        splitCs=i
    if noDup[i] == '36-225':
        splitMath = i

csCourse = noDup[:splitCs+1]
mathCourse = noDup[splitCs+1:splitMath+1]
scienceCourse = noDup[splitMath+1:-1]
humCourse = cHtext1

def writeLists(fileName, courseList, courseType):
    courseLists = open(fileName, "a")
    courseLists.write(courseType +"= [")
    for course in courseList:
        courseLists.write(course + ",")
    courseLists.write("]\n")

writeLists("course_list.txt", csCourse, "Core")
writeLists("course_list.txt", mathCourse, "Math")
writeLists("course_list.txt", scienceCourse, "Science")
writeLists("course_list.txt", humCourse, "Humanities")
