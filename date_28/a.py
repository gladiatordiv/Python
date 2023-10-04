import pyodbc
Driver_Name = "SQL SERVER"
Server_Name = "LAPTOP-AK8HVF4P\SQLEXPRESS"
Database_Name = "Cars_and_employees"
connection_string = f"DRIVER={{SQL Server}};SERVER={Server_Name};DATABASE={Database_Name};"
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()
# create_table = """
# CREATE TABLE Employee_data_(
#     id int,
#     name varchar(50),
#     city varchar(50),
#     email varchar(100),
#     dob varchar(30),
# );
# """
    
# insert_query = """
# INSERT INTO Employee_data_(id, name, city, email, dob)
# VALUES (1, 'DIVYA', 'BEAWAR', 'divya@gmail.com', '2002-07-30'),
#         (2, 'SNEHA', 'JODHPUR', 'sneha@gmail.com', '2004-10-27'),
#         (3, 'KRISHI', 'UDAIPUR', 'krishi@gmail.com', '2002-08-06'),
#         (4, 'SAKSHI', 'JODHPUR', 'sakshi@gmail.com', '2002-09-12'),
#         (5, 'AYUSH', 'BEAWAR', 'ayush@gmail.com', '2002-12-28');
# """
    
# add_column = """
#     ALTER TABLE Employee_data_
#     ADD is_active BIT DEFAULT 1;
#     """

# update_query = """
#     UPDATE Employee_data_
#     SET is_active = 0
#     WHERE id = 1;
#     """
# cursor.execute(create_table)
# cursor.execute(insert_query)
# cursor.execute(add_column)
# cursor.execute(update_query)


select_query = "SELECT * FROM Employee_data_"
cursor.execute(select_query)
for row in cursor:
    print(row)
connection.commit()
connection.close()

