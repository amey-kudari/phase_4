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