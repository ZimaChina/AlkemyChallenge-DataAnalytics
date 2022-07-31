#Creacion base de datos en postgree
from sqlalchemy import create_engine
from normalizacion_datos import tabla_principal, df_registros, df_provincias

engine = create_engine("postgresql://postgres:123456@localhost:5432/tabla")
"""desde nuestro modulo de normalizacion de datos, pasar nuestras variables.csv a sql para crear las tablas"""
df_provincias.to_sql("tabla_provincias", con=engine, if_exists= "replace")
df_registros.to_sql("registros categorias", con=engine, if_exists= "replace")
tabla_principal.to_sql("tabla principal", con=engine, if_exists= "replace")