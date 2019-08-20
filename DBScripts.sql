create table employee (
emp_no int not null,
emp_name char(100),
dept_id int ,
salary int,
constraint emp_no_pk primary key (emp_no),
constraint dept_id_fk foreign key (dept_id) references department (dept_id)
);


create table department (
dept_id int,
dept_name char(50) not null,
constraint dept_id_pk primary key (dept_id)
);

--select * from employee

insert into employee  
values(  
 100, 'Alex White', 10, 60000
);

insert into employee  
values(  
 101, 'James Hunter', 10, 65000
);

insert into employee  
values(  
 102, 'Olivia Ditcher', 10, 70000
);

insert into employee  
values(  
 103, 'Lisa Ray', 10, 40000
);

insert into employee  
values(  
 104, 'Naveen Mishra', 20, 50000
);

insert into employee  
values(  
 105, 'Kelly Evans', 30, 90000
);

insert into employee  
values(  
 106, 'Christine Fox', 40, 100000
);
commit;


--select * from employee


--select * from department;


insert into department
values(10, 'ACCOUNTING');


insert into department  
values(20, 'RESEARCH');

insert into department  
values(30, 'SALES');

insert into department  
values(40, 'OPERATIONS');

commit;

-- to get average salary department wise
select dept_id, AVG(salary) from employee
group by dept_id;


-- to get current date and time
select CURRENT_TIMESTAMP AS current_date_time;
