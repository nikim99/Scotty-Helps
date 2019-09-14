import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
#%matplotlib inline

def makeGraphsl(course, y):
    fullTable = pd.read_csv("data/individual_fce.csv")
    courseTable = fullTable[fullTable.Course==course]
    courseTable["Year"] = courseTable["Year"].astype(int)
    courseTable = courseTable.groupby(["Year"]).first()
    courseTable.columns = ["".join(x) for x in courseTable.columns.ravel()]
    courseTable = courseTable.dropna()
    courseTable = courseTable.reset_index()
    # data
    df=pd.DataFrame({'x': courseTable['Year'], 'y': courseTable[y] })
 
    # plot
    plt.plot( 'x', 'y', data=df, linestyle='-', marker='o')
    plt.ylabel(y)
    plt.xlabel("Year")
    y = y.split(" ")
    y = "_".join(y)
    fig = plt.savefig("static/" + y +'_plot.png')
    plt.close(fig)

def makeGraph(course):
    fullTable = pd.read_csv("data/individual_fce.csv")
    courseTable = fullTable[fullTable.Course==course]
    courseTable["Year"] = courseTable["Year"].astype(int)
    courseTable = courseTable.groupby(["Year"]).first()
    courseTable.columns = ["".join(x) for x in courseTable.columns.ravel()]
    courseTable = courseTable.dropna()
    courseTable=courseTable.loc[[2019], ['Interest in student learning', \
        'Instructor provides feedback to students to improve', \
            'Explains subject matter of course']]
    courseTable = courseTable.transpose()
    courseTable = courseTable.reset_index()
    courseTable = courseTable.rename(columns={"index":"category",2019:"rating"})
    sns.set(font_scale=0.5)
    plot = sns.barplot(x='rating',y='category', data=courseTable)
    plot.set_yticklabels(labels = {"Student Learning", "Feedback", "Explanations"}, rotation=45)
    figure = plot.get_figure()    
    figure.savefig('static/Course_plot.png', dpi=600)
    plt.close(figure)
    makeGraphsl(course, "Overall teaching rate")
    makeGraphsl(course, "Overall course rate")
    makeGraphsl(course, "Hrs Per Week")

