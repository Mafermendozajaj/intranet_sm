Generacion de la base de datos

createuser --createdb intranet_sm
createdb -O intranet_sm intranet_sm
psql intranet_sm -c "ALTER USER intranet_sm with password 'intranetSM23'";

Hacer las migraciones

./manage.py makemigrations
./manage.py migrate

Crea un usuario adminitrador


./manage.py createsuperuser

Correr el programa

./manage.py runserver
