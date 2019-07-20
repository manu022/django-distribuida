#Django API-REST
Servidor Django para el proyecto de Computación Distribuida 2019 UTEM que otorga dos servicios Rest.

## Requisitos

Python 3.6
pip

### Para Instalar los paquetes necesarios

pip install -r requirements.txt

### Realizar migraciones

python manage.py makemigrations
python manage.py migrate

### Iniciar servidor

python manage.py runserver 0.0.0.0:8000

#URL Servicios

http://0.0.0.0:8000/upload/ : Se encarga de recibir el archivo 
http://0.0.0.0:8000/rest/ : Entrega los resultados luego de su análisis, posterior a eso el archivo es eliminado.
