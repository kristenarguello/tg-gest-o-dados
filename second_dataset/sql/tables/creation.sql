CREATE TABLE Countries (
    name VARCHAR(255) PRIMARY KEY,
    latitude FLOAT,
    longitude FLOAT
);
ALTER TABLE Countries ADD CONSTRAINT AK_geo_location UNIQUE (latitude, longitude);



CREATE TABLE HealthAndDemography (
    country_name VARCHAR(255) PRIMARY KEY, 
    birth_rate FLOAT, 
    unemployment_rate FLOAT,
    youthliteracy_rate_male INTEGER, 
    youthliteracy_rate_female INTEGER
);
ALTER TABLE HealthAndDemography ADD FOREIGN KEY (country_name) REFERENCES Countries (name);


CREATE TABLE EducationLevel (
    country_name VARCHAR(255) PRIMARY KEY,
    Pre0Primary_Age_Male INTEGER,
    Pre0Primary_Age_Female INTEGER,
    Primary_Age_Male INTEGER,
    Primary_Age_Female INTEGER,
    Lower_Secondary_Age_Male INTEGER,
    Lower_Secondary_Age_Female INTEGER,
    Upper_Secondary_Age_Male INTEGER,
    Upper_Secondary_Age_Female INTEGER,
    Completion_Rate_Primary_Male INTEGER,
    Completion_Rate_Primary_Female INTEGER
); 
ALTER TABLE EducationLevel ADD FOREIGN KEY (country_name) REFERENCES Countries (name);


CREATE TABLE  EducationProficiency (
    country_name VARCHAR(255) PRIMARY KEY,
    Grade_2_3_Reading INTEGER,
    Grade_2_3_Math INTEGER,
    Primary_End_Reading INTEGER,
    Primary_End_Math INTEGER,
    Lower_Secondary_End_Reading INTEGER,
    Lower_Secondary_End_Math INTEGER
);
ALTER TABLE EducationProficiency ADD FOREIGN KEY (country_name) REFERENCES Countries (name);


CREATE TABLE Enrollment (
    country_name VARCHAR(255) PRIMARY KEY,
    Primary_EduEnrollment FLOAT,
    Tertiary_EduEnrollment FLOAT
);
ALTER TABLE Enrollment ADD FOREIGN KEY (country_name) REFERENCES Countries (name);
