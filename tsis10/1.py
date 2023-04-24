import psycopg2
from config import host, user, password, database

try:
    connection = psycopg2.connect(
        host=host
        , user=user
        , password=password,
        database=database
    )
    connection.autocommit = True

    # create new table
    # with connection.cursor() as cursor:
    #     cursor.execute("""CREATE TABLE users(
    #         id serial PRIMARY KEY
    #         ,first_name varchar(50) NOT NULL
    #         ,nick_name varchar(50) NOT NULL);
    #                    """
    #     )
    #     print("[INFO] Table created succesfully")
    # insert values
    # with connection.cursor() as cursor:
    #     cursor.execute("""INSERT INTO users(first_name , nick_name) VALUES
    #                    ('dosymzhan' , 'DONI');
    #                    """
    #     )
    #     print("[INFO] Table created succesfully")
    # cursor.close()
    # connection.close()
    # print("[INFO] PostgreSQL connection closed")
    
    # DELETE A TABLE
    with connection.cursor() as cursor:
        cursor.execute("""DROP TABLE test_table;
                       """
        )
        print("Table was deleted")
    

except Exception as ex:
    print("[ERROR] Error while working with PostgreSQL:", ex)
