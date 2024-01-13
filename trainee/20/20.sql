CREATE OR REPLACE PROCEDURE public.list_for_surname (IN surname VARCHAR(255))
LANGUAGE SQL
AS $$
UPDATE Users SET middle_name = 'PROCEDURED!!!' WHERE last_name = surname;
$$;

CREATE OR REPLACE PROCEDURE public.list_for_name (IN name VARCHAR(255))
LANGUAGE SQL
AS $$
UPDATE Users SET middle_name = 'PROCEDURED!!!' WHERE first_name = name;
$$;

