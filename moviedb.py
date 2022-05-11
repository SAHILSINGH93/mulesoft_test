import sqlite3

# Create connection
connect= sqlite3.connect("Movies.db")
cursor=connect.cursor()

# Create a table 

command1="""CREATE TABLE IF NOT EXISTS
MOVIE( "MNAME" varchar2(20),
    "ACTOR" varchar2(20),
    "ACTRESS" varchar2(20),
    "YEAR" number(4),
    "DNAME" varchar(20))"""

cursor.execute(command1)

print("Table MOVIE Created!!")
print(".............................................................")

# Insert values into the table 
cursor.execute("INSERT INTO MOVIE VALUES('KGF','YASH','SRINIDHI',2022,'PRASHANTH NEEL')")
cursor.execute("INSERT INTO MOVIE VALUES('RAAZI','VICKY','ALIA BHAT',2018,'MEGHANA GULZAR')")
cursor.execute("INSERT INTO MOVIE VALUES('THAPPAD','PAVAIL','TAAPSE',2020,'ANUBHAV SINHA')")
cursor.execute("INSERT INTO MOVIE VALUES('RAID','AJAY DEVGAN','ILLEANA',2018,'RAJKUMAR GUPTA')")
cursor.execute("INSERT INTO MOVIE VALUES('BHUJ','AJAY DEVGAN','SONAKSHI SINHA',2021,'ABHISHEK DUDHAIYA')")
cursor.execute("INSERT INTO MOVIE VALUES('PK','AAMIR KHAN','ANUSHKA SHARMA',2014,'RAJKUMAR HIRANI')")
cursor.execute("INSERT INTO MOVIE VALUES('FIDAA','VARUN','SAI PALLAVI',2017,'SHEKAR KAMMULA')")
cursor.execute("INSERT INTO MOVIE VALUES('ROOHI','RAJKUMMAR','JANHVI',2021,'HARDIK MEHTA')")

# Query

cursor.execute("SELECT * FROM MOVIE")
rs=cursor.fetchall()
print("Movie     Actor      Actress     Year     Director")
print(".............................................................")
for i in range(len(rs)):
    print(str(rs[i][0])+"  |  "+str(rs[i][1])+"  |  "+str(rs[i][2])+"  |  "+str(rs[i][3])+"  |  "+str(rs[i][4]))
    print(".............................................................")

# other Queries
print("The movies acted by AJAY DEVGAN are:::::")
print(".............................................................")
cursor.execute("SELECT MNAME,ACTOR,ACTRESS,YEAR,DNAME FROM MOVIE WHERE ACTOR='AJAY DEVGAN'")

res=cursor.fetchall()
print("Movie     Actor      Actress     Year     Director")
print(".............................................................")
for i in range(len(res)):
    print(str(res[i][0])+"  |  "+str(res[i][1])+"  |  "+str(res[i][2])+"  |  "+str(res[i][3])+"  |  "+str(res[i][4]))
    print(".............................................................")