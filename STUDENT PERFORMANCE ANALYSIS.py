import pandas as pd
#Student data
data={
    "Student_ID":[101,102,103,104,105,106,107,108,109,110],
    "Name":["Anandi","Kirti","Ritika","Sanjana","Mayuri","Aryan","Yash","Vansh","Aadi","Ayush"],
    "Maths":[78,92,65,88,56,74,81,95,69,85],
    "Science":[82,89,70,91,60,78,85,93,72,88],
    "English":[75,94,68,86,62,80,79,96,70,90],
    "Attendance":[85,95,72,90,65,88,92,98,75,94]
}
#Create DataFrame
df=pd.DataFrame(data)

#calculate Total Marks
df["Total"]=df["Maths"]+df["Science"]+df["English"]

#Calculate Percentage
df["Percentage"]=df["Total"]/3

#Assign Grade
def get_grades(percentage):
    if percentage>=90:
        return "A+"
    elif percentage>=80:
        return "A"
    elif percentage>=70:
        return "B"
    elif percentage>=60:
        return "C"
    else:
        return "D"
df["Grade"]=df["Percentage"].apply(get_grades)

#Pass/Fail
df["Result"]=df["Percentage"].apply(lambda x:"Pass" if x>40 else "Fail")

#display data
print("---------------STUDENT PERFORMANCE----------------")
print(df)

#Basic Analysis
print("\nAverage Percentage:")
print(round(df["Percentage"].mean(),2))

print("\nHighest Percentage:")
print(round(df["Percentage"].max(),2))

print("\nLowest Percentage:")
print(round(df["Percentage"].min(),2))

print("\nAverage Attendance:")
print(round(df["Attendance"].mean(),2))

#Save data for Power BI
df.to_csv("Student_Performance.csv",index=False)

print("\nCSV FILE SUCCESSFULLY CREATED")
print("FILE NAME:Student_Performance.csv")