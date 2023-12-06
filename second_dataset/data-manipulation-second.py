import pandas

def create_insert_sql(table_name, columns, values):
    columns_str = ', '.join(columns)
    
    values_str = []
    for v in values:
        if isinstance(v, str):
            values_str.append(f"'{v}'")
        elif v == 'nan':
            values_str.append('NULL')
        elif v == None:
            values_str.append('NULL')
        else:
            values_str.append(str(v))
    
    values_str = ', '.join(values_str)
            
    # values_str = ', '.join([f'"{value}"' if isinstance(value, str) else str(value) for value in values])
  
    return f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str});\n"


# Read the data from the CSV file
data = pandas.read_csv('Global_Education.csv', encoding='latin-1')  

for index, row in data.iterrows():
    # if row["Year"] == 2019: # only data from 2019
        with open("countries_two.sql", "a") as countries_insert:
            countries_insert.write(create_insert_sql('Countries', ['name', 'latitude', 'longitude'], [row['Countries and areas'], row['Latitude '], row['Longitude']]))

        with open("healthanddemo.sql", "a") as health:
            health.write(create_insert_sql('HealthandDemographics', ['country_name','birth_rate', 'unemployment_rate', 'youthliteracy_rate_male', 'youthliteracy_rate_female'], [row['Countries and areas'], row['Birth_Rate'], row['Unemployment_Rate'], row['Youth_15_24_Literacy_Rate_Male'], row['Youth_15_24_Literacy_Rate_Female']]))
        # with open("health_inserts.sql", "a") as healthdata:
        #     healthdata.write(create_insert_sql('HealthData', ['country_name','life_expectancy', 'prevelance_undernourishment', 'health_expenditure'], [row['Country Name'], row['Life Expectancy World Bank'], row['Prevelance of Undernourishment'], row['Health Expenditure %']]))

        with open("educationlevel.sql", "a") as edlevel:
            edlevel.write(create_insert_sql("EducationLevel", ["country_name", "Pre0Primary_Age_Male", "Pre0Primary_Age_Female" ,"Primary_Age_Male","Primary_Age_Female" , "Lower_Secondary_Age_Male" , "Lower_Secondary_Age_Female" , "Upper_Secondary_Age_Male" , "Upper_Secondary_Age_Female" , "Completion_Rate_Primary_Male" ,"Completion_Rate_Primary_Female"  ], [row["Countries and areas"], row["OOSR_Pre0Primary_Age_Male"], row["OOSR_Pre0Primary_Age_Female"] , row["OOSR_Primary_Age_Male"], row["OOSR_Primary_Age_Female"] , row["OOSR_Lower_Secondary_Age_Male"] , row["OOSR_Lower_Secondary_Age_Female"] , row["OOSR_Upper_Secondary_Age_Male"] , row["OOSR_Upper_Secondary_Age_Female"] , row["Completion_Rate_Primary_Male"] ,row["Completion_Rate_Primary_Female"]  ]))
        # with open("env_inserts.sql", "a") as envdata:

        with open("enrollment.sql", "a") as enrollment:
            enrollment.write(create_insert_sql("Enrollment", ["country_name", "Primary_EduEnrollment", "Tertiary_EduEnrollment"], [row["Countries and areas"], row["Gross_Primary_Education_Enrollment"], row["Gross_Tertiary_Education_Enrollment"]]))
        #     envdata.write(create_insert_sql('EnvironmentData', ['country_name', 'co2_emissions', 'sanitation', 'injuries'], [row['Country Name'], row['CO2'], row['Sanitation'], row['Injuries']]))


        with open("educationproficiency.sql", "a") as edprof:
            edprof.write(create_insert_sql("EducationProficiency", ["country_name", "Grade_2_3_Reading", "Grade_2_3_Math", "Primary_End_Reading", "Primary_End_Math", "Lower_Secondary_End_Reading", "Lower_Secondary_End_Math"], [row["Countries and areas"], row["Grade_2_3_Proficiency_Reading"], row["Grade_2_3_Proficiency_Math"], row["Primary_End_Proficiency_Reading"], row["Primary_End_Proficiency_Math"], row["Lower_Secondary_End_Proficiency_Reading"], row["Lower_Secondary_End_Proficiency_Math"]]))
        # with open("financial_inserts.sql", "a") as financialdata:
        #     financialdata.write(create_insert_sql('FinancialData', ['country_name', 'unemployment', 'corruption', 'communicable', 'noncommunicable'], [row['Country Name'], row['Unemployment'], row['Corruption'], row['Communicable'], row['NonCommunicable']]))
        
        # with open("education_inserts.sql", "a") as educationdata:
        #     educationdata.write(create_insert_sql('EducationData', ['country_name', 'educational_expanditure'], [row['Country Name'], row['Education Expenditure %']]))
        
