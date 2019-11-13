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
			WingID		INT,
			NurseID		INT,
			DoctorID	INT
			);""")

		c.execute("""create table SPECIALITY(
			DoctorID 	INT,
			Spec   		VARCHAR(50)
			);""")

		c.execute("""create table QUALIFICATIONS(
			DoctorID 	INT,
			Qual   		VARCHAR(50)
			);""")

		db.commit()
	except:
		print("ERROR CREATING TABLES, PLEASE TRY AGAIN")
		db.rollback()

	# try:
	# 	c.execute("""insert into STAFF values(1,'abc','A','def','1989-07-08','2015-11-01', 4, 35000, 14);""")
	# 	c.execute("""insert into STAFF values(2,'jhg','A','ytr','1984-02-05','2015-11-01', 4, 24000, 17);""")
	# 	c.execute("""insert into STAFF values(3,'djs','A','qwe','1983-05-01','2015-11-01', 4, 10000, 12);""")

	# 	c.execute("""insert into PATIENT values(1, 'kur', 'E', 'hey', '2019-11-01', 2, 201);""")
	# 	c.execute("""insert into PATIENT values(2, 'djf', 'E', 'ewi', '2019-11-02', 1, 323);""")
	# 	c.execute("""insert into PATIENT values(3, 'wqe', 'E', 'dsi', '2019-11-03', 1, 124);""")

	# 	db.commit()
	# except:
	# 	print("poiuytr")
	# 	db.rollback()
