import csv
file=open("student.csv","w",newline='')
writer=csv.writer(file)
writer.writerow(["name","marks"])
writer.writerow(["Hardik","100"])
file.close()


file=open("student.csv","r")
reader=csv.reader(file)
for row in reader:
    print(row)
file.close()


file=open("student.csv","a")
writer=csv.writer(file)
writer.writerow(["Rahul","91"])
file.close()