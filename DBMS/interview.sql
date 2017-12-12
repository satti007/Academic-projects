/* CREATE TABLE */
CREATE TABLE Interview
(
	RollNo CHAR(6),
	Org_ID INT(3),
	Org_profile_ID DECIMAL(1),
	Date VARCHAR(100),
	Time VARCHAR(100),
	Place VARCHAR(100),
	Outcome VARCHAR(100),
	primary key(RollNo,Org_ID,Org_profile_ID),
	foreign key(Org_ID) references Company(Org_ID)
	on delete cascade on update cascade,
	foreign key(Org_ID,Org_profile_ID) references Profile(Org_ID,Org_profile_ID)
	on delete cascade on update cascade
);

/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'AE2#01',108,1,'03/12/16','14:00:00','HSB','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'AE2#01',108,2,'03/12/16','15:00:00','HSB','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'AE2#02',105,1,'04/12/16','14:00:00','HSB','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'AE2#02',106,2,'03/12/16','12:00:00','CRC','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'AE2#02',108,1,'01/12/16','14:00:00','HSB','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'AE2#03',105,1,'04/12/16','14:00:00','HSB','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'AE2#03',106,1,'01/12/16','11:00:00','CRC','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'AE2#03',108,1,'01/12/16','14:00:00','HSB','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'AE3#04',108,1,'02/12/16','14:00:00','HSB','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'AE3#05',108,1,'03/12/16','14:00:00','HSB','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'AE3#06',108,1,'02/12/16','14:00:00','HSB','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'AE3#07',108,2,'02/12/16','15:00:00','HSB','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'AE3#07',108,1,'03/12/16','14:00:00','HSB','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CH1#01',101,1,'03/12/16','10:00:00','PO','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CH1#01',103,1,'04/12/16','12:00:00','HSB','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CH1#01',105,1,'04/12/16','14:00:00','HSB','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CH1#02',101,1,'03/12/16','10:00:00','PO','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CH1#02',103,1,'04/12/16','12:00:00','HSB','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CH1#02',105,1,'04/12/16','14:00:00','HSB','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CH1#03',103,1,'01/12/16','12:00:00','HSB','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CH1#03',106,1,'01/12/16','11:00:00','CRC','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CH1#04',101,1,'01/12/16','10:00:00','PO','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CH1#04',106,1,'02/12/16','11:00:00','CRC','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CH1#05',103,1,'04/12/16','12:00:00','HSB','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CH1#05',106,1,'02/12/16','11:00:00','CRC','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CH4#06',101,1,'01/12/16','10:00:00','PO','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CH4#06',102,1,'03/12/16','11:00:00','CRC','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CH4#07',101,1,'03/12/16','10:00:00','PO','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CH4#07',102,1,'03/12/16','11:00:00','CRC','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CH4#08',101,1,'01/12/16','10:00:00','PO','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CH4#08',102,1,'03/12/16','11:00:00','CRC','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CH4#09',101,1,'01/12/16','10:00:00','PO','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CH4#09',102,1,'03/12/16','11:00:00','CRC','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CH4#10',101,1,'03/12/16','10:00:00','PO','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CH4#10',102,1,'03/12/16','11:00:00','CRC','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS1#01',106,2,'02/12/16','12:00:00','CRC','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS1#01',107,1,'01/12/16','11:00:00','CRC','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS1#01',107,2,'02/12/16','12:00:00','CRC','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS1#02',106,1,'03/12/16','11:00:00','CRC','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS1#02',109,1,'03/12/16','10:00:00','PO','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS1#03',107,3,'02/12/16','13:00:00','CRC','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS1#03',109,1,'02/12/16','10:00:00','PO','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS1#04',104,1,'04/12/16','10:00:00','PO','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS1#04',106,1,'01/12/16','11:00:00','CRC','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS1#04',106,2,'02/12/16','12:00:00','CRC','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS1#04',107,1,'02/12/16','11:00:00','CRC','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS1#04',107,3,'02/12/16','13:00:00','CRC','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS1#04',109,1,'03/12/16','10:00:00','PO','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS1#05',104,1,'01/12/16','10:00:00','PO','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS1#05',105,1,'01/12/16','14:00:00','HSB','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS1#05',107,2,'01/12/16','12:00:00','CRC','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS1#05',107,1,'03/12/16','11:00:00','CRC','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS1#05',110,1,'01/12/16','10:00:00','PO','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS2#06',104,1,'04/12/16','10:00:00','PO','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS2#06',105,1,'02/12/16','14:00:00','HSB','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS2#06',106,2,'02/12/16','12:00:00','CRC','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS2#06',107,3,'01/12/16','13:00:00','CRC','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS2#06',109,1,'01/12/16','10:00:00','PO','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS2#06',110,1,'03/12/16','10:00:00','PO','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS2#07',104,1,'01/12/16','10:00:00','PO','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS2#07',105,1,'02/12/16','14:00:00','HSB','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS2#07',106,1,'02/12/16','11:00:00','CRC','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS2#07',106,2,'03/12/16','12:00:00','CRC','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS2#07',107,3,'02/12/16','13:00:00','CRC','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS2#07',107,2,'02/12/16','12:00:00','CRC','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS2#07',109,1,'01/12/16','10:00:00','PO','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS2#07',110,1,'03/12/16','10:00:00','PO','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS2#08',104,1,'04/12/16','10:00:00','PO','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS2#08',105,1,'01/12/16','14:00:00','HSB','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS2#08',106,1,'01/12/16','11:00:00','CRC','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS2#08',107,1,'02/12/16','11:00:00','CRC','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS2#08',107,2,'02/12/16','12:00:00','CRC','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS2#08',110,1,'01/12/16','10:00:00','PO','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS3#09',107,1,'02/12/16','11:00:00','CRC','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS3#09',107,3,'02/12/16','13:00:00','CRC','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS3#09',109,1,'03/12/16','10:00:00','PO','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS3#10',106,1,'01/12/16','11:00:00','CRC','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS3#10',106,2,'02/12/16','12:00:00','CRC','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS3#10',107,1,'01/12/16','11:00:00','CRC','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'CS3#10',109,1,'01/12/16','10:00:00','PO','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'EE1#01',107,1,'01/12/16','11:00:00','CRC','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'EE1#01',107,3,'02/12/16','13:00:00','CRC','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'EE1#02',106,1,'02/12/16','11:00:00','CRC','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'EE1#02',107,3,'02/12/16','13:00:00','CRC','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'EE1#03',104,1,'01/12/16','10:00:00','PO','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'EE1#03',104,2,'04/12/16','11:00:00','PO','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'EE1#03',105,1,'02/12/16','14:00:00','HSB','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'EE1#03',106,1,'02/12/16','11:00:00','CRC','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'EE1#03',107,1,'02/12/16','11:00:00','CRC','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'EE1#04',104,2,'01/12/16','11:00:00','PO','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'EE1#04',107,3,'02/12/16','13:00:00','CRC','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'EE1#05',104,2,'04/12/16','11:00:00','PO','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'EE1#05',107,1,'01/12/16','11:00:00','CRC','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'EE2#06',104,2,'04/12/16','11:00:00','PO','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'EE2#07',107,1,'02/12/16','11:00:00','CRC','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'EE2#08',104,2,'04/12/16','11:00:00','PO','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'EE2#08',105,1,'02/12/16','14:00:00','HSB','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'EE2#08',106,1,'03/12/16','11:00:00','CRC','Placed');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'EE2#09',104,2,'04/12/16','11:00:00','PO','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'EE2#09',105,1,'02/12/16','14:00:00','HSB','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'EE2#10',106,1,'01/12/16','11:00:00','CRC','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'EE3#13',104,1,'04/12/16','10:00:00','PO','WL');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'EE3#13',104,2,'04/12/16','11:00:00','PO','Rejected');
/* INSERT QUERY */INSERT INTO Interview(RollNo,Org_ID,Org_profile_ID,Date,Time,Place,Outcome) VALUES( 'EE3#14',106,1,'01/12/16','11:00:00','CRC','Placed');
