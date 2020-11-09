DROP TABLE IF EXISTS records;

CREATE TABLE records (
    first_name STRING NOT NULL,
    last_name STRING NOT NULL,
    pregnancies FLOAT NOT NULL,
    glucose FLOAT NOT NULL,
    blood_pressure FLOAT NOT NULL,
    skin_thickness FLOAT NOT NULL,
    insulin FLOAT NOT NULL,
    bmi FLOAT NOT NULL,
    diabetes_pedigree FLOAT NOT NULL,
    age FLOAT NOT NULL,
    outcome FLOAT NOT NULL
)