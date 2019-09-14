import json 
import cmu_course_api
import pandas as pd 
import numpy as np

def get_new_table(dept, unitRange, year, sem, courseType = None):
    fileDict = {"Spring": "data/spring_final.csv", "Fall": "data/fall_final.csv", \
        "Summer 1": "data/m1_final.csv", "Summer 2": "data/m2_final.csv"}
    opDict = {"Core": ["15-128","15-122","15-112","15-150","15-151","15-210","15-213","15-251",\
        "15-451","15-221","15-354","15-355","15-453","15-455","15-456","21-301","21-484","02-450",\
            "05-391","05-431","05-433","10-601","11-411","15-313","15-322", "15-323","15-381",\
                "15-415","15-462","16-384","16-385","15-312","15-317","15-414","15-424","21-300",\
                    "80-310","80-311","15-410","15-411","15-418","15-440","15-441"], \
        "Science": ["21-120","21-122","21-241","21-242","21-341","15-359","21-325",\
            "36-217","36-225"], "Math": ["02-261","03-124","09-101","09-221","15-321"\
                ,"27-100","33-104","42-203","85-310","02-223","02-250"], \
        "Humanities": ["76-101","70-311","80-130","80-150","80-180","80-221","80-241",\
            "80-242","80-270","80-271","80-275","80-281","80-330","85-102","85-211",\
                "85-221","85-241","85-251","85-261","88-120","88-260","19-101","36-303"\
                    ,"70-332","73-100","73-102","73-103","73-230","73-240","79-299"\
                        ,"79-300","79-320","79-331","80-135","80-136","80-243","80-244",\
                "80-245","80-324","80-334","80-341","84-104","84-275","84-310","84-320",\
                    "84-322","84-324","84-326","84-362","84-380","84-402","84-414",\
                        "88-220","88-257","57-173","60-205","70-342","76-221","76-227"\
            ,"76-232","76-239","76-241","79-104","79-201","79-202","79-207","79-222",\
                "79-223","79-226","79-229","79-230","79-240","79-241","79-242","79-255"\
            ,"79-262","79-265","79-282","79-311","79-316","79-345","79-350"]}
    
    df = pd.read_csv(fileDict[sem])
    if year == "Undergraduate":
        df = df[df["School Level"] != "Graduate"]
    else:
        df = df[df["School Level"] == year]
    df = df[df.department == dept]
    if "SCS" in dept and courseType != None:
        df = df[df.Course.isin(opDict[courseType])]
    num = int(unitRange[:unitRange.find("-")])
    df = df[(df.units >= num) & (df.units <= num + 4)]
    df["sumSeries"] = None
    df["Hrs Per Week"] = df["Hrs Per Week"].fillna(9)
    df = df.fillna(3)
    df.sumSeries = -df["Hrs Per Week"] + df["Overall teaching rate"] + \
        df["Overall course rate"] + df["Interest in student learning"] + \
            df["Explains subject matter of course"] + df["Show respect for all students"] + \
              df["Instructor provides feedback to students to improve"]  
    df = df[["Course", "name", "units", "profs", "Overall course rate", "sumSeries"]]
    df = df.reset_index()
    df = df.sort_values("sumSeries", ascending = False)
    df = df.drop("index", axis = 1)
    df = df.drop("sumSeries", axis = 1)
    df = df.reset_index()
    df = df.drop("index", axis = 1)
    df.to_csv("static/queried.csv")
