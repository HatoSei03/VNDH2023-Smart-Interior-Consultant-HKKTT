DROP DATABASE IKEA;

CREATE DATABASE IKEA;

USE IKEA;

CREATE TABLE UserPrompt
(
	userPromptID int auto_increment, 
    prompt varchar(500),
    
	PRIMARY KEY(userPromptID)
);


CREATE TABLE IkeaItem
(
	ID int auto_increment,
    itemLink nvarchar(150),
    itemPrice float,
    
	PRIMARY KEY(ID)
);

-- drop table UserPrompt;
-- drop table IkeaItem;

select * from IkeaItem;
select * from UserPrompt;

-- select * from IkeaItem where ID > 1000;
-- LOAD DATA INFILE 'Downloads/IKEA.csv' INTO TABLE IkeaItem;