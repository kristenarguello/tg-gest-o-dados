CREATE TABLE Countries (
    name VARCHAR(255) PRIMARY KEY,
    ISO VARCHAR(3),
    region VARCHAR(255),
    income_group VARCHAR(255)
);
ALTER TABLE Countries ADD CONSTRAINT AK_ISO UNIQUE (ISO);

CREATE TABLE HealthData (
    country_name VARCHAR(255) PRIMARY KEY,
    life_expectancy FLOAT,
    prevelance_undernounishment FLOAT,
    health_expanditure FLOAT
);
ALTER TABLE HEALTHDATA ADD FOREIGN KEY (country_name) REFERENCES Countries (name);

CREATE TABLE FinancialData (
    country_name VARCHAR(255) PRIMARY KEY,
    unemployment FLOAT,
    corruption FLOAT,
    communicable FLOAT,
    noncommunicable FLOAT
);
ALTER TABLE FinancialData ADD FOREIGN KEY (country_name) REFERENCES Countries (name);

CREATE TABLE EnvironmentData (
    country_name VARCHAR(255) PRIMARY KEY,
    co2_emissions FLOAT,
    sanitation FLOAT,
    injuries FLOAT
);
ALTER TABLE EnvironmentData ADD FOREIGN KEY (country_name) REFERENCES Countries (name);

CREATE TABLE EducationData (
    country_name VARCHAR(255) PRIMARY KEY,
    educational_expanditure FLOAT
);
ALTER TABLE EducationData ADD FOREIGN KEY (country_name) REFERENCES Countries (name);