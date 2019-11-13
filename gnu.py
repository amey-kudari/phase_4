import pymysql,sys,random
import bfun
import insert
import update

def main():
    db = pymysql.connect("localhost","newuser","password","TDB" )
    c = db.cursor()
    bfun.create_tables(c,db)
    c.execute("SHOW TABLES")
    print(c.fetchall())

    while True:
        val = int(input("""What would you like to do? Options:
            1 : make an entry
            2 : update an entry
            3 : delete an entry
            4 : update Salary DONE
            5 : print bill 
            6 : generate report 
            7 : show staff
            8 : show patients
            9 : quit\n"""))

        if val == 1:
            print(val)
            etype = input("enter the type of entity (doctor/nurse/patient/dependent) : ")
            print(etype)
            # if etype == "room":
            #     arr = ['WingID','RoomNo','Floor','Cost']
            #     room = dict()
            #     for i in arr: room[i]=input("enter the " + i + " : ")
            #     insert.addroom(c,db,room)
            # if etype == "warden":
            #     wid = input("enter wing id : ")
            #     wnm = input("enter warden name : ")
            #     print(wid)
            if etype == "doctor":
                arr = ['StaffID','Fname','Minit','Lname','DOB','DOJ','Wdays','Salary/hr','Whours','SuperID','OfficeNo','OnCall']
                doc = dict()
                for i in arr: doc[i] = input("enter the " + i + " : ")
                insert.addstaff(c,db,doc)
                print(doc)
                for q in range(0,int(input("how many qualifications : "))):
                    qual = input("enter qualifications : ")
                
            
            if etype == "nurse":
                arr = ['StaffID','Fname','Minit','Lname','DOB','DOJ','Wdays','Salary/hr','Whours','DoctorID']
                nurse = dict()
                for i in arr: nurse[i] = input("enter the " + i + " : ")
                print(nurse)


            if etype == "patient":
                insert.addpatient(c,db)
                # for n in range(0,int(input("how many nurses : "))):
                #     nurse = input("enter nurse id : ")
                # for d in range(0,int(input("how many doctors : "))):
                #     doc = input("enter doctor id : ")



            # staff = dict()
            # arr = ['StaffID','Fname','Minit','Lname','DOB','DOJ','Wdays','Salary/hr','Whours']
            # for i in arr: staff[i]=input("enter the " + i + " : ")
            # print(staff)
            
        if val == 2:
            print(val)
            # update.update_patient(c,db)
        if val == 3:
            print(val)
        if val == 4:
            print(val)
            # update.update_staff_salary(c, db)
        if val == 5:
            print(val)
        if val == 6:
            print(val)
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

    db.close()

if __name__=='__main__': main()


