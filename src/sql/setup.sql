drop TABLE IF exists associate_portfolio;
drop TABLE IF exists associate_portfolio;
drop TABLE IF exists associate;
drop table if exists employee;


create table associate(
    salesforceId varchar(10) primary key not null, 
    firstname varchar(20) not null,
    lastname varchar(20) not null,
    email varchar(40),
    pswrd varchar(40)
);

create table associate_portfolio(
    bio text,
    favorite_technologies text,
    preference varchar(15),
    salesforceId varchar(10) not null,
    foreign key (salesforceId)
    references associate(salesforceId)

);

create table employee (
    salesforceId varchar(10) primary key not null, 
    firstname varchar(20) not null,
    lastname varchar(20) not null,
    email varchar(40),
    pswrd varchar(40)
);

create table employee_portfolio(
    bio text,
    technology text,
    trainer_location varchar(25),
    salesforceId varchar(10) not null,
    foreign key (salesforceId)
    references associate(salesforceId)
    
);
