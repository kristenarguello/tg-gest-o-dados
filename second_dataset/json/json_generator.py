import pandas
import json

# Raad the data from the CSV file
data = pandas.read_csv('Global_Education.csv', encoding='latin-1') 

jsons = []
for index, row in data.iterrows():
    j = {
        "country_name": row['Countries and areas'],
        "latitude": row['Latitude '],
        "longitude": row['Longitude'],
        "healthanddemography": {
            "birth_rate": row['Birth_Rate'],
            "unemployment_rate": row['Unemployment_Rate'],
            "youth_15_24_literacy_rate_male": row['Youth_15_24_Literacy_Rate_Male'],
            "youth_15_24_literacy_rate_female": row['Youth_15_24_Literacy_Rate_Female']
        }, 
        "educationlevel": {
            "OOSR_Pre0Primary_Age_Male": row["OOSR_Pre0Primary_Age_Male"],
            "OOSR_Pre0Primary_Age_Female": row["OOSR_Pre0Primary_Age_Female"],
            "OOSR_Primary_Age_Male": row["OOSR_Primary_Age_Male"],
            "OOSR_Primary_Age_Female": row["OOSR_Primary_Age_Female"],
            "OOSR_Lower_Secondary_Age_Male": row["OOSR_Lower_Secondary_Age_Male"],
            "OOSR_Lower_Secondary_Age_Female": row["OOSR_Lower_Secondary_Age_Female"],
            "OOSR_Upper_Secondary_Age_Male": row["OOSR_Upper_Secondary_Age_Male"],
            "OOSR_Upper_Secondary_Age_Female": row["OOSR_Upper_Secondary_Age_Female"],
            "Completion_Rate_Primary_Male": row["Completion_Rate_Primary_Male"],
            "Completion_Rate_Primary_Female": row["Completion_Rate_Primary_Female"] 
        },
        "educationproficiency": {
            "Grade_2_3_Proficiency_Reading": row["Grade_2_3_Proficiency_Reading"],
            "Grade_2_3_Proficiency_Math": row["Grade_2_3_Proficiency_Math"],
            "Primary_End_Proficiency_Reading": row["Primary_End_Proficiency_Reading"],
            "Primary_End_Proficiency_Math": row["Primary_End_Proficiency_Math"],
            "Lower_Secondary_End_Proficiency_Reading": row["Lower_Secondary_End_Proficiency_Reading"],
            "Lower_Secondary_End_Proficiency_Math": row["Lower_Secondary_End_Proficiency_Math"]
        },
        "enrollment": {
            "Gross_Primary_Education_Enrollment": row["Gross_Primary_Education_Enrollment"],
            "Gross_Tertiary_Education_Enrollment": row["Gross_Tertiary_Education_Enrollment"]
        }
    }
    jsons.append(j)

result = json.dumps(jsons, indent=4)
with open("data.json", "w") as f:
    f.write(result)
