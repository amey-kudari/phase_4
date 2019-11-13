import pymysql,sys,random
import bfun
import insert, delete
import update
import calculate

def main():
    db = pymysql.connect("localhost","newuser","password","TDB" )
    c = db.cursor()
    bfun.create_tables(c,db)
    c.execute("SHOW TABLES")
    print(c.fetchall())

    while True:
        val = int(input("""What would you like to do? Options:
            1  : make an entry
            2  : update an entry
            3  : delete an entry
            4  : update Salary DONE
            5  : print bill 
            6  : generate report 
            7  : show staff
            8  : show patients
            9  : quit
            10 : debug\n"""))

        if val == 1:
            print(val)
            etype = input("enter the type of entity (doctor/nurse/patient/dependent) : ")
            print(etype)

            if etype == "doctor":
                arr = ['StaffID','Fname','Minit','Lname','DOB','DOJ','Wdays','Salary/hr','Whours','SuperID','OfficeNo','OnCall']
                doc = dict()
                for i in arr: doc[i] = input("enter the " + i + " : ")
                insert.addstaff(c,db,doc)
                print(doc)
                for q in range(0,int(input("how many qualifications : "))):
                    insert.addqual(c,db,doc['StaffID'])
                
            
            if etype == "nurse":
                arr = ['StaffID','Fname','Minit','Lname','DOB','DOJ','Wdays','Salary/hr','Whours','DoctorID']
                nurse = dict()
                for i in arr: nurse[i] = input("enter the " + i + " : ")
                print(nurse)


            if etype == "patient":
                p_id = insert.addpatient(c,db)
                for n in range(0,int(input("how many nurses : "))):
                    nurse = input("enter nurse id : ")
                    insert.lnk_np(c,db,nurse,p_id)
                for d in range(0,int(input("how many doctors : "))):
                    doc = input("enter doctor id : ")
                    insert.lnk_dp(c,db,doc,p_id)

            # staff = dict()
            # arr = ['StaffID','Fname','Minit','Lname','DOB','DOJ','Wdays','Salary/hr','Whours']
            # for i in arr: staff[i]=input("enter the " + i + " : ")
            # print(staff)

        if val == 2:
            print(val)
            update.update_patient(c,db)

        if val == 3:
            print(val)
            delete.del_patient(c,db)

        if val == 4:
            print(val)
            update.update_staff_salary(c, db)
        if val == 5:
            print(val)
            calculate.print_bill(c,db)
        if val == 6:
            print(val)
            calculate.calculate_revenue(c,db)
        if val == 7:
            print(val)
            # select * from STAFF;
            c.execute("select * from STAFF")
            rows = c.fetchall()
            print(rows)
            for row in rows:
                print(row)
        if val == 8:
            print(val)
            # select * from PATIENT;
            c.execute("select * from PATIENT")
            rows = c.fetchall()
            print(rows)
            for row in rows:
                print(row)        
        if val == 9: 
            break
        if val == 10:
            table_names = ['STAFF', 'PATIENT', 'WING', 'ROOM', 'DEPENDENT', 'DOCTORS', 'NURSE', 'NURSES', 'SPECIALITY', 'QUALIFICATIONS', 'TREATS', 'TREATED']
            for t in table_names:
                print(" --------------- ")
                print("TABLE : " + t)
                c.execute("SELECT * FROM " + t + ";")
                d = c.fetchall()
                if len(d):
                    for i in d : print(i)

    db.close()

if __name__=='__main__': main()


