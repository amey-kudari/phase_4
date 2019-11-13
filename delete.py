def del_patient(c,db):
    try:
        pat_id = input("enter patient id : ")
        c.execute("SELECT WingID FROM PATIENT WHERE PatientID = " + pat_id + ";")
        w_id = str(c.fetchone()[0])
        # print(w_id)
        c.execute("DELETE FROM PATIENT WHERE PatientID = " + pat_id + ";")
        c.execute("DELETE FROM NURSES WHERE PatientID = " + pat_id + ";")
        c.execute("DELETE FROM TREATS WHERE PatientID = " + pat_id + ";")
        c.execute("INSERT INTO TREATED VALUES(" + pat_id + "," + w_id + ");")
        # c.execute()

        db.commit()
        print(pat_id)
    except:
        print("error deleting patient, try again")
        db.rollback()