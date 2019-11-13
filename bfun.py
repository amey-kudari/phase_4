
def create_tables(c,db):
	try:
		table_names = ['STAFF', 'PATIENT', 'WING', 'ROOM', 'DEPENDENT', 'DOCTORS', 'NURSE', 'NURSES', 'WORKS_WITH', 'SPECIALITY', 'QUALIFICATIONS', 'TREATS', 'TREATED']
		for t in table_names:
			c.execute("drop table if exists " + t + ";")

		c.execute("""create table STAFF(
			StaffID INT,
			Fname	VARCHAR(50),
			Minit	VARCHAR(3),
			Lname	VARCHAR(50),
			DOB		DATE,
			DOJ		DATE,
			Wdays	INT,
			Salary_hr	INT,
			Whours	INT
			);""")

		c.execute("""create table PATIENT(
			PatientID	INT,
			Fname		VARCHAR(50),
			Minit		VARCHAR(3),
			Lname		VARCHAR(50),
			BloodGrp	VARCHAR(50),
			DOA			DATE,
			WingID		INT,
			ROOM        INT
			);""")


		c.execute("""create table WING(
			WingID 		INT,
			Warden		INT
			);""")

		c.execute("""create table ROOM(
			WingID		INT,
			RoomNo		INT,
			Floor		INT,
			Cost		INT
			);""")

		c.execute("""create table DEPENDENT(
			StaffID		INT,
			Fname		VARCHAR(50),
			Minit		VARCHAR(3),
			Lname		VARCHAR(50),
			Sex			VARCHAR(50),
			DOB			DATE,
			Relationship VARCHAR(50)
			);""")

		c.execute("""create table DOCTORS(
			StaffID 	INT,
			SuperID		INT,
			OfficeNo	INT,
			OnCall		VARCHAR(3)
			);""")


		c.execute("""create table NURSE(
			StaffID		INT
			);""")

		c.execute("""create table NURSES(
			PatientID	INT,
			NurseID		INT
			);""")

		c.execute("""create table WORKS_WITH(
			DoctorID 	INT,
			NurseID		INT
			);""")

		c.execute("""create table TREATS(
			DoctorID	INT,
			PatientID	INT
			);""")

		c.execute("""create table TREATED(
			PatientID	INT,
			WingID		INT
			);""")

		c.execute("""create table SPECIALITY(
			DoctorID 	INT,
			Spec   		VARCHAR(50)
			);""")

		c.execute("""create table QUALIFICATIONS(
			DoctorID 	INT,
			Qual   		VARCHAR(50)
			);""")

		# c.execute("insert into ROOM values (1, 123, 1, 1200);")
		# c.execute("insert into ROOM values (1, 223, 2, 1100);")
		# c.execute("insert into ROOM values (1, 323, 3, 1500);")
		
		# c.execute("""insert into STAFF values(1001,'Surya','M','Chand','1989-07-08','2011-11-01', 6, 1000,5);""")
		# c.execute("""insert into STAFF values(1002,'Chalu,'A','Gyan','1984-02-05','2013-11-01', 5, 10000, 6);""")

		# c.execute("""insert into STAFF values(2001,'SHeru','K','Pandey','1983-05-01','2012-06-01', 6, 100, 10);""")
		# c.execute("""insert into STAFF values(2002,'Ash','B','Bandi','1990-05-01','2011-02-01', 7, 100, 12);""")
		# c.execute("""insert into STAFF values(3001,'Bhanu','K','Sreekar','1980-05-01','2011-06-01', 7, 100, 12);""")
		# # c.execute("""insert into STAFF values(4,'qwe','A','qwe','1983-05-01','2015-11-01', 4, 10000, 12);""")
		# # c.execute("""insert into STAFF values(5,'fuk','C','you','1983-05-01','2015-11-01', 4, 10000, 12);""")




		# c.execute("""insert into PATIENT values(112, 'Suman', 'E', 'Chalan','A+', '2019-11-01', 1, 123);""")
		# c.execute("""insert into PATIENT values(113, 'Jag', 'E', 'Smith','B+', '2019-11-02', 1, 223);""")
		# c.execute("""insert into PATIENT values(114, 'Sumanth', 'E', 'Garlapati','O-', '2019-11-03', 1, 323);""")

		# c.execute("""insert into WING values(1, 3001);""")
		
		# c.execute("""insert into DEPENDENT values(1001, 'Chaitany', 'M', 'Chand', 'M', '2015-11-04',"Son");""")
		# c.execute("""insert into DEPENDENT values(1001, 'Sarala', 'K', 'Chand', 'F', '1970-11-04',"Wife");""")

		# c.execute("""insert into NURSES values(112,2001);""")
		# c.execute("""insert into NURSES values(112,2002);""")

		# c.execute("""insert into WORKS_WITH values(1001,2001);""")
		# c.execute("""insert into WORKS_WITH values(1002,2001);""")
		# c.execute("""insert into WORKS_WITH values(1001,2002);""")

		# c.execute("""insert into TREATS values(1001,112);""")
		# c.execute("""insert into TREATS values(1002,112);""")

		# c.execute("""insert into SPECIALITY values(1001,"ENT");""")
		# c.execute("""insert into SPECIALITY values(1001,"BONE");""")
		# c.execute("""insert into SPECIALITY values(1002,"LUNGS");""")

		# c.execute("""insert into QUALIFICATIONS values(1001,"MBBS");""")
		# c.execute("""insert into QUALIFICATIONS values(1001,"PHD");""")
		# c.execute("""insert into QUALIFICATIONS values(1002,"MBBS");""")
		# c.execute("""insert into QUALIFICATIONS values(1002,"PHD");""")

		# c.execute("""insert into TREATED values(112,1,2001,1001);""")
		# c.execute("""insert into TREATED values(112,1,2002,1002);""")
		
		# c.execute("""insert into DOCTOR values(1001,1002,123,"YES");""")
		# c.execute("""insert into DOCTOR values(1002,"NULL",224,"NO");""")



		
		# c.execute("""insert into PATIENT values(4, 'wqe', 'E', 'dsi','A', '2019-11-03', 1, 323);""")	
		# 
		# 
		c.execute("insert into ROOM values (1, 123, 1, 1200);")
		c.execute("insert into ROOM values (1, 223, 2, 1100);")
		c.execute("insert into ROOM values (1, 323, 3, 1500);")
		
		c.execute("""insert into STAFF values(1,'abc','A','def','1989-07-08','2015-11-01', 4, 35000, 14);""")
		c.execute("""insert into STAFF values(2,'jhg','A','ytr','1984-02-05','2015-11-01', 4, 24000, 17);""")
		c.execute("""insert into STAFF values(3,'djs','A','qwe','1983-05-01','2015-11-01', 4, 10000, 12);""")
		# c.execute("""insert into STAFF values(4,'qwe','A','qwe','1983-05-01','2015-11-01', 4, 10000, 12);""")
		# c.execute("""insert into STAFF values(5,'fuk','C','you','1983-05-01','2015-11-01', 4, 10000, 12);""")

		


		# c.execute("""insert into PATIENT values(1, 'kur', 'E', 'hey','A', '2019-11-01', 1, 123);""")
		# c.execute("""insert into PATIENT values(2, 'djf', 'E', 'ewi','A', '2019-11-02', 1, 223);""")
		# c.execute("""insert into PATIENT values(3, 'wqe', 'E', 'dsi','A', '2019-11-03', 1, 323);""")		
		# c.execute("""insert into PATIENT values(4, 'wqe', 'E', 'dsi','A', '2019-11-03', 1, 323);""")	

		print("inserted patients")
		db.commit()
	except:
		print("ERROR CREATING TABLES, PLEASE TRY AGAIN")
		db.rollback()

	# try:

	# 	db.commit()
	# except:
	# 	print("poiuytr")
	# 	db.rollback()
