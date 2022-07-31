from extraccion_datos import datos_bibliotecas, datos_cines, datos_museos
import pandas as pd


#Normalizacion de datos
"""
A traves de la libreria read_csv tomamos las direcciones generadas en el modulo de extraccion de datos."""

df_bibliotecas = pd.read_csv("bibliotecas/2022-julio/bibliotecas-14-07-2022.csv")

df_museos = pd.read_csv("museos/2022-julio/museos-14-07-2022.csv")

df_cines = pd.read_csv("cines/2022-julio/cines-14-07-2022.csv")

"""Removemos las columnas con informacion innecesaria."""

df_bibliotecas2 = df_bibliotecas.drop(["Observacion", "Departamento","Piso", "Cod_tel", "Información adicional","Latitud", "Longitud", "TipoLatitudLongitud","Fuente", "Tipo_gestion",	"año_inicio",	"Año_actualizacion"], axis=1)
df_museos2 = df_museos.drop(["Observaciones", "subcategoria","nombre", "piso", "cod_area", "Latitud", "Longitud", "TipoLatitudLongitud", "Info_adicional", "fuente", "jurisdiccion", "año_inauguracion", "actualizacion"], axis=1)
df_cines2 = df_cines.drop(["Observaciones", "Departamento", "Piso", "cod_area", "Información adicional", "Latitud", "Longitud", "TipoLatitudLongitud", "Fuente", "tipo_gestion",	"Pantallas",	"Butacas",	"espacio_INCAA", "año_actualizacion"], axis=1)

"""Creamos la tabla principal con las columnas requeridas"""
tabla_principal = pd.DataFrame(columns=["Codigo localidad", "id_provincia", "Id_departamento ", "Categoría", "Provincia", "Localidad", "Nombre", "Domicilio", "Código postal", "Número de teléfono", "Mail", "Web"])

"""Cambiamos el nombre de cada columna para luego unificarlas"""
df_bibliotecas2 = df_bibliotecas2.rename(columns={"Codigo localidad":"Cod_Loc", "IdProvincia":"id_provincia", "Id_departamento ":"id_departamento", "Categoría":"Categoría", "Provincia":"provincia", "Localidad":"localidad", "Nombre":"nombre", "Domicilio":"domicilio", "CP":"código postal", "Teléfono":"número de teléfono",  "Mail":"mail", "Web":"web"})

df_museos2 = df_museos2.rename(columns={"Cod_Loc":"Codigo localidad", "IdProvincia":"id_provincia", "IdDepartamento":"id_departamento", "categoria":"Categoría","Provincia":"provincia", "direccion":"domicilio", "CP":"código postal", "telefono":"número de teléfono",  "Mail":"mail", "Web":"web"})

df_cines2 = df_cines2.rename(columns={"Cod_Loc":"Codigo localidad", "IdProvincia":"id_provincia", "Id_departamento  ":"id_departamento", "Categoría":"Categoría", "Provincia":"provincia","Dirección":"domicilio", "CP":"código postal", "Teléfono":"número de teléfono",  "Mail":"mail", "Web":"web"})

"""Unificacion de dataframes"""
tabla_principal = tabla_principal.append(df_bibliotecas2)
tabla_principal = tabla_principal.append(df_museos2)
tabla_principal = tabla_principal.append(df_cines2)

tabla_principal = tabla_principal.T.drop_duplicates().T
tabla_principal = tabla_principal.fillna("0")

tabla_principal.dropna(thresh=1)

#Tabla categorias, fuente y provincias
"""Normalizacion tabla categorias y fuentes"""
df_museos3 = df_museos.rename(columns={"categoria":"Categoría","fuente":"Fuente","nombre":"Nombre", "provincia":"Provincia", })
df_archivos = df_museos3.append(df_cines).append(df_bibliotecas)
df_archivos2 = df_archivos.drop(["Cod_Loc", "IdProvincia", "Observaciones", "IdDepartamento", "subcategoria", "direccion", "CP", "piso", "cod_area", "telefono", "Mail", "Web", "Latitud", "Longitud", "TipoLatitudLongitud", "jurisdiccion", "año_inauguracion", "Info_adicional", "Departamento", "localidad", "Localidad", "Dirección", "Piso", "Teléfono", "tipo_gestion", "Pantallas", "Butacas", "espacio_INCAA", "Observacion", "Subcategoria", "Domicilio", "Tipo_gestion", "año_inicio","año_actualizacion", "Información adicional", "Año_actualizacion", "actualizacion"], axis=1)

df_registros = df_archivos2.pivot_table(values="Nombre", index=["Provincia"], columns=["Categoría", "Fuente"], aggfunc="count", margins=True)
"""utilizamos .fillna para reemplazar los datos NaN y reconocerlos como nulos"""
df_registros= df_registros.fillna("0")

#Tabla datos de Cines
"""Normalizacion tabla provincias"""
df_provincias = df_cines[["Provincia", "Pantallas", "Butacas", "espacio_INCAA"]]
df_provincias = df_provincias.rename(columns={"espacio_INCAA":"Espacio INCAA"})
df_provincias["Espacio INCAA"] = df_provincias["Espacio INCAA"].replace("si", "SI").replace("SI", 1)
df_provincias["Espacio INCAA"] = df_provincias["Espacio INCAA"].fillna(0)
df_provincias["Espacio INCAA"] = df_provincias["Espacio INCAA"].astype("int")
df_provincias = df_provincias.groupby("Provincia").sum()
