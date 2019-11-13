def print_bill(c, db):
    pat = input("Enter Patient ID")
    c.execute("select * from PATIENT WHERE PatientID = " + pat)
    rows = c.fetchall()
    print(rows)
    for row in rows:
        print(row[0])
        # if(row[0]==pat):
        print(row[5],row[6],row[7])



# def calculate_revenue()