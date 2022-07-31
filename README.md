# AlkemyChallenge-DataAnalytics
Challenge de análisis de datos de Alkemy, donde se utilizaran Python, Pandas, SqlAlchemy y PostgreSQL como medios.

1-Para realizar el deploy se deberá ejecutar primero el entorno virtual:

pip install virtualenv

2- A continuación dirigirse a la carpeta donde se quiera instalar el entorno y ejecutar lo siguiente bajo el nombre que le demos:

virtualenv nombre_entorno

3- Activar entorno:

.\nombre_entorno\Script\activate

4-Una vez tengamos el entorno activado, precederemos a instalar las siguientes dependencias en la consola:

pip install requests
pip install pandas
pip install sqlalchemy
pip install python-decouple

Una vcez instaladas, con "pip list" podemos chequear si las mismas fueron isntaladas, y sus versiones.

5- Por ultimo, dirigirse al directorio main.py y ejecutar los archivos en el siguiente órden:

python extraccion_datos.py
python normalizacion_datos.py
python db.py


