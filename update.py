def update_staff_salary(c,db,sal, StaffID):
	try:
		command = "UPDATE STAFF SET Salary_hr = " +str(sal) + " WHERE StaffID = " + str(StaffID) + ";"
		c.execute(command)
		db.commit()
	except:
		print("error updating value, please try again")
		db.rollback()