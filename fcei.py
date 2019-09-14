import json 
import cmu_course_api
import pandas as pd 
import numpy as np

fce = pd.read_csv("data/modified_fce.csv")

fcei = fce.groupby(["Course", "Year"]).agg({"Hrs Per Week":"median", \
    "Interest in student learning":"median", \
        "Instructor provides feedback to students to improve":"median", \
        "Explains subject matter of course":"median", \
            "Show respect for all students":"median", \
            "Overall teaching rate": "median", "Overall course rate": "median"})
fcei.columns = ["".join(x) for x in fcei.columns.ravel()]
fcei = fcei.reset_index()

fcei.to_csv("data/individial_fce.csv")