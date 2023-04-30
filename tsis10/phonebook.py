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
    cur.execute("""INSERT INTO PhoneBook(name , phone)
                VALUES (%s , %s)""", (name , phone)
                )

def delete(name):
    with conn.cursor() as cursor:
        cur.execute("""DELETE FROM PhoneBooK WHERE name ILIKE %s
                """ , (name))
    
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
        print('BY ASC ENTER "asc" and BY DESC ENTER "desc" ')
        choice = input()
        if choice == 'asc':
            cur.execute("SELECT * FROM PhoneBook ORDER BY name ASC" )
            rows = cur.fetchall() 
            for row in rows: 
                print(row)
        elif choice == 'desc':
            cur.execute("SELECT * FROM PhoneBook ORDER BY name DESC")
            rows = cur.fetchall()
            print(rows)
        
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
            
while True:
    print('PHONEBOOK PROGRAM')
    print('1. Add Entry')
    print('2. Querying data')
    print('3. Update Entry')
    print('4. Upload csv File')
    print('5. Delete Entry')
    print('6. Quit')
    choice = input('Enter your choice (1-6): ')
    
    if choice == '1':
        name = input("Enter name: ")
        phone = input('Enter phone: ')
        add_data(name , phone)
    elif choice == '2':
        querying_data()
    elif choice == '3':
        name = input('Enter name: ')
        phone = input('Enter phone: ')
        update(name , phone)
    elif choice == '4':
        filename = input('Enter csv filename: ')
        upload_csv(filename)
    elif choice == '5':
        name = input('Enter name to delete: ')
        delete(name)
    elif choice == '6':
        break
    else:
        print('Invalid choice.')
        
    
conn.close()