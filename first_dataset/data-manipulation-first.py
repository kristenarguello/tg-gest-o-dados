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
data = pandas.read_csv('life_expectancy.csv', encoding='latin-1')  

for index, row in data.iterrows():
    if row["Year"] == 2019: # only data from 2019

        with open("health_inserts.sql", "a") as healthdata:
            healthdata.write(create_insert_sql('HealthData', ['country_name','life_expectancy', 'prevelance_undernourishment', 'health_expenditure'], [row['Country Name'], row['Life Expectancy World Bank'], row['Prevelance of Undernourishment'], row['Health Expenditure %']]))

        with open("env_inserts.sql", "a") as envdata:
            envdata.write(create_insert_sql('EnvironmentData', ['country_name', 'co2_emissions', 'sanitation', 'injuries'], [row['Country Name'], row['CO2'], row['Sanitation'], row['Injuries']]))

        with open("financial_inserts.sql", "a") as financialdata:
            financialdata.write(create_insert_sql('FinancialData', ['country_name', 'unemployment', 'corruption', 'communicable', 'noncommunicable'], [row['Country Name'], row['Unemployment'], row['Corruption'], row['Communicable'], row['NonCommunicable']]))
        
        with open("education_inserts.sql", "a") as educationdata:
            educationdata.write(create_insert_sql('EducationData', ['country_name', 'educational_expanditure'], [row['Country Name'], row['Education Expenditure %']]))
        
