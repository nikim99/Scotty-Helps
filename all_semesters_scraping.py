import json 
import cmu_course_api
import pandas as pd 
import numpy as np

#SPRING
spring_df = pd.read_json("data/spring.json")
spring_df = spring_df.drop('coreqs_obj')
spring_df = spring_df.drop('prereqs_obj')
spring_df = spring_df.drop('sections')
spring_df = spring_df.transpose()
spring_df["profs"] = None
spring_df["School Level"] = None
for i in range(len(spring_df.lectures)):
    spring_df.profs[i] = spring_df["lectures"][i][0]["instructors"][0]
    if spring_df.prereqs[i] == None:
        spring_df.prereqs[i] = "None"
    if spring_df.coreqs[i] == None:
        spring_df.coreqs[i] = "None"
    if spring_df.index[i][3] <= '1':
        spring_df["School Level"][i] = "Freshman"
    elif spring_df.index[i][3] == '2':
        spring_df["School Level"][i] = "Sophomore"
    elif spring_df.index[i][3] == '3':
        spring_df["School Level"][i] = "Junior"
    elif spring_df.index[i][3] == '4' or spring_df.index[i][3] == 5:
        spring_df["School Level"][i] = "Senior"
    else:
        spring_df["School Level"][i] = "Graduate"
spring_df = spring_df.drop('lectures', axis = 1)
spring_df["Course"] = spring_df.index
spring_df = spring_df.reset_index()
spring_df = spring_df.drop("index", axis = 1)
spring_df.to_csv("data/spring.csv")

#FALL
fall_df = pd.read_json("data/fall.json")
fall_df = fall_df.drop('coreqs_obj')
fall_df = fall_df.drop('prereqs_obj')
fall_df = fall_df.drop('sections')
fall_df = fall_df.transpose()
fall_df["profs"] = None
fall_df["School Level"] = None
for i in range(len(fall_df.lectures)):
    fall_df.profs[i] = fall_df["lectures"][i][0]["instructors"][0]
    if fall_df.prereqs[i] == None:
        fall_df.prereqs[i] = "None"
    if fall_df.coreqs[i] == None:
        fall_df.coreqs[i] = "None"
    if fall_df.index[i][3] <= '1':
        fall_df["School Level"][i] = "Freshman"
    elif fall_df.index[i][3] == '2':
        fall_df["School Level"][i] = "Sophomore"
    elif fall_df.index[i][3] == '3':
        fall_df["School Level"][i] = "Junior"
    elif fall_df.index[i][3] == '4' or fall_df.index[i][3] == 5:
        fall_df["School Level"][i] = "Senior"
    else:
        fall_df["School Level"][i] = "Graduate"
fall_df = fall_df.drop('lectures', axis = 1)
fall_df["Course"] = fall_df.index
fall_df = fall_df.reset_index()
fall_df = fall_df.drop("index", axis = 1)
fall_df.to_csv("data/fall.csv")

#M1
m1_df = pd.read_json("data/m1.json")
m1_df = m1_df.drop('coreqs_obj')
m1_df = m1_df.drop('prereqs_obj')
m1_df = m1_df.drop('sections')
m1_df = m1_df.transpose()
m1_df["profs"] = None
m1_df["School Level"] = None
for i in range(len(m1_df.lectures)):
    m1_df.profs[i] = m1_df["lectures"][i][0]["instructors"][0]
    if m1_df.prereqs[i] == None:
        m1_df.prereqs[i] = "None"
    if m1_df.coreqs[i] == None:
         m1_df.coreqs[i] = "None"
    if m1_df.index[i][3] <= '1':
        m1_df["School Level"][i] = "Freshman"
    elif m1_df.index[i][3] == '2':
        m1_df["School Level"][i] = "Sophomore"
    elif m1_df.index[i][3] == '3':
        m1_df["School Level"][i] = "Junior"
    elif m1_df.index[i][3] == '4' or m1_df.index[i][3] == 5:
        m1_df["School Level"][i] = "Senior"
    else:
        m1_df["School Level"][i] = "Graduate"
m1_df = m1_df.drop('lectures', axis = 1)
m1_df["Course"] = m1_df.index
m1_df = m1_df.reset_index()
m1_df = m1_df.drop("index", axis = 1)
m1_df.to_csv("data/m1.csv")

#M2
m2_df = pd.read_json("data/m2.json")
m2_df = m2_df.drop('coreqs_obj')
m2_df = m2_df.drop('prereqs_obj')
m2_df = m2_df.drop('sections')
m2_df = m2_df.transpose()
m2_df["profs"] = None
m2_df["School Level"] = None
for i in range(len(m2_df.lectures)):
    m2_df.profs[i] = m2_df["lectures"][i][0]["instructors"][0]
    if m2_df.prereqs[i] == None:
        m2_df.prereqs[i] = "None"
    if m2_df.coreqs[i] == None:
        m2_df.coreqs[i] = "None"
    if m2_df.index[i][3] <= '1':
        m2_df["School Level"][i] = "Freshman"
    elif m2_df.index[i][3] == '2':
        m2_df["School Level"][i] = "Sophomore"
    elif m2_df.index[i][3] == '3':
        m2_df["School Level"][i] = "Junior"
    elif m2_df.index[i][3] == '4' or m2_df.index[i][3] == 5:
        m2_df["School Level"][i] = "Senior"
    else:
        m2_df["School Level"][i] = "Graduate"
m2_df = m2_df.drop('lectures', axis = 1)
m2_df["Course"] = m2_df.index
m2_df = m2_df.reset_index()
m2_df = m2_df.drop("index", axis = 1)
m2_df.to_csv("data/m2.csv")