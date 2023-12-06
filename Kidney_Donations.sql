-- Create Kidney_Donations database
CREATE DATABASE IF NOT EXISTS Kidney_Donations;

USE Kidney_Donations;

-- Create Organ_Waitlist table
CREATE TABLE Organ_Waitlist (
    State VARCHAR(50),
    Kidney INT,
    Liver INT,
    Pancreas INT,
    Heart INT,
    Lung INT,
    Intestine INT,
    Abdominal_Wall INT,
    VCA_Head_and_Neck INT,
    VCA_Upper_Limb INT,
    VCA_Uterus INT
);

SELECT * FROM Organ_Waitlist;

-- Create Kidney_Waitlist table
CREATE TABLE Kidney_Waitlist (
    State VARCHAR(50),
    Duration VARCHAR(50),
    `< 30 Days` INT,
    `30 to < 90 Days` INT,
    `90 Days to < 6 Months` INT,
    `6 Months to < 1 Year` INT,
    `1 Year to < 2 Years` INT,
    `2 Years to < 3 Years` INT,
    `3 Years to < 5 Years` INT,
    `5 or More Years` INT
);

SELECT * FROM Kidney_Waitlist;

-- Create Kidney_Waitlist_Addition table
CREATE TABLE Kidney_Waitlist_Addition (
    State VARCHAR(50),
    `2023` INT,
    `2022` INT,
    `2021` INT,
    `2020` INT,
    `2019` INT,
    `2018` INT,
    `2017` INT,
    `2016` INT,
    `2015` INT,
    `2014` INT,
    `2013` INT,
    `2012` INT,
    `2011` INT,
    `2010` INT,
    `2009` INT,
    `2008` INT,
    `2007` INT,
    `2006` INT,
    `2005` INT,
    `2004` INT,
    `2003` INT,
    `2002` INT,
    `2001` INT,
    `2000` INT,
    `1999` INT,
    `1998` INT,
    `1997` INT,
    `1996` INT,
    `1995` INT,
    `1994` INT,
    `1993` INT,
    `1992` INT,
    `1991` INT,
    `1990` INT,
    `1989` INT,
    `1988` INT
);

-- Verifying data successfully imported into Kidney_Waitlist table
SELECT * FROM Kidney_Waitlist;

-- Verifying data successfully imported into Kidney_Waitlist_Addition table
SELECT * FROM Kidney_Waitlist_Addition;

DELETE FROM Kidney_Waitlist_Addition WHERE State='States';

-- Create Kidney_Transplants table
CREATE TABLE Kidney_Transplants (
    States VARCHAR(255),
    `2023` INT,
    `2022` INT,
    `2021` INT,
    `2020` INT,
    `2019` INT,
    `2018` INT,
    `2017` INT,
    `2016` INT,
    `2015` INT,
    `2014` INT,
    `2013` INT,
    `2012` INT,
    `2011` INT,
    `2010` INT,
    `2009` INT,
    `2008` INT,
    `2007` INT,
    `2006` INT,
    `2005` INT,
    `2004` INT,
    `2003` INT,
    `2002` INT,
    `2001` INT,
    `2000` INT,
    `1999` INT,
    `1998` INT,
    `1997` INT,
    `1996` INT,
    `1995` INT,
    `1994` INT,
    `1993` INT,
    `1992` INT,
    `1991` INT,
    `1990` INT,
    `1989` INT,
    `1988` INT
);

-- Verifying data has successfully been imported
SELECT * FROM Kidney_Transplants;

DELETE FROM Kidney_Transplants WHERE States='States';

-- Create Kidney_Donor_Living table
CREATE TABLE Kidney_Donor_Living (
    States VARCHAR(255),
    `2023` INT,
    `2022` INT,
    `2021` INT,
    `2020` INT,
    `2019` INT,
    `2018` INT,
    `2017` INT,
    `2016` INT,
    `2015` INT,
    `2014` INT,
    `2013` INT,
    `2012` INT,
    `2011` INT,
    `2010` INT,
    `2009` INT,
    `2008` INT,
    `2007` INT,
    `2006` INT,
    `2005` INT,
    `2004` INT,
    `2003` INT,
    `2002` INT,
    `2001` INT,
    `2000` INT,
    `1999` INT,
    `1998` INT,
    `1997` INT,
    `1996` INT,
    `1995` INT,
    `1994` INT,
    `1993` INT,
    `1992` INT,
    `1991` INT,
    `1990` INT,
    `1989` INT,
    `1988` INT
);

