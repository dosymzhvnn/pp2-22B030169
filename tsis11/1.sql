CREATE OR REPLACE  FUNCTION find(patt VARCHAR)
RETURNS TABLE(
    name VARCHAR(20) ,
    phone VARCHAR(20)
) AS
$$
declare
    finde varchar :=CONCAT('%',patt,'%');
BEGIN
  RETURN QUERY
  SELECT m.name,m.phone from Phonebook m
  WHERE m.name LIKE finde or m.phone LIKE finde;
END;
$$
LANGUAGE plpgsql;
DROP FUNCTION find;
SELECT find('d');


CREATE PROCEDURE create_contact(namer VARCHAR,phone_numb VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO Phonebook(name,phone)
    VALUES(namer,phone_numb);
END;
$$;
CALL create_contact('klnlln','23234');
DROP Procedure create_contact;




CREATE PROCEDURE update_contact(namer VARCHAR,phone_numb VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE Phonebook set phone=phone_numb WHERE name=namer;
END;
$$;
CALL update_contact('qwer','1');
SELECT * FROM Phonebook;

DROP PROCEDURE update_contact;





CREATE PROCEDURE create_contacts(list_in TEXT[])
LANGUAGE plpgsql
AS $$
DECLARE
  item VARCHAR;
  i INTEGER;
BEGIN
    FOREACH item IN ARRAY list_in LOOP
        SELECT count(*) INTO i from Phonebook WHERE name = split_part(item,' ',1);
        IF i = 0 THEN
            INSERT INTO Phonebook(name,phone)
            VALUES( split_part(item,' ',1),split_part(item,' ',2));
        ELSE 
            UPDATE Phonebook set phone=split_part(item,' ',2) WHERE name=split_part(item,' ',1);
            i:=0;
        END IF;
    END LOOP;
END;
$$;
CALL create_contacts(array['sgs 1','rrgerg 456454545']);
SELECT * from Phonebook;
DROP Procedure create_contacts;





CREATE FUNCTION get_sorting_desc(modee text,pagination_limit INTEGER,pagination_offset INTEGER)
RETURNS TABLE(
    name2 VARCHAR(20) ,
    phone VARCHAR(20)
) AS
$$
DECLARE
   
BEGIN
  RETURN QUERY
  SELECT m.name,m.phone from Phonebook m 
  ORDER BY m.name DESC
  OFFSET pagination_offset
  LIMIT pagination_limit;
END;
$$
LANGUAGE plpgsql;

DROP FUNCTION get_sorting_desc;

SELECT * FROM Phonebook ORDER BY name DESC;
SELECT * from get_sorting_desc('DESK',4,0);




CREATE FUNCTION get_sorting_asc(modee text,pagination_limit INTEGER,pagination_offset INTEGER)
RETURNS TABLE(
    name2 VARCHAR(20) ,
    phone VARCHAR(20)
) AS
$$
DECLARE
   
BEGIN
  RETURN QUERY
  SELECT m.name,m.phone from Phonebook m 
  ORDER BY m.name ASC
  OFFSET pagination_offset
  LIMIT pagination_limit;
END;
$$
LANGUAGE plpgsql;




CREATE PROCEDURE delete_contact(something VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM Phonebook
    WHERE name = something OR phone = something;
END
$$;
CALL delete_contact('3333333333');
SELECT * FROM Phonebook;