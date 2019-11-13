# def addroom(c,db,room):
# 	print(room)
# 	# {'WingID': '1', 'RoomNo': '2', 'Floor': '3', 'Cost': '100'}
# 	command = "INSERT INTO ROOM VALUES ("
# 	order = ['WingID','RoomNo','Floor','Cost']
# 	try:
# 		for i in order: command += (room[i]+',')
# 		fcommand = command[:-1] + ')'
# 		command = fcommand
# 		print(command)
# 	except:
# 		print("error adding room, please try again")
# 		db.rollback()

def addstaff(c,db,staff):
	try:
		#            0        1       2       3      4     5       6       7          8
		order = ['StaffID','Fname','Minit','Lname','DOB','DOJ','Wdays','Salary/hr','Whours']
		command = "INSERT INTO STAFF VALUES (" + staff[order[0]] + ',\'' + staff[order[1]] + '\',\'' + staff[order[2]] + '\',\'' + staff[order[3]] + '\',\'' + staff[order[4]] + '\',\'' 
		rest = staff[order[5]] + '\',' + staff[order[6]] + ',' + staff[order[7]] + ',' + staff[order[8]]
		print(command+rest + ');')
		c.execute(command+rest+');')
		db.commit()
		# for i
	except:
		print("ERROR ADDING STAFF") 

def addqual(c,db,staff):
	try:
		qual = input("Enter Qualification")
		command = "INSERT INTO QUALIFICATIONS VALUES ( " + staff + ", \'" + qual + "\')"
		print(command)
		c.execute(command)
		db.commit()
	except:
		print("Error adding Qualification")

def addpatient(c, db):
	try:
		patid = input("Enter PatientID: ")
		fname = input("Enter First Name: ")
		minit = input("Enter Middle Initials: ")
		lname = input("Enter Last Name: ")
		bldg = input("Enter Blood Group: ")
		doa = input("Enter Date of Admission: ")
		wingid = input("Enter WingID: ")
		room = input("Enter Room no: ")

		command = "INSERT INTO PATIENT VALUES (" + patid + ',\'' + fname + '\',\''+ minit + '\',\''+ lname + '\',\''+ bldg + '\', \''+ doa + '\', '+ wingid + ',' + room + ')'  
		print(command)
		c.execute(command)
		db.commit()
		return patid
	except:
		print("Error registering new patient")
		db.rollback()

def lnk_np(c,db,n_id,p_id):
	try:
		c.execute("INSERT INTO NURSES VALUES(" + p_id + "," + n_id + ");")
		db.commit()
	except:
		print("error linking nurse and patient")
		db.rollback()

def lnk_dp(c,db,d_id,p_id):
	try:
		c.execute("INSERT INTO TREATS VALUES(" + d_id + "," + p_id + ");")
		db.commit()
	except:
		print("error linking doctor and patient")
		db.rollback()		