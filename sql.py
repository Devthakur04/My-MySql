import mysql.connector

class Sql:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )
        self.cursor = self.mydb.cursor()

    def create_db(self, db_name):
        self.cursor.execute(f'create database if not exists {db_name}')

    def create_table(self, db_name, table_name):
        self.cursor.execute(f'use {db_name}')
        self.cursor.execute(f'create table if not exists {table_name} (name varchar(20), id int primary key)')

    def insert_values(self, table_name, values):
        sql = f'insert into {table_name} (name, id) values (%s, %s)'
        self.cursor.executemany(sql, values)
        self.mydb.commit()
        print(self.cursor.rowcount, 'record(s) inserted')

    def select_all(self, table_name):
        self.cursor.execute(f'select * from {table_name}')
        result = self.cursor.fetchall()
        for x in result:
            print(x)

    def delete_record(self, table_name, name):
        self.cursor.execute(f"delete from {table_name} where name = '{name}'")
        self.mydb.commit()
        print(self.cursor.rowcount, 'record(s) deleted')

def main():
    sql = Sql()

    while True:
        print("\n1. Create Database")
        print("2. Create Table")
        print("3. Insert Values")
        print("4. Select All Records")
        print("5. Delete Record")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            db_name = input("Enter database name: ")
            sql.create_db(db_name)

        elif choice == '2':
            db_name = input("Enter database name: ")
            table_name = input("Enter table name: ")
            sql.create_table(db_name, table_name) 

        elif choice == '3':
            table_name = input("Enter table name: ")
            num_records = int(input("Enter number of records to insert: "))
            values = []
            for i in range(num_records):
                name = input(f"Enter name for record {i + 1}: ")
                id_val = int(input(f"Enter id for record {i + 1}: "))
                values.append((name, id_val))
            sql.insert_values(table_name, values)

        elif choice == '4':
            table_name = input("Enter table name: ")
            sql.select_all(table_name)

        elif choice == '5':
            table_name = input("Enter table name: ")
            delete_name = input("Enter name to delete: ")
            sql.delete_record(table_name, delete_name)

        elif choice == '6':
            print("Exiting program...")
            break

        else:
            print("Invalid input. Please enter a valid choice.")

if __name__ == '__main__':
    main() 

    
