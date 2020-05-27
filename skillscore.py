# **************************************************************************************************************************
''' 
using with gives file closed problem. use a code to obtain skills from skills.csv without using with --- open --- as ---. 
use pandas from chrome
'''
#****************************************************************************************************************************


from pyresparser import ResumeParser
import pandas as pd
import spacy
import csv
import re

data = ResumeParser('SampleResume.pdf').get_extracted_data()
# data contains a dictionary

name = data['name']
skills = data['skills']
skill1 = str(skills)
skill = re.sub("[\']", '', skill1)
skill = skill.split(",")

#removing [
a = skill[0]
c = ""
for i in range(1,len(a)):
	c+=a[i]
skill[0] = c

#removing ]
a = skill[-1]
c = ""
for i in range(len(a)-1):
	c+=a[i]
skill[-1] = c

skill_list = []
skill_req = []

# converting all to lower case
for i in range(len(skill)):
	skill[i] = skill[i].lower()

for i in skill:
	skill_list.append(i.strip())

	
	
f = open("requirement.txt","r")
text = f.read()
text = text.split(",")

for i in range(len(text)):
	text[i] = text[i].lower()
for i in text:
	skill_req.append(i.strip())

score = 0
for s in skill_list:
	if s in skill_req:
		score = score + 1

print("Name: ",name)
print("score: ",score)
print("\nRequirements: ",skill_req)
print("\nSkills: ",skill_list)
