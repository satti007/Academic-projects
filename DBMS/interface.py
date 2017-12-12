import mysql.connector
from mysql.connector import Error
 
def query_with_fetchone(conn,data):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM %s "%data)
        row = cursor.fetchone()
        while row is not None:
            print(row)
            row = cursor.fetchone()
    except Error as e:
        print(e)

def DISPLAY(conn):
  cursor = conn.cursor()
  cursor.execute("SHOW TABLES")
  for (table_name,) in cursor:
        print(table_name)
  data=raw_input("Pick a table: ")
  query_with_fetchone(conn,data)
  operations(conn)

def ADD(conn):
  cursor = conn.cursor()
  cursor.execute("SHOW TABLES")
  for (table_name,) in cursor:
        print(table_name)
  table=raw_input("Pick a table: ")
  cursor.execute("SELECT column_name FROM information_schema.columns WHERE  table_name = '%s'"%table)
  print('Attributes of the table are: ')
  i=0;
  for (columns,) in cursor:
    print(columns)
    i=i+1
  Attributes=[]
  for k in range(1,i+1):
     data=raw_input("Enter the Attribute%d: "%k )
     Attributes.append(data)
  cmd= "INSERT INTO "+table+" VALUES" +"("
  for i in range(0,len(Attributes)):
    if(i==len(Attributes)-1):
      cmd=cmd+"'"+Attributes[i]+"'"
    else:
      cmd=cmd+"'"+Attributes[i]+"'"+","
  cmd=cmd+")"+";"
  print(cmd)
  try:
    cursor.execute(cmd)
    conn.commit()
  except Error as e:
    print(e)
  operations(conn)

def DELETE(conn):
  cursor=conn.cursor()
  cursor.execute("SHOW TABLES")
  for (table_name,) in cursor:
        print(table_name)
  table=raw_input("Pick a Table: ")
  cursor.execute("SELECT column_name FROM information_schema.columns WHERE  table_name = '%s'"%table)
  print('Attributes of the table are: ')
  for (columns,) in cursor:
    print(columns)
  Attributes=raw_input("Enter Attributes: ").split()
  Values=raw_input("Enter Values: ").split()
  cmd="DELETE FROM "+table+" WHERE "
  for attr,val in zip(Attributes,Values):
    cmd=cmd+attr+"="
    try:
      float(val)
      cmd=cmd+val+" AND "
    except Exception as e:
      cmd=cmd+"'"+val+"' AND "  
  cmd=cmd[:len(cmd)-4]+";"
  #print(cmd)
  try:
    cursor.execute(cmd)
    conn.commit()
  except Error as e:
    print(e)
  operations(conn)

def UPDATE(conn):
  cursor=conn.cursor()
  cursor.execute("SHOW TABLES")
  for (table_name,) in cursor:
        print(table_name)
  table=raw_input("Pick a Table: ")
  cursor.execute("SELECT column_name FROM information_schema.columns WHERE  table_name = '%s'"%table)
  print('Attributes of the table are: ')
  for (columns,) in cursor:
    print(columns)
  Attributes=raw_input("Attributes to be Updated: ").split()
  Values=raw_input("Values to be Updated: ").split()
  Query_Attributes=raw_input("Attributes to be Queried: ").split()
  Query_Values=raw_input("Values to be Queried: ").split()
  cmd="UPDATE "+table+" SET "
  for attr,val in zip(Attributes,Values):
    cmd=cmd+attr+"="
    try:
      float(val)
      cmd=cmd+val+" , "
    except Exception as e:
      cmd=cmd+"'"+val+"' , "  
  cmd=cmd[:len(cmd)-2]+" WHERE "
  for attr,val in zip(Query_Attributes,Query_Values):
    cmd=cmd+attr+"="
    try:
      float(val)
      cmd=cmd+val+" AND "
    except Exception as e:
      cmd=cmd+"'"+val+"' AND "
  cmd=cmd[:len(cmd)-4]+" ;"
  print(cmd)
  try:
    cursor.execute(cmd)
    conn.commit()
  except Error as e:
    print(e)
  operations(conn)
    

def EXIT(conn):
  conn.close()
  print('Connection closed.') 

def operations(conn):
  print('1. ADD a row to a table')
  print('2. DELETE a row from a table')       
  print('3. UPDATE or MODIFY certain values in a table')       
  print('4. DISPLAY the contents of a table')       
  print('5. EXIT')
  data=int(raw_input("Choose an option: "))
  options = {
              1 : ADD,
              2 : DELETE,
              3 : UPDATE,
              4 : DISPLAY,
              5 : EXIT ,
            }
  options[data](conn)
        

def connect():
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='Student_Placements',
                                       user='root',
                                       password='A')
        if conn.is_connected():
            print('Connected to Student_Placements database')
    
        operations(conn)
    except Error as e:
        print(e)
 
 
if __name__ == '__main__':
    connect()