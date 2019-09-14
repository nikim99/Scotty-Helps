import json 
import cmu_course_api
import pandas as pd 
import numpy as np

fce_raw = pd.read_csv("data/raw_fce.csv")
fce_raw = fce_raw.drop("Semester", axis = 1)
fce_raw = fce_raw.drop("College", axis = 1)
fce_raw = fce_raw.drop("Dept", axis = 1)
fce_raw = fce_raw.drop("Section", axis = 1)
fce_raw = fce_raw.drop("Name", axis = 1)
fce_raw = fce_raw.drop("Course Name", axis = 1)
fce_raw = fce_raw.drop("Level", axis = 1)
fce_raw = fce_raw.drop("Hrs Per Week 5", axis = 1)
fce_raw = fce_raw.drop("Hrs Per Week 8", axis = 1)
fce_raw = fce_raw.drop("Num Respondents", axis = 1)
fce_raw = fce_raw.drop("Response Rate %", axis = 1)
fce_raw = fce_raw.drop("Possible Respondents", axis = 1)
fce_raw = fce_raw.drop("Clearly explain course requirements", axis = 1)
fce_raw = fce_raw.drop("Clear learning objectives & goals", axis = 1)
fce_raw = fce_raw.drop("Demonstrate importance of subject matter", axis = 1)
fce_raw["Course"] = None
for i in range(len(fce_raw.index)):
    fce_raw["Course"][i] = fce_raw.loc[i, "Course ID"][:2] + "-" + \
        fce_raw.loc[i, "Course ID"][2:]
fce_raw = fce_raw.drop("Course ID", axis = 1)

fce_raw_2019 = (fce_raw[fce_raw.Year == 2019]).groupby("Course").agg({ \
    "Hrs Per Week":"median", "Interest in student learning":"median", \
        "Instructor provides feedback to students to improve":"median", \
        "Explains subject matter of course":"median", \
            "Show respect for all students":"median", \
            "Overall teaching rate": "median", "Overall course rate": "median"})
fce_raw_2019.columns = ["".join(x) for x in fce_raw_2019.columns.ravel()]

fce_raw.to_csv("data/modified_fce.csv")
fce_raw_2019.to_csv("data/fce2019.csv")