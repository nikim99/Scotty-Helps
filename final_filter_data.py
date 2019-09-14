import json 
import cmu_course_api
import pandas as pd 
import numpy as np

fce = pd.read_csv("data/fce2019.csv")
spring = pd.read_csv("data/spring.csv")
spring_final = pd.merge(spring, fce, on = "Course", how = "left")
spring_final = spring_final.drop("Unnamed: 0", axis = 1)
spring_final.to_csv("data/spring_final.csv")

fall = pd.read_csv("data/fall.csv")
fall_final = pd.merge(fall, fce, on = "Course", how = "left")
fall_final = fall_final.drop("Unnamed: 0", axis = 1)
fall_final.to_csv("data/fall_final.csv")

m1 = pd.read_csv("data/m1.csv")
m1_final = pd.merge(m1, fce, on = "Course", how = "left")
m1_final = m1_final.drop("Unnamed: 0", axis = 1)
m1_final.to_csv("data/m1_final.csv")

m2 = pd.read_csv("data/m2.csv")
m2_final = pd.merge(m2, fce, on = "Course", how = "left")
m2_final = m2_final.drop("Unnamed: 0", axis = 1)
m2_final.to_csv("data/m2_final.csv")