-- Verifying data has successfully been imported
SELECT * FROM Kidney_Donor_Living;

DELETE FROM Kidney_Donor_Living WHERE States='States';

-- Create Kidney_Donor_Deceased table
CREATE TABLE Kidney_Donor_Deceased (
    States VARCHAR(255),
    `2023` INT,
    `2022` INT,
    `2021` INT,
    `2020` INT,
    `2019` INT,
    `2018` INT,
    `2017` INT,
    `2016` INT,
    `2015` INT,
    `2014` INT,
    `2013` INT,
    `2012` INT,
    `2011` INT,
    `2010` INT,
    `2009` INT,
    `2008` INT,
    `2007` INT,
    `2006` INT,
    `2005` INT,
    `2004` INT,
    `2003` INT,
    `2002` INT,
    `2001` INT,
    `2000` INT,
    `1999` INT,
    `1998` INT,
    `1997` INT,
    `1996` INT,
    `1995` INT,
    `1994` INT,
    `1993` INT,
    `1992` INT,
    `1991` INT,
    `1990` INT,
    `1989` INT,
    `1988` INT
);

-- Verifying data has successfully been imported
SELECT * FROM Kidney_Donor_Deceased;

-- Create Kidney_Transplant_Repeat
CREATE TABLE Kidney_Transplant_Repeat (
    States VARCHAR(255),
    Diabetes_Status VARCHAR(255),
    Transplant_Type VARCHAR(255),
    `2023` INT,
    `2022` INT,
    `2021` INT,
    `2020` INT,
    `2019` INT,
    `2018` INT,
    `2017` INT,
    `2016` INT,
    `2015` INT,
    `2014` INT,
    `2013` INT,
    `2012` INT,
    `2011` INT,
    `2010` INT,
    `2009` INT,
    `2008` INT,
    `2007` INT,
    `2006` INT,
    `2005` INT,
    `2004` INT,
    `2003` INT,
    `2002` INT,
    `2001` INT,
    `2000` INT,
    `1999` INT,
    `1998` INT,
    `1997` INT,
    `1996` INT,
    `1995` INT,
    `1994` INT,
    `1993` INT,
    `1992` INT,
    `1991` INT,
    `1990` INT,
    `1989` INT,
    `1988` INT
);

-- Verifying data successfully imported to Kidney_Transplant_Repeat
SELECT * FROM Kidney_Transplant_Repeat;

-- Create Kidney_Donor_Relation_to_Recipient table
CREATE TABLE Kidney_Donor_Relation_to_Recipient (
    States VARCHAR(255),
    Diabetes_Status VARCHAR(255),
    Donor_Relation_Type VARCHAR(255),
    `2023` INT,
    `2022` INT,
    `2021` INT,
    `2020` INT,
    `2019` INT,
    `2018` INT,
    `2017` INT,
    `2016` INT,
    `2015` INT,
    `2014` INT,
    `2013` INT,
    `2012` INT,
    `2011` INT,
    `2010` INT,
    `2009` INT,
    `2008` INT,
    `2007` INT,
    `2006` INT,
    `2005` INT,
    `2004` INT,
    `2003` INT,
    `2002` INT,
    `2001` INT,
    `2000` INT,
    `1999` INT,
    `1998` INT,
    `1997` INT,
    `1996` INT,
    `1995` INT,
    `1994` INT,
    `1993` INT,
    `1992` INT,
    `1991` INT,
    `1990` INT,
    `1989` INT,
    `1988` INT
);

-- Verifying data successfully imported to Kidney_Donor_Relation_to_Recipient
SELECT * FROM Kidney_Donor_Relation_to_Recipient;

-- Create Kidney_Donor_Age table
CREATE TABLE Kidney_Donor_Age (
    Age_Group VARCHAR(255),
    `2023` INT,
    `2022` INT,
    `2021` INT,
    `2020` INT,
    `2019` INT,
    `2018` INT,
    `2017` INT,
    `2016` INT,
    `2015` INT,
    `2014` INT,
    `2013` INT,
    `2012` INT,
    `2011` INT,
    `2010` INT,
    `2009` INT,
    `2008` INT,
    `2007` INT,
    `2006` INT,
    `2005` INT,
    `2004` INT,
    `2003` INT,
    `2002` INT,
    `2001` INT,
    `2000` INT,
    `1999` INT,
    `1998` INT,
    `1997` INT,
    `1996` INT,
    `1995` INT,
    `1994` INT,
    `1993` INT,
    `1992` INT,
    `1991` INT,
    `1990` INT,
    `1989` INT,
    `1988` INT
);

