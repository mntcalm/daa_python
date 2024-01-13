CALL public.list_for_surname('last_name 20');
SELECT last_name, first_name, middle_name FROM Users WHERE last_name = 'last_name 20';
CALL public.list_for_name('first_name 31');
SELECT last_name, first_name, middle_name FROM Users WHERE last_name = 'last_name 20';
#SELECT proname, proargtypes, proargnames, prosrc FROM pg_proc WHERE proname = 'list_for_surname';
#SELECT proname, proargtypes, proargnames, prosrc FROM pg_proc WHERE proname = 'list_for_name';
