# def update_staff_salary(c,db):
# 	try:
# 		StaffID = input("Enter StaffID: ")
#      	new_sal = input("Enter Update Salary: ")
# 		command = "UPDATE STAFF SET Salary_hr = " + new_sal + " WHERE StaffID = " + StaffID + ";"
# 		c.execute(command)
# 		db.commit()
# 	except:
# 		print("error updating value, please try again")
# 		db.rollback()

# def update_patient(c,db):
# 	try:
# 		pid = input("Enter PatientID of patient: ")
# 		attr = input("Enter attribute to change: ")
# 		new_val = input("Enter updated value of attribute: ")
# 		command = "UPDATE PATIENT SET " + attr + " = " + new_val + " WHERE PatientID = " + pid
# 		c.execute(command)
# 		db.commit()
# 	except:
# 		print("Error updating Patient Details")
# 		db.rollback()