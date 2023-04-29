import psycopg2 , csv
from config import host,database,user,password

conn = psycopg2.connect(
    host= host
    ,user= user
    ,password=password
    ,database=database
)
conn.autocommit = True
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS PhoneBook(
    id SERIAL PRIMARY KEY
    ,name VARCHAR(50)
    ,phone VARCHAR(20)
)""")


def add_data(name , phone):
    with conn.cursor() as cursor:
        cur.execute("""INSERT INTO PhoneBook(name , phone)
                VALUES (%s , %s)""", (name , phone)
                )
        
def delete(pattern):
    with conn.cursor() as cursor:
        cur.execute("""DELETE FROM PhoneBooK WHERE name ILIKE %s OR phone ILIKE %s
                """ , ('%'+pattern+'%' , '%'+pattern+'%' ))
    
def update(name , phone):
    with conn.cursor() as cursor:
        cur.execute("""SELECT FROM PhoneBook WHERE name = %s OR phone = %s
                """ , (name , phone))
    user = cur.fetchone()
    if user == None:
        cur.execute("""INSERT INTO PhoneBook (name , phone) 
                    VALUES (%s , %s )
                    """ , (name , phone))
    else:
        cur.execute("""UPDATE PhoneBook 
                    SET phone = %s WHERE name = %s""" ,(phone , name))
        
def querying_data():
    with conn.cursor() as cursor:
        print('If you want to return all records, enter "all" ')
        print('If you want to return records with pagination, enter "pagination"')
        print('If you want to return all records based on a pattern, enter "ptn"')
        choice = input()
        if choice == 'all':
            cur.execute("SELECT * FROM PhoneBook")
            rows = cur.fetchall()
            for row in rows:
                print(rows)
        elif choice == 'pagination':
            limit = input('Number of limit: ')
            offset = input('Number of offset: ')
            cur.execute("""SELECT * FROM PhoneBook 
                LIMIT %s 
                OFFSET %s""" , (limit , offset))
            rows = cur.fetchall()
            for row in rows:
                print(row)
        elif choice == 'ptn':
            pattern = input('Enter a pattern: ')
            cur.execute("""SELECT * FROM PhoneBooK WHERE name ILIKE %s OR phone ILIKE %s
                """ , ('%'+pattern+'%' , '%'+pattern+'%' ))
            rows = cur.fetchall()
            for row in rows:
                print(row)
            
def upload_csv(filename):
    with conn.cursor() as cursor:
        with open (filename , 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                name = row[0]
                phone = row[1]
                cur.execute("""INSERT INTO PhoneBook(name , phone)
                        VALUES  (%s , %s )
                        """ , (name , phone))
    
def add_many_users():
    with conn.cursor() as cursor:
        users = []
        while True:
            name = input("Enter name (or 'e' to exit): ")
            if name.lower() == 'e':
                break
            phone = input('Enter phone: ')
            users.append((name, phone))

    for name, phone in users:
            add_data(name, phone)
    
    incorrect = []
    for name, phone in users:
        if len(phone) != 10 or not phone.isdigit():
            incorrect.append((name, phone))

    return incorrect
            
while True:
    print('PHONEBOOK PROGRAM')
    print('1. Add Entry')
    print('2. Querying data')
    print('3. Upload csv File')
    print('4. Delete Entry')
    print('5. Add many new users')
    print('6. Quit')
    choice = input('Enter your choice (1-6): ')
    
    if choice == '1':
        name = input("Enter name: ")
        phone = input('Enter phone: ')
        update(name , phone)
    elif choice == '2':
        querying_data()
    elif choice == '3':
        filename = input('Enter csv filename: ')
        upload_csv(filename)
    elif choice == '6':
        break
    elif choice == '4':
        pattern = input('Enter a pattern to delete: ')
        delete(pattern)
    elif choice == '5':
        incorrect = add_many_users()
        if incorrect:
            print("The following entries have incorrect phone numbers:")
            for name, phone in incorrect:
                print(name, phone)
    else:
        print('Invalid choice.')
conn.close()