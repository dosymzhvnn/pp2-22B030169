import psycopg2
import csv
def main():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password= "doni2005"
    )
    on=True
    mode='ASC'
    conn.autocommit = True
    all_contacts2=[]

    with conn.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS phonebook(
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(20) NOT NULL,
        phone_number VARCHAR(20) NOT NULL
        ) """)
    while on:
        choice =int(input("Enter your choice:\n1. Add Contact\n2. Delete Contact\n3. Update Contact\n4. Look Contacts\n5. Resort\n6. Find By Pattern\n:"))
        if choice == 1:
                all_contacts=list(input("input like:aaa 8747,bbb 87535,...:").split(","))
                for contact in all_contacts:
                    contactsplited=contact.split(" ")
                    if len(contactsplited)==1 or len(contactsplited)==0:
                        print("something is missing try writting'NAME PHONENUMBER'")
                    elif not contactsplited[1].isdigit():
                        print(f"{contactsplited[1]} phonenumber is incorrect")
                    else:
                        all_contacts2.append(contact)

                if len(all_contacts2)!=0:
                    with conn.cursor() as cursor:
                        cursor.execute(f"call create_contacts(ARRAY{all_contacts2})")
                
        elif choice == 4:
            with conn.cursor() as cursor:
                if mode=='ASC':
                    cursor.execute(f"""SELECT * FROM phonebook ORDER BY first_name ASC""")
                if mode=='DESC':
                    cursor.execute(f"""SELECT * FROM phonebook ORDER BY first_name DESC""")
                all=cursor.fetchall()
                for _,name,phone in all:
                    print("|"+name+"___"+phone+"|")
        elif choice == 2:
            name_to_delete=input("Enter contact to delete: ")
            with conn.cursor() as cursor:
                cursor.execute(f"CALL delete_contact('{name_to_delete}')")
        elif choice == 3:
            editing_name=input("what contact you will update?: ")
            new_name=input("new name: ")
            new_number=input("new phone number: ")
            with conn.cursor() as cursor:
                cursor.execute(f"UPDATE phonebook SET first_name='{new_name}' WHERE first_name='{editing_name}'")
                cursor.execute(f"UPDATE phonebook SET phone_number='{new_number}' WHERE first_name='{new_name}'")
        elif choice ==5:
            mode_change=input("1. By ASC\n2. By DESC")
            pagination_offset=int(input("Enter Offset: "))
            pagination_limit=int(input("Enter Limit: "))

            if mode_change==1:
                mode='ASC'
                with conn.cursor() as cursor:
                    cursor.execute(f"""SELECT * from get_sorting_asc('DESK',{pagination_limit},{pagination_offset})""")
                    all=cursor.fetchall()
                    for name,phone in all:
                        print("|"+name+"___"+phone+"|")
            else:
                mode='DESC'
                with conn.cursor() as cursor:
                    cursor.execute(f"""SELECT * from get_sorting_desc('DESK',{pagination_limit},{pagination_offset})""")
                    all=cursor.fetchall()
                    for name,phone in all:
                        print("|"+name+"___"+phone+"|")
       
        elif choice == 6:
            with conn.cursor() as cursor:
                patt=input("Enter Pattern:")
                with conn.cursor() as cursor:
                    cursor.execute("SELECT find(%s)",[patt] )
                    result = cursor.fetchall()
                    print(result)

if __name__ == "__main__":
    main()