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
    cur.close()
    
def search(name , phone):
    cur.execute("""SELECT * FROM PhoneBook WHERE name ILIKE %s
                """ , (name or phone))
    rows = cur.fetchall()
    cur.close()
    return rows

def delete(pattern):
    cur.execute("""DELETE FROM PhoneBooK WHERE name ILIKE %s OR phone ILIKE %s
                """ , ('%'+pattern+'%' , '%'+pattern+'%' ))
    cur.close()
    
def update(name , phone):
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
    cur.close()
        
def querying_data():
    cur.execute("SELECT * FROM PhoneBook")
    rows = cur.fetchall()
    for row in rows:
        print(rows)
    cur.close()
        
def upload_csv(filename):
    with open (filename , 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            name = row[0]
            phone = row[1]
            cur.execute("""INSERT INTO PhoneBook(name , phone)
                        VALUES  (%s , %s )
                        """ , (name , phone))
    cur.close()
            
while True:
    print('PHONEBOOK PROGRAM')
    print('1. Add Entry')
    print('2. Search Entry')
    print('3. Querying data')
    print('4. Update Entry')
    print('5. Upload csv File')
    print('6. Quit')
    print('7. Delete Entry')
    choice = input('Enter your choice (1-7): ')
    
    if choice == '1':
        name = input("Enter name: ")
        phone = input('Enter phone: ')
        add_data(name , phone)
    elif choice == '2':
        name = input('Enter name: ')
        rows = search(name)
        for row in rows:
            print(row)
    elif choice == '3':
        querying_data()
    if choice == '4':
        name = input('Enter name: ')
        phone = input('Enter phone: ')
        update(name , phone)
    if choice == '5':
        filename = input('Enter csv filename')
        upload_csv(filename)
    if choice == '6':
        break
    if choice == '7':
        pattern = input('Enter pattern of Entry, that you want to delete: ')
        delete(pattern)
    else:
        print('Invalid choice.')
        
    
conn.close()