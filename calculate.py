def print_bill(c, db):
    curr_date = input("Enter Today's Date: ")
    pat = input("Enter Patient ID: ")
    c.execute("select * from PATIENT WHERE PatientID = " + pat)
    rows = c.fetchall()
    print(rows)
    for row in rows:
        print(row[0])
        # if(row[0]==pat):
        print(row[5],row[6],row[7])
    command = "select DATEDIFF(\'" + curr_date + "\', \'" + str(row[5]) + "\')"
    print(command)
    c.execute(command)
    dur = c.fetchall()

    # command = "select Cost from ROOM WHERE WingID"

    return dur[0][0]



# def calculate_revenue():
