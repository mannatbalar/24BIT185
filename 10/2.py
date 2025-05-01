def read_csv():
    d = {}
    f = open("students.csv", "r")
    lines = f.readlines()
    f.close()

    for line in lines[1:]:
        row = line.strip().split(",")
        roll = int(row[0])
        name = row[1]
        m1 = int(row[2])
        m2 = int(row[3])
        m3 = int(row[4])
        total = m1 + m2 + m3
        d[roll] = [name, m1, m2, m3, total]
    
    print(d)

read_csv()
