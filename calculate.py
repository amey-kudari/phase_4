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
    dur = int(dur[0][0])

    command ="select Cost from ROOM WHERE WingID=" + str(row[6]) + " and RoomNo=" + str(row[7])
    c.execute(command)
    cost = c.fetchall()
    cost = int(cost[0][0])

    total_cost = cost * dur
    print("  BILL")
    print("=========")
    print("Patient ID: ", row[0])
    print("Patient Name: ", row[1], " " ,row[2], " ",  row[3])
    print("Patient DOA: ", row[5])

    print("Total Cost: ", total_cost, "\n\n")

    return dur


def print_bill_sil(c, db, pat, curr_date):

    c.execute("select * from PATIENT WHERE PatientID = " + str(pat))
    rows = c.fetchall()
    row = rows[0]
    command = "select DATEDIFF(\'" + curr_date + "\', \'" + str(row[5]) + "\')"
    c.execute(command)
    dur = c.fetchall()
    dur = int(dur[0][0])
    command ="select Cost from ROOM WHERE WingID=" + str(row[6]) + " and RoomNo=" + str(row[7])
    c.execute(command)
    cost = c.fetchall()
    cost = int(cost[0][0])
    total_cost = cost * dur
    return total_cost   

def calculate_revenue(c,db):

    curr_date = input("Enter Today's Date: ")
    command = "select PatientID from PATIENT"
    c.execute(command)
    pat = c.fetchall()
    c.execute(command)
    total = 0
    for patid in pat:
        total += print_bill_sil(c,db, patid[0], curr_date)

    print("   Current Total Revenue")
    print("============================")
    print("-> $", total, "/-\n\n")