-- Verifying data successfully imported to Kidney_Donor_Age
SELECT * FROM Kidney_Donor_Age;

DELETE FROM Kidney_Donor_Age WHERE Age_Group='Age Group';

-- Create Kidney_Recipient_Age table
CREATE TABLE Kidney_Recipient_Age (
    Age_Group VARCHAR(255),
    `2023` INT,
    `2022` INT,
    `2021` INT,
    `2020` INT,
    `2019` INT,
    `2018` INT,
    `2017` INT,
    `2016` INT,
    `2015` INT,
    `2014` INT,
    `2013` INT,
    `2012` INT,
    `2011` INT,
    `2010` INT,
    `2009` INT,
    `2008` INT,
    `2007` INT,
    `2006` INT,
    `2005` INT,
    `2004` INT,
    `2003` INT,
    `2002` INT,
    `2001` INT,
    `2000` INT,
    `1999` INT,
    `1998` INT,
    `1997` INT,
    `1996` INT,
    `1995` INT,
    `1994` INT,
    `1993` INT,
    `1992` INT,
    `1991` INT,
    `1990` INT,
    `1989` INT,
    `1988` INT
);

-- Verifying data successfully imported to Kidney_Recipient_Age
SELECT * FROM Kidney_Recipient_Age;

-- Create Recipient_Diabetes_Status table
CREATE TABLE Recipient_Diabetes_Status (
    States VARCHAR(255),
    Diabetes_Status VARCHAR(255),
    `2023` INT,
    `2022` INT,
    `2021` INT,
    `2020` INT,
    `2019` INT,
    `2018` INT,
    `2017` INT,
    `2016` INT,
    `2015` INT,
    `2014` INT,
    `2013` INT,
    `2012` INT,
    `2011` INT,
    `2010` INT,
    `2009` INT,
    `2008` INT,
    `2007` INT,
    `2006` INT,
    `2005` INT,
    `2004` INT,
    `2003` INT,
    `2002` INT,
    `2001` INT,
    `2000` INT,
    `1999` INT,
    `1998` INT,
    `1997` INT,
    `1996` INT,
    `1995` INT,
    `1994` INT,
    `1993` INT,
    `1992` INT,
    `1991` INT,
    `1990` INT,
    `1989` INT,
    `1988` INT
);

-- Verifying data successfully imported to Recipient_Diabetes_Status
SELECT * FROM Recipient_Diabetes_Status;

-- Creating Kidney_Donor_Gender
CREATE TABLE Kidney_Donor_Gender (
    Gender VARCHAR(10),
    `2023` INT,
    `2022` INT,
    `2021` INT,
    `2020` INT,
    `2019` INT,
    `2018` INT,
    `2017` INT,
    `2016` INT,
    `2015` INT,
    `2014` INT,
    `2013` INT,
    `2012` INT,
    `2011` INT,
    `2010` INT,
    `2009` INT,
    `2008` INT,
    `2007` INT,
    `2006` INT,
    `2005` INT,
    `2004` INT,
    `2003` INT,
    `2002` INT,
    `2001` INT,
    `2000` INT,
    `1999` INT,
    `1998` INT,
    `1997` INT,
    `1996` INT,
    `1995` INT,
    `1994` INT,
    `1993` INT,
    `1992` INT,
    `1991` INT,
    `1990` INT,
    `1989` INT,
    `1988` INT
    );
    
SELECT * FROM Kidney_Donor_Gender;

DELETE FROM Kidney_Donor_Gender WHERE Gender='Gender';

-- Total Kidney Transplants Over the Years
SELECT
    SUM(`2023` + `2022` + `2021` + `2020` + `2019` + `2018` + `2017` + `2016` + `2015` + `2014` + `2013` + `2012` + `2011` + `2010` + `2009` + `2008` + `2007` + `2006` + `2005` + `2004` + `2003` + `2002` + `2001` + `2000` + `1999` + `1998` + `1997` + `1996` + `1995` + `1994` + `1993` + `1992` + `1991` + `1990` + `1989` + `1988`) AS Total_Transplants
FROM Kidney_Transplants;

