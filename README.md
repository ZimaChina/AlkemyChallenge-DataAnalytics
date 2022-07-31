# AlkemyChallenge-DataAnalytics
**Challenge de análisis de datos de Alkemy, donde se utilizaran Python, Pandas, SqlAlchemy y PostgreSQL como medios.**

<sub>1-Para realizar el deploy se deberá ejecutar primero el entorno virtual:</sub>

pip install virtualenv

<sub>2- A continuación dirigirse a la carpeta donde se quiera instalar el entorno y ejecutar lo siguiente bajo el nombre que le demos:</sub>

virtualenv nombre_entorno

<sub>3- Activar entorno:</sub>

.\nombre_entorno\Script\activate

<sub>4-Una vez tengamos el entorno activado, precederemos a instalar las siguientes dependencias en la consola:</sub>

pip install requests
pip install pandas
pip install sqlalchemy
pip install python-decouple

Una vcez instaladas, con "pip list" podemos chequear si las mismas fueron isntaladas, y sus versiones.

<sub>5- Por ultimo, dirigirse al directorio main.py y ejecutar los archivos en el siguiente órden:</sub>

python extraccion_datos.py
python normalizacion_datos.py
python db.py


