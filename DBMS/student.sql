/*CREATE TABLE*/

CREATE TABLE Student_Details
(
RollNo CHAR(6) NOT NULL,
Name VARCHAR(100) NOT NULL,
Sex CHAR(1),
PhoneNo DECIMAL(10),
Email VARCHAR(100),
CGPA DECIMAL(10,2),
Degree_ID CHAR(3),
primary key(RollNo),
foreign key(Degree_ID) references Degree(Degree_ID)
on delete cascade on update cascade
);

/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'AE2#01','Abinash Sahoo','M',9176762508,'sahoositu@gmail.com',8.87,'AE2');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'AE2#02','Vaisakh Shankar','M',9791057573,'vaivaiiit@gmail.com',8.11,'AE2');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'AE2#03','Anandu Bhadran','M',9884684988,'itsananduambadi@gmail.com',8.25,'AE2');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'AE3#04','Rekkala Tirupathi Reddy','M',9840279559,'rtr182018@gmail.com',6.69,'AE3');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'AE3#05','Harsh Satiya','M',7092139900,'Harshsatiya@gmail.com',5.51,'AE3');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'AE3#06','J Jayasilan','M',9789896827,'jaisi307@gmail.com',6.17,'AE3');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'AE3#07','P Srinivas Ganesh','M',9908519301,'psganesh2906@gmail.com',9.54,'AE3');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'CH1#01','Keerthana.A','F',7598083695,'keerthana28395@gmail.com',9.28,'CH1');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'CH1#02','Konge Utkarsh Vasudev','M',9003291621,'utkarshkonge2@gmail.com',8.83,'CH1');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'CH1#03','Koppula Manoj Kumar','M',9884184813,'koppulamanoj9997@gmail.com',5.56,'CH1');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'CH1#04','Manneti Shyamprasad Reddy','M',9042539396,'mannetishyam@gmail.com',7.71,'CH1');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'CH1#05','Lanka Jaswanth','M',9940253744,'l.jassu24@gmail.com',6.29,'CH1');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'CH4#06','Arijit Jana','M',9092849960,'arijit1995jana@gmail.com',8.55,'CH4');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'CH4#07','Arshiya Kaur','F',9953554096,'arshiyakaur94@gmail.com',9.33,'CH4');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'CH4#08','Arunava Saha','F',9962750235,'arunavasaha45@gmail.com',9,'CH4');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'CH4#09','Hemkalyan Ballav','M',7044338670,'cy15c013@smail.iitm.ac.in',8.62,'CH4');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'CH4#10','Kanad Majumder','M',9051300237,'dbkanadmajumder@gmail.com',8.07,'CH4');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'CS1#01','Akshay B','M',9003277682,'mail.akshayb@gmail.com',8.17,'CS1');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'CS1#02','Aravind S','M',9962914141,'sathooriaravind@gmail.com',6.89,'CS1');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'CS1#03','Bekkam Venkata Aditya','M',9940134127,'adityabekkamab@gmail.com',7.11,'CS1');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'CS1#04','Preetham V R','M',9962106217,'vraikarpreetham@gmail.com',8.36,'CS1');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'CS1#05','K Ritwika','M',9940248660,'k.ritwika.reddy@gmail.com',8.99,'CS1');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'CS2#06','Meka Gayathri','F',9003163094,'gayathrimeka@gmail.com',8.59,'CS2');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'CS2#07','Punit Khanna','M',9092403970,'punitkhanna25@gmail.com',8.24,'CS2');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'CS2#08','J P Sagar','M',9962613421,'jpsagarm95@gmail.com',9.58,'CS2');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'CS3#09','Suthar Hardikkumar Manubhai','M',9923115505,'cs15m049@smail.iitm.ac.in',8.11,'CS3');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'CS3#10','Vinamr Goel','M',9971125482,'vinamrxgoel@gmail.com',6.67,'CS3');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'EE1#01','Mutnuru Sarath Kumar','M',8682908569,'sarathkumarmutnuru8@gmail.com',8.6,'EE1');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'EE1#02','Navin Adarsh G','M',9444475375,'adarshnavin@gmail.com',7.42,'EE1');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'EE1#03','Nithin Seyon Ramesan','M',9025088461,'nithinseyon@gmail.com',9.12,'EE1');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'EE1#04','Pendem Shravan','M',9003112733,'shravanbittu2013@gmail.com',8.13,'EE1');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'EE1#05','Pothumahanti Srikar','M',8106370909,'srikarrohit@gmail.com',7.75,'EE1');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'EE2#06','Maluchuru Sai Dinesh Reddy','M',9790956523,'maluchurudinesh@gmail.com',7.19,'EE2');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'EE2#07','Manish Kumar Maurya','M',9043814237,'manish16dec93@gmail.com',7.68,'EE2');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'EE2#08','Akshat Dave','M',8939565908,'adaveiitm@gmail.com',8.74,'EE2');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'EE2#09','Pulkit Agarwal','M',9043810290,'pulkitagarwal347@gmail.com',8.78,'EE2');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'EE2#10','Gadi Sunil','M',8056117720,'sunil.gadi71@gmail.com',7.33,'EE2');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'EE3#11','Shashank Anand','M',8144890059,'anand10692@gmail.com',7.42,'EE3');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'EE3#12','Debjyoti Kumar Mandal','M',9903048516,'danieltombay@gmail.com',7.11,'EE3');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'EE3#13','Gayathri S','F',8129465717,'gayathribalchandran@gmail.com',9.41,'EE3');
/* INSERT QUERY */INSERT INTO Student_Details(RollNo,Name,Sex,PhoneNo,Email,CGPA,Degree_ID) VALUES( 'EE3#14','Mittapalli Harshavardhan','M',9493042146,'harshamp1511@gmail.com',7.5,'EE3');