-- Average Number of Kidney Transplants per Year
SELECT
    AVG(`2023` + `2022` + `2021` + `2020` + `2019` + `2018` + `2017` + `2016` + `2015` + `2014` + `2013` + `2012` + `2011` + `2010` + `2009` + `2008` + `2007` + `2006` + `2005` + `2004` + `2003` + `2002` + `2001` + `2000` + `1999` + `1998` + `1997` + `1996` + `1995` + `1994` + `1993` + `1992` + `1991` + `1990` + `1989` + `1988`) AS Avg_Transplants_Per_Year
FROM Kidney_Transplants;

-- Number of Kidney Transplants in 2022 by State
SELECT States, `2022` AS Transplants_2022
FROM Kidney_Transplants
ORDER BY Transplants_2022 DESC;

-- Distribution of Donor Status Types
SELECT
    Year,
    Deceased_Donor / All_Donor_Types * 100 AS Deceased_Donor_Percentage,
    Living_Donor / All_Donor_Types * 100 AS Living_Donor_Percentage
FROM Kidney_Donor_Status;

-- Top 5 States with the Highest Number of Repeat Kidney Transplants in 2023
SELECT States, `2023` AS Repeat_Transplants
FROM Kidney_Transplant_Repeat
ORDER BY Repeat_Transplants DESC
LIMIT 5;

-- Distribution of Recipient Diabetes Status in 2023
SELECT
    States,
    Diabetes_Status,
    SUM(`2023`) / SUM(`2023`) OVER (PARTITION BY States) * 100 AS Diabetes_Status_Percentage
FROM Recipient_Diabetes_Status
GROUP BY States, Diabetes_Status, `2023`
ORDER BY Diabetes_Status DESC;

-- Average Waiting Time for Kidney Transplants by State
SELECT
    State,
    AVG(`< 30 Days` + `30 to < 90 Days` + `90 Days to < 6 Months` + `6 Months to < 1 Year` + `1 Year to < 2 Years` + `2 Years to < 3 Years` + `3 Years to < 5 Years` + `5 or More Years`) AS Avg_Waiting_Time
FROM Kidney_Waitlist
GROUP BY State
ORDER BY Avg_Waiting_Time DESC
LIMIT 0, 50000;

-- Growth Rate of Kidney Transplants Over the Years
SELECT
    t.States,
    MAX(t.`2023`) / MIN(t.`1988`) AS Growth_Rate
FROM Kidney_Transplants t
GROUP BY t.States
ORDER BY Growth_Rate DESC;

-- States with the Longest Average Waiting Time for Kidney Transplants
WITH WaitlistDuration AS (
    SELECT
        State,
        AVG(
            `1 Year to < 2 Years` * 1 +
            `2 Years to < 3 Years` * 2 +
            `3 Years to < 5 Years` * 3 +
            `5 or More Years` * 5
        ) AS Avg_Waiting_Duration
    FROM Kidney_Waitlist
    GROUP BY State
)

SELECT
    w.State,
    w.Avg_Waiting_Duration
FROM WaitlistDuration w
ORDER BY Avg_Waiting_Duration DESC;

-- Age Group with the Highest Average Number of Kidney Donors
SELECT
    a.Age_Group,
    AVG(`2023` + `2022` + `2021` + `2020` + `2019` + `2018` + `2017` + `2016` + `2015` + `2014` + `2013` + `2012` + `2011` + `2010` + `2009` + `2008` + `2007` + `2006` + `2005` + `2004` + `2003` + `2002` + `2001` + `2000` + `1999` + `1998` + `1997` + `1996` + `1995` + `1994` + `1993` + `1992` + `1991` + `1990` + `1989` + `1988`) AS Avg_Donors
FROM Kidney_Donor_Age a
GROUP BY a.Age_Group
ORDER BY Avg_Donors DESC
LIMIT 1;

-- Year with the Maximum Increase in Kidney Transplants
SELECT
    t.States,
    MAX(t.`2023` - t.`1988`) AS Max_Increase
FROM Kidney_Transplants t
GROUP BY t.States
ORDER BY Max_Increase DESC;

-- States with a Significant Increase in Living Donor Transplants from 2010 to 2023
SELECT
    t.States,
    (t.`2023` - t.`2010`) AS Increase_Living_Donor_Transplants
FROM Kidney_Transplants t
WHERE (t.`2023` - t.`2010`) > 0
ORDER BY Increase_Living_Donor_Transplants DESC;
